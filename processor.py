"""
Code Processing Engine
Handles file migration, chunking, and API interactions.
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any, Union

from config import DEFAULT_CHUNK_SIZE
from llm_client import MultiProviderClient
from prompts import prompt_manager
from utils import normalize_model_name, chunk_code, ensure_directory


class MigrationManager:
    """Manages the migration process for PHP files."""
    
    def __init__(self, multi_client: MultiProviderClient, test_files: Dict[str, str]):
        self.multi_client = multi_client
        self.test_files = test_files
    
    @staticmethod
    def save_response(response_data: Dict[str, Any], file_path: Path, metadata: Dict[str, Any] = None):
        """Save API response with consistent metadata format."""
        ensure_directory(file_path.parent)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("=== RAW MODEL RESPONSE ===\n")
            
            # Write metadata
            if metadata:
                for key, value in metadata.items():
                    f.write(f"{key.capitalize()}: {value}\n")
            
            f.write(f"Length: {len(response_data['content'])} characters\n")
            f.write(f"Usage: {response_data.get('usage', {})}\n")
            f.write(f"Timestamp: {datetime.now()}\n")
            f.write("=" * 50 + "\n\n")
            f.write(response_data['content'])
    
    def process_api_call(self, model_name: str, prompt: str, output_path: Path, metadata: Dict[str, Any]) -> Optional[str]:
        """Unified API call processing with error handling."""
        print(f"🔗 Making API call via multi-provider client...")
        
        # Make API call
        result = self.multi_client.make_api_call(model_name, prompt)
        print(f"📊 Provider: {result.get('provider', 'unknown').upper()}")
        
        if not result['success']:
            print(f"❌ API Error: {result['error']}")
            return None
        
        # Validate response
        raw_response = result['content']
        print(f"📏 Response length: {len(raw_response)} characters")
        
        if not raw_response or len(raw_response.strip()) < 10:
            print(f"❌ Model response is empty or too short")
            return None
        
        # Save response
        metadata['provider'] = result.get('provider', 'unknown').upper()
        self.save_response(result, output_path, metadata)
        print(f"✅ Response saved to: {output_path}")
        
        return raw_response
    
    def migrate_file_single(self, filename: str, original_code: str, model_name: str, strategy: str) -> Optional[str]:
        """Migrate single file using multi-provider client."""
        prompt = prompt_manager.create_prompt(original_code, strategy)
        print(f"📏 Prompt length: {len(prompt):,} characters")
        
        # Create output path
        model_short = normalize_model_name(model_name)
        base_name = filename.replace('.php', '')
        output_file = Path('model_output') / model_short / f"{base_name}.txt"
        
        return self.process_api_call(model_name, prompt, output_file, {
            'file': filename, 'model': model_name, 'strategy': strategy
        })
    
    def migrate_file_chunked(self, filename: str, original_code: str, model_name: str, strategy: str, chunk_size: int) -> List[Optional[str]]:
        """Migrate large file using organized chunking."""
        chunks = chunk_code(original_code, chunk_size)
        total_chunks = len(chunks)
        
        print(f"📦 Split into {total_chunks} chunks of ~{chunk_size} lines each")
        
        # Create organized folder structure
        model_short = normalize_model_name(model_name)
        file_base = filename.replace('.php', '')
        
        file_dir = Path('chunked_model_output') / model_short / file_base
        ensure_directory(file_dir)
        print(f"📁 Saving chunks to: {file_dir}")
        
        # Process chunks
        chunk_strategy = f"chunk_{strategy}" if not strategy.startswith('chunk_') else strategy
        all_responses = []
        
        for i, chunk_info in enumerate(chunks, 1):
            print(f"\n[Chunk {i}/{total_chunks}] Processing lines {chunk_info['start_line']}-{chunk_info['end_line']}...")
            
            # Create prompt and make API call
            prompt = prompt_manager.create_prompt(
                chunk_info['code'], chunk_strategy,
                filename=filename, start_line=chunk_info['start_line'],
                end_line=chunk_info['end_line'], total_lines=chunk_info['total_lines'],
                chunk_number=i, total_chunks=total_chunks
            )
            
            print(f"📏 Chunk prompt length: {len(prompt):,} characters")
            response = self.process_api_call(model_name, prompt, file_dir / f"{i}.txt", {
                'file': filename, 'model': model_name, 'strategy': chunk_strategy, 'chunk': i
            })
            
            all_responses.append(response)
            status = "✅" if response else "❌"
            print(f"{status} Chunk {i} {'processed successfully' if response else 'failed'}")
        
        # Summary
        successful_chunks = sum(1 for r in all_responses if r is not None)
        print(f"\n🎉 Chunked migration completed!")
        print(f"✅ Successful chunks: {successful_chunks}/{total_chunks}")
        print(f"📁 All chunks saved in: {file_dir}")
        
        return all_responses
    
    def migrate_file(self, filename: str, model_name: str, strategy: str = "basic", 
                    chunk_size: int = None, auto_chunk: bool = True) -> Union[str, List[Optional[str]], None]:
        """Enhanced migration function with multi-provider support."""
        
        chunk_size = chunk_size or DEFAULT_CHUNK_SIZE
        
        if filename not in self.test_files:
            print(f"❌ File '{filename}' not found")
            return None
        
        original_code = self.test_files[filename]
        line_count = len(original_code.split('\n'))
        
        print(f"🚀 Migrating {filename} using {model_name} with {strategy} strategy...")
        print(f"📏 Input code length: {len(original_code):,} characters ({line_count:,} lines)")
        
        # Decide processing method
        if auto_chunk and line_count > chunk_size:
            print(f"📦 Large file detected ({line_count} lines) - using organized chunking")
            return self.migrate_file_chunked(filename, original_code, model_name, strategy, chunk_size)
        else:
            print(f"📄 Processing as single file ({line_count} lines, chunk limit: {chunk_size})")
            return self.migrate_file_single(filename, original_code, model_name, strategy)
    
    def batch_migrate(self, filenames: List[str], model: str = "gemini-1.5-pro", strategy: str = "basic", 
                     chunk_size: int = None, auto_chunk: bool = True) -> List[Union[str, List[Optional[str]], None]]:
        """Migrate multiple files with multi-provider chunking support."""
        chunk_size = chunk_size or DEFAULT_CHUNK_SIZE
        provider = self.multi_client.detect_provider(model)
        
        print(f"🔄 Batch migrating {len(filenames)} files using {provider.upper()}")
        if auto_chunk:
            print(f"📦 Auto-chunking enabled for files > {chunk_size} lines")
        
        results = []
        stats = {'files': 0, 'chunks': 0, 'success_files': 0, 'success_chunks': 0}
        
        for i, filename in enumerate(filenames, 1):
            print(f"\n[{i}/{len(filenames)}] Processing {filename}...")
            result = self.migrate_file(filename, model, strategy, chunk_size=chunk_size, auto_chunk=auto_chunk)
            results.append(result)
            
            # Update statistics
            stats['files'] += 1
            if result is not None:
                if isinstance(result, list):  # Chunked file
                    stats['chunks'] += len(result)
                    stats['success_chunks'] += sum(1 for r in result if r is not None)
                    if any(r is not None for r in result):
                        stats['success_files'] += 1
                else:  # Single file
                    stats['chunks'] += 1
                    stats['success_chunks'] += 1
                    stats['success_files'] += 1
        
        # Summary
        print(f"\n🎉 Batch migration completed!")
        print(f"✅ Successful files: {stats['success_files']}/{stats['files']}")
        if stats['chunks'] > len(filenames):
            print(f"📦 Total chunks processed: {stats['success_chunks']}/{stats['chunks']}")
        
        return results

"""
Prompt Templates and Management System
Handles different prompting strategies for PHP code migration.
"""

from typing import Dict, Any


# Basic prompting template
BASIC_PROMPT_TEMPLATE = """You are a senior PHP developer with expertise in legacy code modernization.
Your task is to migrate this legacy PHP code to PHP 8.3 standards using modern syntax and features while maintaining functional equivalence.

Please migrate the following PHP code up to PHP 8.3 standards:

{code}

Your response should follow this EXACT format:

// MIGRATION_START
[your migrated PHP code here]
// MIGRATION_END

CRITICAL FORMATTING REQUIREMENT: 
- Place the MIGRATION_START marker BEFORE the opening <?php tag
- Place the MIGRATION_END marker AFTER the closing PHP code
- Do NOT place these markers inside the PHP code itself

Provide only the migrated PHP code with the markers placed correctly outside the PHP code block, no additional commentary."""

# Comprehensive prompting template
COMPREHENSIVE_PROMPT_TEMPLATE = """You are a senior PHP developer with expertise in legacy php code modernization.
Your task is to migrate old PHP code up to PHP 8.3 standards using specific modern features like strict typing, constructor property promotion, match expressions, union types, and secure function replacements while preserving compatibility and maintaining the functionality of the original code etc.

Migration Requirements:
1. Update deprecated syntax
2. Replace deprecated functions
3. Implement modern PHP features
4. Improve security and code quality
5. Maintain functional equivalence
6. Enforce strict typing
7. Adopt core PHP 8.3 constructs

Please migrate the following PHP code to PHP 8.3:

{code}



Your response should follow this EXACT format:

// MIGRATION_START
[your migrated PHP code here]
// MIGRATION_END

CRITICAL FORMATTING REQUIREMENT: 
- Place the MIGRATION_START marker BEFORE the opening <?php tag
- Place the MIGRATION_END marker AFTER the closing PHP code
- Do NOT place these markers inside the PHP code itself

Include the markers as comments OUTSIDE the PHP code block. Keep the original comments as they are.
Do not add any other text, explanations, or commentary outside the markers. Make sure you give the COMPLETE migrated code."""

# Chunking basic template
CHUNK_BASIC_PROMPT_TEMPLATE = """You are a senior PHP developer with expertise in legacy code modernization. 
Your task is to migrate this PARTIAL SEGMENT of a larger PHP file up to PHP 8.3 standards using modern syntax and features.


CONTEXT:
- Original file: {filename}
- Processing lines: {start_line} to {end_line} (of {total_lines} total lines)
- This is chunk {chunk_number} of {total_chunks}

CRITICAL INSTRUCTIONS FOR PARTIAL CODE SEGMENTS:
1. This is ONLY a SEGMENT of a larger file - DO NOT try to complete it
2. DO NOT add opening <?php tags unless the segment starts with one
3. DO NOT add closing ?> tags unless the segment already has one  
4. DO NOT add any closing braces }} that are not in the original segment
5. DO NOT add any opening braces {{ that are not in the original segment
6. DO NOT try to complete class definitions, function definitions, or any code structures
7. If the segment starts mid-function, keep it mid-function
8. If the segment ends mid-function, keep it mid-function
9. Preserve the EXACT START and END boundaries of the provided code segment

WARNING: Adding extra braces or completing code structures will break the reconstruction process!

Please migrate ONLY the following PHP code segment up to PHP 8.3 standards:

{code}

Your response should follow this EXACT format:

// MIGRATION_START
[your migrated code segment here - exactly as provided, no additions]
// MIGRATION_END

CRITICAL FORMATTING REQUIREMENT: 
- Place the MIGRATION_START marker BEFORE the code segment
- Place the MIGRATION_END marker AFTER the code segment  
- Do NOT place these markers inside the PHP code itself

Migrate only the provided code segment. Do not add any missing parts or try to complete incomplete structures."""

# Chunking comprehensive template
CHUNK_COMPREHENSIVE_PROMPT_TEMPLATE = """You are a senior PHP developer with expertise in legacy code modernization. 
Your task is to migrate this PARTIAL SEGMENT of a larger PHP file up to PHP 8.3 standards using specific modern features like strict typing, constructor property promotion, match expressions, union types, and secure function replacements etc.


CONTEXT:
- Original file: {filename}
- Processing lines: {start_line} to {end_line} (of {total_lines} total lines)  
- This is chunk {chunk_number} of {total_chunks}

CRITICAL INSTRUCTIONS FOR PARTIAL CODE SEGMENTS:
1. This is ONLY a SEGMENT of a larger file - DO NOT try to complete it
2. DO NOT add opening <?php tags unless the segment starts with one
3. DO NOT add closing ?> tags unless the segment already has one
4. DO NOT add any closing braces }} that are not in the original segment
5. DO NOT add any opening braces {{ that are not in the original segment  
6. DO NOT try to complete class definitions, function definitions, or any code structures
7. If the segment starts mid-function, keep it mid-function
8. If the segment ends mid-function, keep it mid-function
9. Preserve the EXACT START and END boundaries of the provided code segment

WARNING: Adding extra braces or completing code structures will break the reconstruction process!

Migration Requirements for this segment:
1. Update deprecated syntax
2. Replace deprecated functions
3. Implement modern PHP features
4. Adopt core PHP 8.3 constructs

Please migrate ONLY the following PHP code segment to PHP 8.3:

{code}

Your response should follow this EXACT format:

// MIGRATION_START
[your migrated code segment here - exactly as provided, no additions]
// MIGRATION_END

CRITICAL FORMATTING REQUIREMENT: 
- Place the MIGRATION_START marker BEFORE the code segment
- Place the MIGRATION_END marker AFTER the code segment
- Do NOT place these markers inside the PHP code itself

Include the markers as comments OUTSIDE the code segment. Keep the original comments as they are.
Migrate only the provided code segment. Do not add missing functions, classes, or try to complete the file."""


class PromptManager:
    """Manages prompt templates and creation for different migration strategies."""
    
    def __init__(self):
        self.templates = {
            'basic': BASIC_PROMPT_TEMPLATE,
            'comprehensive': COMPREHENSIVE_PROMPT_TEMPLATE,
            'chunk_basic': CHUNK_BASIC_PROMPT_TEMPLATE,
            'chunk_comprehensive': CHUNK_COMPREHENSIVE_PROMPT_TEMPLATE,
        }
    
    def create_prompt(self, code: str, strategy: str = "basic", **kwargs) -> str:
        """Create migration prompts using different strategies."""
        if strategy not in self.templates:
            raise ValueError(f"Unknown prompting strategy: {strategy}. Available: {list(self.templates.keys())}")
        
        template = self.templates[strategy]
        
        # For chunking strategies, we need additional parameters
        if strategy.startswith('chunk_'):
            required_params = ['filename', 'start_line', 'end_line', 'total_lines', 'chunk_number', 'total_chunks']
            missing_params = [param for param in required_params if param not in kwargs]
            if missing_params:
                raise ValueError(f"Chunking strategy requires parameters: {missing_params}")
        
        return template.format(code=code, **kwargs)
    
    def get_available_strategies(self) -> list:
        """Get list of available prompting strategies."""
        return list(self.templates.keys())
    
    def validate_strategy(self, strategy: str) -> bool:
        """Validate if a strategy exists."""
        return strategy in self.templates
    
    def print_strategies(self):
        """Print available strategies."""
        print("🎯 Available prompting strategies:")
        for strategy in self.templates.keys():
            print(f"   📋 {strategy}")


# Global prompt manager instance
prompt_manager = PromptManager()

# Initialize and show available strategies
print("✅ Prompting strategies configured")
print(f"📋 Available strategies: {prompt_manager.get_available_strategies()}")
print("🔧 All prompts configured to prevent placing MIGRATION markers inside PHP code")
print("⚠️  Chunking strategies include warnings about NOT completing code structures")

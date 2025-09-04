# LLM Migration Tool - Python Scripts

This directory contains the converted Python scripts from your Jupyter notebook, organized into a clean, modular structure.

## 🏗️ Project Structure

```
├── config.py              # Configuration and environment setup
├── llm_client.py          # Multi-provider LLM client
├── prompts.py             # Prompt templates and management
├── utils.py               # Utility functions and helpers
├── processor.py           # File processing and migration engine
├── parser.py              # Output parsing and file reconstruction
├── migrate.py             # Main CLI script
├── example.py             # Usage examples
└── requirements.txt       # Python dependencies
```

## 📦 Script Overview

### 1. `config.py` - Configuration Manager
- Loads environment variables (API keys)
- Initializes OpenRouter and Google AI clients
- Manages provider configuration
- Sets up global constants

### 2. `llm_client.py` - Multi-Provider Client
- Handles API calls to different LLM providers
- Automatic provider detection
- Unified response handling
- Error management and retries

### 3. `prompts.py` - Prompt Management
- Basic and comprehensive prompting strategies
- Chunking-specific templates
- Template validation and parameter handling
- Strategy selection utilities

### 4. `utils.py` - Utility Functions
- File loading and validation
- PHP-aware code chunking
- Function boundary detection
- File size analysis tools

### 5. `processor.py` - Migration Engine
- Single file and batch migration
- Chunked file processing
- API call orchestration
- Progress tracking and statistics

### 6. `parser.py` - Output Processing
- Response parsing and code extraction
- MIGRATION_START/END marker handling
- File reconstruction from chunks
- Clean PHP file output generation

### 7. `migrate.py` - Main CLI Interface
- Command-line argument parsing
- Workflow orchestration
- Progress reporting
- Error handling

## 🚀 Quick Start

### Basic Usage (CLI)
```bash
# Migrate first 3 files with basic strategy
python migrate.py --model gemini-1.5-pro --strategy basic --limit 3

# Migrate specific files with comprehensive strategy
python migrate.py --files file1.php file2.php --model anthropic/claude-3.5-sonnet --strategy comprehensive

# Analyze file sizes
python migrate.py --analyze

# Parse existing responses
python migrate.py --parse

# Reconstruct chunked files
python migrate.py --reconstruct
```

### Programmatic Usage
```python
from config import config
from llm_client import MultiProviderClient
from processor import MigrationManager
from utils import load_test_files

# Load files and initialize system
test_files = load_test_files('selected_100_files/extra_large_1000_plus')
multi_client = MultiProviderClient(config.get_providers())
migration_manager = MigrationManager(multi_client, test_files)

# Migrate files
results = migration_manager.batch_migrate(
    list(test_files.keys())[:3],
    model='gemini-1.5-pro',
    strategy='basic',
    auto_chunk=True
)
```

## 🛠️ Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file:
   ```env
   OPENROUTER_API_KEY=your_openrouter_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. **Ensure PHP files are available:**
   - Place your test files in `selected_100_files/` directory
   - Or specify custom directory with `--files-dir`

## 📋 Command Line Options

```bash
python migrate.py --help
```

### File Selection
- `--files file1.php file2.php` - Migrate specific files
- `--files-dir path/to/files` - Directory containing PHP files
- `--all-files` - Migrate all loaded files
- `--limit N` - Limit to N files

### Model and Strategy
- `--model MODEL_NAME` - LLM model to use
- `--strategy basic|comprehensive` - Migration strategy

### Chunking
- `--chunk-size N` - Chunk size for large files (default: 500)
- `--no-auto-chunk` - Disable automatic chunking

### Actions
- `--analyze` - Analyze file sizes only
- `--migrate` - Perform migration (default)
- `--parse` - Parse existing responses
- `--reconstruct` - Reconstruct files from chunks
- `--test` - Test provider detection

## 🔧 Configuration

### Supported Models
- **Google AI:** `gemini-1.5-pro`, `gemini-1.5-flash`, `gemini-1.0-pro`
- **OpenRouter:** `anthropic/claude-3.5-sonnet`, `meta-llama/llama-3.1-8b-instruct`, etc.

### Strategies
- **Basic:** Simple migration with modern PHP syntax
- **Comprehensive:** Advanced migration with strict typing, match expressions, etc.

### Chunking
- Automatically chunks large files (>500 lines by default)
- Respects PHP function boundaries
- Smart reconstruction from chunks

## 📁 Output Structure

```
├── model_output/           # Raw API responses (single files)
│   └── model_name/
│       └── file.txt
├── chunked_model_output/   # Raw API responses (chunked files)
│   └── model_name/
│       └── filename/
│           ├── 1.txt
│           ├── 2.txt
│           └── ...
└── new-version/           # Final migrated PHP files
    └── model_name/
        └── file.php
```

## 🧪 Examples

Run the example script to see different usage patterns:
```bash
python example.py
```

## 🔍 Troubleshooting

1. **API Keys not found:**
   - Ensure `.env` file exists with correct keys
   - Check environment variable names

2. **No files loaded:**
   - Verify file directory exists
   - Check file permissions
   - Ensure PHP files have `.php` extension

3. **Provider errors:**
   - Test provider detection with `--test` flag
   - Check API key validity
   - Verify internet connection

## 🎯 Benefits of Modular Structure

1. **Maintainability:** Each script has a single responsibility
2. **Reusability:** Components can be used independently
3. **Testability:** Easy to unit test individual modules
4. **Extensibility:** Simple to add new providers or strategies
5. **CLI-Ready:** Professional command-line interface
6. **Error Handling:** Robust error management throughout

## 🔄 Migration from Notebook

Your original notebook functionality is preserved but organized into:
- **Setup → config.py**
- **Multi-provider client → llm_client.py**
- **Prompts → prompts.py**
- **Processing → processor.py**
- **Parsing → parser.py**
- **Execution → migrate.py**

The scripts maintain full compatibility with your existing data and workflows!

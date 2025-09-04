# Simple main.py - Direct execution of notebook commands
# Just hardcode and run - exactly like the notebook

# Import everything we need (same as notebook)
import os
import json
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import warnings
import openai
from dotenv import load_dotenv
warnings.filterwarnings('ignore')

# Load environment variables
load_dotenv()

# Initialize clients (same as notebook)
print("🔬 Multi-Provider LLM Migration Tool Initialized")
print(f"⚙️  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# OpenRouter client
try:
    OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
    openrouter_client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )
    print("✅ OpenRouter client initialized successfully")
except Exception as e:
    print(f"❌ Error initializing OpenRouter client: {e}")
    openrouter_client = None

# Google AI client
try:
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    import google.genai as genai
    google_client = genai.Client(api_key=GOOGLE_API_KEY)
    print("✅ Google AI client initialized successfully")
except Exception as e:
    print(f"❌ Error initializing Google AI client: {e}")
    google_client = None

# Provider configuration
PROVIDERS = {
    'openrouter': {
        'client': openrouter_client,
        'api_key': OPENROUTER_API_KEY,
        'enabled': openrouter_client is not None
    },
    'google': {
        'client': google_client,
        'api_key': GOOGLE_API_KEY,
        'enabled': google_client is not None
    }
}

enabled_providers = [name for name, config in PROVIDERS.items() if config['enabled']]
print(f"\n🎯 Available providers: {', '.join(enabled_providers)}")

# Import all the notebook functions
from llm_client import MultiProviderClient
from processor import MigrationManager
from parser import OutputParser, FileReconstructor
from utils import load_test_files

# Initialize multi-provider client
multi_client = MultiProviderClient(PROVIDERS)

# Load test files (same as notebook)
test_files = {}
old_version_path = Path('selected_100_files/extra_large_1000_plus')

if old_version_path.exists():
    for php_file in old_version_path.rglob('*.php'):
        try:
            with open(php_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if content.strip():
                    test_files[php_file.name] = content
        except Exception as e:
            print(f"⚠️  Could not load {php_file.name}: {e}")
    
    print(f"📁 Loaded {len(test_files)} PHP files")
else:
    print("❌ selected_100_files directory not found")

# Create migration manager 
migration_manager = MigrationManager(multi_client, test_files)

# Create parsers (same as notebook)
parser = OutputParser()
reconstructor = FileReconstructor(parser)

# EXACTLY THE SAME COMMANDS AS THE NOTEBOOK:
print("\n🚀 Starting batch migration...")

# UNCOMMENT THESE LINES FOR BATCH MIGRATION WITH DIFFERENT PROVIDERS:

# Google AI batch migration:
# migration_manager.batch_migrate(list(test_files.keys())[:3], model='gemini-1.5-pro', strategy='basic')

# OpenRouter batch migration:
# migration_manager.batch_migrate(list(test_files.keys())[:3], model='mistralai/mistral-small-3.2-24b-instruct:free', strategy='basic')

# Mixed provider batch (you can mix and match in sequence):
migration_manager.migrate_file('003_wp-db.php', 'gemini-1.5-flash', 'basic')
# migration_manager.migrate_file('file2.php', 'anthropic/claude-3.5-sonnet', 'comprehensive')

print("\n🔄 Processing responses and reconstructing files...")
parser.process_all_responses()
reconstructor.reconstruct_all_files()

print("✅ Done!")

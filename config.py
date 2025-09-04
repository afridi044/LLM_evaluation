"""
Configuration and Environment Setup for LLM Migration Tool
Handles API keys, client initialization, and global settings.
"""

import os
import warnings
from datetime import datetime
from dotenv import load_dotenv
import openai

# Suppress warnings
warnings.filterwarnings('ignore')

# Load environment variables
load_dotenv()

# Constants
DEFAULT_CHUNK_SIZE = 500  # Default chunk size in lines

class Config:
    """Configuration manager for LLM migration tool."""
    
    def __init__(self):
        self.openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
        self.openrouter_client = None
        self.google_client = None
        self.providers = {}
        
        # Initialize clients and providers
        self._initialize_clients()
        
    def _initialize_clients(self):
        """Initialize API clients for different providers."""
        print("🔬 Multi-Provider LLM Migration Tool Initialized")
        print(f"⚙️  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Initialize OpenRouter client
        self._init_openrouter()
        
        # Initialize Google AI client
        self._init_google()
        
        # Setup provider configuration
        self._setup_providers()
        
    def _init_openrouter(self):
        """Initialize OpenRouter client."""
        try:
            if not self.openrouter_api_key:
                raise ValueError("OPENROUTER_API_KEY not found in environment variables.")
            
            self.openrouter_client = openai.OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=self.openrouter_api_key,
            )
            print("✅ OpenRouter client initialized successfully")
        except Exception as e:
            print(f"❌ Error initializing OpenRouter client: {e}")
            self.openrouter_client = None
    
    def _init_google(self):
        """Initialize Google AI client."""
        try:
            if not self.google_api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment variables.")
            
            # Import and configure Google AI with new API
            import google.genai as genai
            
            # Create client with API key
            self.google_client = genai.Client(api_key=self.google_api_key)
            print("✅ Google AI client initialized successfully")
        except Exception as e:
            print(f"❌ Error initializing Google AI client: {e}")
            self.google_client = None
    
    def _setup_providers(self):
        """Setup provider configuration dictionary."""
        self.providers = {
            'openrouter': {
                'client': self.openrouter_client,
                'api_key': self.openrouter_api_key,
                'enabled': self.openrouter_client is not None
            },
            'google': {
                'client': self.google_client,
                'api_key': self.google_api_key,
                'enabled': self.google_client is not None
            }
        }
        
        # Show available providers
        enabled_providers = [name for name, config in self.providers.items() if config['enabled']]
        print(f"\n🎯 Available providers: {', '.join(enabled_providers)}")
        
        print("\n🌐 Supported models:")
        print("   OpenRouter: 'anthropic/claude-3.5-sonnet', 'meta-llama/llama-3.1-8b-instruct', etc.")
        print("   Google AI: 'gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-1.0-pro', etc.")
        print("📋 Visit https://openrouter.ai/models for OpenRouter model list")
    
    def get_providers(self):
        """Get provider configuration."""
        return self.providers
    
    def is_provider_enabled(self, provider_name: str) -> bool:
        """Check if a provider is enabled."""
        return self.providers.get(provider_name, {}).get('enabled', False)

# Global configuration instance
config = Config()

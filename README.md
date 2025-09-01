# LLM Migration Evaluation Tool

This notebook implements a tool for testing open-source Large Language Models' capability in migrating legacy PHP code (WordPress 4.3) to modern PHP 8.3 standards.

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/afridi044/LLM_evaluation.git
cd LLM_evaluation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file in the project root:

```bash
# Copy the example and add your key
cp .env.example .env
```

Edit the `.env` file and add your OpenRouter API key:

```
OPENROUTER_API_KEY=your_actual_api_key_here
```

### 4. Run the Notebook

Open `llm_migration_evaluation.ipynb` in Jupyter Lab or VS Code.

## 🔐 Security Setup

### API Key Management

**NEVER commit your API keys to version control!**

✅ **Secure approach:**
- Store API keys in `.env` file (ignored by git)
- Use environment variables in code
- The `.env` file is automatically excluded from git commits

❌ **Insecure approach:**
- Hardcoding API keys directly in notebooks
- Committing API keys to GitHub
- Sharing API keys in plain text

### Environment Variables

The notebook automatically loads environment variables using `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
```

## 📁 Project Structure

```
LLM_evaluation/
├── .env                    # API keys (DO NOT COMMIT)
├── .env.example           # Template for environment variables
├── .gitignore            # Excludes sensitive files
├── requirements.txt      # Python dependencies
├── llm_migration_evaluation.ipynb  # Main notebook
├── model_output/         # Single file responses
├── chunked_model_output/ # Chunked file responses
├── new-version/          # Parsed PHP output
└── selected_100_files/   # Test PHP files
```

## 🌐 Getting an OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai/)
2. Sign up for an account
3. Go to your API Keys section
4. Create a new API key
5. Add it to your `.env` file

## ✨ Features

- **Multi-model support**: Test different LLMs via OpenRouter
- **Chunking support**: Handle large files by splitting into chunks
- **Clean output parsing**: Extract migrated code from model responses
- **Organized storage**: Separate folders for different models and strategies
- **Security-first**: Environment variable based API key management

## 🔧 Usage Examples

```python
# Single file migration
migrate_file('014_module.tag.id3v2.php', 'qwen/qwen3-coder:free', 'basic')

# Quick migration with defaults
quick_migrate('014_module.tag.id3v2.php')

# Batch migration
batch_migrate(['file1.php', 'file2.php'], 'meta-llama/llama-3.1-8b-instruct')

# Parse model outputs
parser.process_all_responses()

# Reconstruct chunked files
reconstructor.reconstruct_all_files()
```

## 🛡️ Security Best Practices

1. **Never commit `.env` files** - They contain sensitive API keys
2. **Use environment variables** - Keep secrets separate from code
3. **Review commits** - Check that no secrets are accidentally included
4. **Rotate keys regularly** - Generate new API keys periodically
5. **Use `.gitignore`** - Prevent sensitive files from being tracked

## 🔄 Git Workflow

```bash
# Check what files will be committed
git status

# Add files (excluding .env automatically)
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push origin main
```

## 🚨 Important Security Notes

- The `.env` file is automatically ignored by git
- Never share your API keys in issues, discussions, or documentation
- If you accidentally commit an API key, rotate it immediately
- Consider using GitHub secrets for CI/CD workflows

## 📊 Model Output Structure

### Single Files
```
model_output/
└── model_name/
    ├── file1.txt
    └── file2.txt
```

### Chunked Files
```
chunked_model_output/
└── model_name/
    └── filename/
        ├── 1.txt
        ├── 2.txt
        └── 3.txt
```

### Parsed Results
```
new-version/
└── model_name/
    ├── file1.php
    └── file2.php
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

**Remember:** Never include API keys in your contributions!

## 📝 License

This project is for research purposes. Please respect the terms of service of the APIs and models used.

## 🆘 Troubleshooting

### Missing API Key Error
```
OPENROUTER_API_KEY not found in environment variables
```
**Solution:** Create a `.env` file with your API key.

### Import Error for dotenv
```
ModuleNotFoundError: No module named 'dotenv'
```
**Solution:** Install python-dotenv: `pip install python-dotenv`

### Git Tracking .env File
If git is tracking your `.env` file:
```bash
git rm --cached .env
git commit -m "Remove .env from tracking"
```

# AI Study Material Generator 📚

An AI-powered application that generates structured learning content based on topics and difficulty levels using Generative AI.

## Features ✨

- 🤖 AI-powered content generation using GPT-2
- 📊 Multiple difficulty levels (Beginner, Intermediate, Advanced)
- 💡 Real-world examples generation
- ❓ Interactive quiz generation
- 📄 PDF and Markdown export
- 🎨 Beautiful Streamlit interface
- 📜 Generation history tracking

## Installation 🛠️

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone or create the project directory:**
```bash
mkdir ai-study-material
cd ai-study-material
```

2. **Create a virtual environment:**
```bash
python -m venv genai_env
```

3. **Activate the virtual environment:**

On Windows:
```bash
genai_env\Scripts\activate
```

On macOS/Linux:
```bash
source genai_env/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Project Structure 📁
```
ai-study-material/
│
├── generation/
│   ├── __init__.py
│   ├── content_generator.py       # Main content generation
│   ├── example_generator.py       # Example generation
│   ├── notes_formatter.py         # PDF/MD formatting
│   └── quiz_generator.py          # Quiz generation
│
├── app/
│   └── streamlit_app.py           # Main Streamlit application
│
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── .gitignore                     # Git ignore rules
```

## Usage 🚀

1. **Start the Streamlit app:**
```bash
streamlit run app/streamlit_app.py
```

2. **Use the application:**
   - Enter a topic in the sidebar
   - Select difficulty level
   - Click "Generate Study Material"
   - View generated content in tabs
   - Export as PDF or Markdown

## Features in Detail 📖

### Content Generation
- Generates structured explanations based on difficulty level
- Uses GPT-2 model with fallback content
- Customized prompts for each difficulty level

### Example Generation
- Provides real-world examples
- Context-appropriate for difficulty level
- Multiple examples per topic

### Quiz Generation
- Automatically creates quiz questions
- Multiple-choice format
- Includes explanations for answers

### Export Options
- **Markdown**: Easy to edit and share
- **PDF**: Professional formatted documents

## Customization 🎨

### Modifying Prompts
Edit `content_generator.py` to customize prompts:
```python
prompts = {
    "Beginner": f"Your custom prompt for {topic}...",
    # Add more customizations
}
```

### Adding Features
- Extend `quiz_generator.py` for more question types
- Modify `notes_formatter.py` for different export formats
- Customize UI in `streamlit_app.py`

## Troubleshooting 🔧

### Model Download Issues
If GPT-2 download fails:
```bash
pip install --upgrade transformers torch
```

### PDF Generation Errors
Install reportlab:
```bash
pip install reportlab
```

### Import Errors
Ensure you're in the project root and virtual environment is activated:
```bash
cd ai-study-material
source genai_env/bin/activate  # or genai_env\Scripts\activate on Windows
```

## Assignment Tasks ✅

- [x] Add quiz generation
- [x] Export notes as PDF
- [x] Improve prompt templates
- [ ] Add more export formats
- [ ] Implement user feedback system

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License 📄

This project is created for educational purposes as part of an internship project.

## Support 💬

For issues and questions:
- Check the troubleshooting section
- Review code comments
- Contact project supervisor

## Acknowledgments 🙏

- Hugging Face for Transformers library
- Streamlit for the amazing UI framework
- OpenAI for GPT-2 model

---
**Built with ❤️ using Python, Streamlit, and AI**
```

### 9. **.gitignore**
```
# Virtual Environment
genai_env/
venv/
env/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Distribution / packaging
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyTorch
*.pth
*.pt

# Streamlit
.streamlit/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Generated files
*.pdf
*.md
!README.md

In last after averything done ,run the below commands in terminal 

# Create virtual environment
python3 -m venv genai_env

# Activate virtual environment
source genai_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
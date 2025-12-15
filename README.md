# Clerk AI Chat

An AI-powered tool that creates a professional email based on incoming email and user's simple summary.
<img width="953" height="611" alt="image" src="https://github.com/user-attachments/assets/1a0fdb7c-beca-4a09-85c0-c10334241f87" />


## Features

- **AI-Powered Email Generation**: Create professional emails from simple summaries
- **Multiple Tones**: Choose from Professional, Friendly, Formal, or Casual tones
- **Web Interface**: Simple and responsive web application
- **Command Line Tools**: Multiple CLI tools for different use cases
- **Comprehensive Testing**: Full test suite with agent testing

## Project Structure

```bash
Clerk-AI-Chat/
├── .github/worklows        # CI
├── clerk-ai-chat/
    ├── templates
      └── index.html        # HTML templates
    ├── init.py
    ├── agent.py            # AI Agents
    └── web_app.py          # Flask Web Application
├── tests/
    ├── init.py
    └── test_agent.py       # pytest
├── app.py                  # main module
├── pytest.ini
├── README.md
└── requirements.txt        # Python dependencies
```

## Installation

### 1. Clone the Project
```bash
git clone https://github.com/aklimchu/Clerk-AI-Chat.git
cd Clerk-AI-Chat
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```bash
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

## Web Application

### Start the Web Server
```bash
python app.py
```

### Access the Web Interface
1. Open your browser
2. Go to `http://localhost:5000`
3. Fill out the form and generate emails!

### Web Interface Features
- **Simple Form**: Just describe what you want the email to say
- **Tone Selection**: Choose from 4 different tones
- **Real-time Generation**: See results instantly
- **Copy to Clipboard**: Easy copying of generated emails
- **Responsive Design**: Works on desktop and mobile
- **Error Handling**: Clear error messages and validation

## Command Line Tools

### Automated tests
```bash
pytest tests/test_agent.py
```

## Configuration

### Available Tones
- **Professional**: Standard business communication
- **Friendly**: Warm but professional
- **Formal**: Very formal, traditional business style
- **Casual**: Relaxed but appropriate for business

## Troubleshooting

### Common Issues

1. **"OpenAI API key not found"**
   - Make sure you have a `.env` file with `OPENAI_API_KEY=your_key`
   - Check that the `.env` file is in the project root

2. **"Model not found" error**
   - The app uses `gpt-4-turbo` by default
   - You can change it to `gpt-3.5-turbo` in `email_agent.py` if needed

3. **"Insufficient quota" error**
   - Check your OpenAI API billing and usage limits
   - Make sure you have credits available

### Getting Help
- Check the error messages in the web interface
- Use the health check endpoint: `http://localhost:5000/health`

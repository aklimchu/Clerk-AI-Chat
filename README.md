# Clerk AI Chat

An AI-powered tool that creates a professional email based on incoming email and user's simple summary.

## Features

- **AI-Powered Email Generation**: Create professional emails from simple summaries
- **Multiple Tones**: Choose from Professional, Friendly, Formal, or Casual tones
- **Web Interface**: Beautiful, responsive web application
- **Command Line Tools**: Multiple CLI tools for different use cases
- **Comprehensive Testing**: Full test suite with agent testing

## Project Structure

```
to be added
```

## Installation

### 1. Clone or Download the Project
```bash
cd /path/to/Clerk-AI-Chat
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
- **Optional Fields**: Add sender details, company info, recipient context
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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- OpenAI for providing the GPT API
- Flask for the web framework
- The Python community for excellent libraries

---

**Happy Email Writing!**

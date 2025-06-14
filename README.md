# 🎨 Mandala Generator

A beautiful web app that generates black and white mandala art using AI, inspired by a single word.

## Features

- 🎯 Simple one-word inspiration input
- 🤖 AI-powered mandala generation using OpenAI's DALL-E 3
- 📱 Clean, responsive web interface
- 📥 Download high-quality JPEG images (1024x1024)
- 🔒 Secure API key handling (not stored)

## How to Use

1. Enter your OpenAI API key in the sidebar
2. Type a single word for inspiration (e.g., "peace", "harmony", "nature")
3. Click "Generate Mandala" 
4. Download your unique mandala artwork

## Live Demo

🚀 [Try the app online](your-zap-dev-url-here)

## Local Development

### Prerequisites
- Python 3.8+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/mandala-generator.git
cd mandala-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

## Deployment

This app is designed to work perfectly with:
- ✅ Zap.dev
- ✅ Streamlit Cloud
- ✅ Heroku
- ✅ Railway
- ✅ Any Python hosting platform

## API Key Security

⚠️ **Important**: Never commit your API key to Git. This app asks users to enter their API key securely through the interface.

## Tech Stack

- **Frontend**: Streamlit
- **AI**: OpenAI DALL-E 3
- **Image Processing**: Pillow
- **Language**: Python 3.8+

## Contributing

Feel free to fork this project and submit pull requests!

## License

MIT License - feel free to use this for your own projects!

---

Made with ❤️ using Streamlit and OpenAI DALL-E
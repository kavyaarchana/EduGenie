# EduGenie - AI Powered Learning Assistant

## Overview

EduGenie is a lightweight AI-powered educational assistant designed to simplify and enhance the learning experience using Generative AI. It helps students, self-learners, and educators by providing intelligent educational support.

## Features

- Intelligent Question Answering
- Simplified Concept Explanation
- AI-Powered Quiz Generation
- Educational Text Summarization
- Personalized Learning Path Recommendation

## Technologies Used

- Python
- FastAPI
- HTML
- CSS
- Google Gemini API
- SQLAlchemy
- SQLite
- Jinja2

## Project Structure

```
EduGenie/
│
├── app/
├── static/
├── templates/
├── venv/
├── .env
├── requirements.txt
├── README.md
└── edugenie.db
```

## Installation

1. Clone the repository.
2. Create a virtual environment.

```
python -m venv venv
```

3. Activate the virtual environment.

Windows PowerShell:

```
.\venv\Scripts\Activate.ps1
```

4. Install dependencies.

```
pip install -r requirements.txt
```

5. Add your Gemini API Key in the `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

6. Run the project.

```
uvicorn app.main:app --reload
```

7. Open your browser.

```
http://127.0.0.1:8000
```

## Future Enhancements

- Student Progress Tracking
- Voice-based Learning
- Multilingual Support
- LMS Integration
- Mobile Application Support

## Author

Kavya Nallamilli
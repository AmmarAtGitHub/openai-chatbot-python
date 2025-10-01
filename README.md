# openai-chatbot-python

This is my attempt to build a chatbot in Python using the OpenAI API. I will keep the code clean and modular. This chatbot marks the beginning of my exploration into AI development. It’s a learning project, but I plan to expand it and make it more useful as I grow my skills.
---

## 🚀 Project Status
- [x] Set up virtual environment  
- [x] Installed dependencies (`openai`, `python-dotenv`, `tenacity`)  
- [ ] First working chatbot CLI with conversation history  
- [ ] Improve error handling and retry logic  
- [ ] Add a simple web or GUI interface (e.g., Streamlit)  
- [ ] Explore RAG (retrieval-augmented generation) later  

---

## 📂 Project Structure
```
chatbot_openai/
│
├── chatbot/
│ ├── config.py # loads API key and settings
│ ├── client.py # wrapper around OpenAI client
│ ├── storage.py # save conversation logs
│ └── cli.py # command line chatbot
│
├── logs/ # saved conversations
├── tests/ # future unit tests
├── requirements.txt
├── README.md
└── .gitignore
```
---

## ⚙️ Setup Instructions
1. Clone the repo:
   ```bash
   git clone  https://github.com/AmmarAtGitHub/openai-chatbot-python.git
   cd openai-chatbot-python


Create and activate a virtual environment (Windows PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1


Install dependencies:

pip install -r requirements.txt


Create a .env file in the project root and add your key:

OPENAI_API_KEY=sk-xxxxxxx

💻 Usage

Run the chatbot in the terminal:

python -c "from chatbot.cli import start_chatbot; start_chatbot()"


Available commands in the chatbot:

/exit → quit

/save → save conversation to logs

/persona <text> → change bot persona

/history → show conversation so far

/clear → clear messages (keep persona)

📝 Notes

This project is part of my learning path towards becoming an AI engineer.

I started simple but I want to add more features and make it non-trivial over time.

Feedback and suggestions are welcome.

📌 Roadmap

 Add unit tests and GitHub Actions for CI

 Implement a Streamlit-based UI

 Support multiple personas in one session

 Add retrieval (RAG) using vector DB

 Deploy a demo (maybe with Docker)
 
 
 
 
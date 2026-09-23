# 🤖 Ollama Streamlit Chatbot

A simple AI chatbot built using **Python, Ollama, and Streamlit**.

## 🚀 Features

* Chat with an AI locally
* Uses Ollama for local AI responses
* Simple Streamlit web interface
* Easy to run and modify
* No API key required

## 🛠️ Technologies Used

* Python
* Streamlit
* Ollama
* Gemma 3:1B

## 📁 Project Structure

```text
ollama_chat_bot/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd ollama_chat_bot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Make sure Ollama is installed and running on your computer.

Check the installed models:

```bash
ollama list
```

Make sure the `gemma3:1b` model is available.

If needed:

```bash
ollama pull gemma3:1b
```

### 5. Run the chatbot

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 Example

```text
User: What is Python?

Bot: Python is a programming language that is easy to learn...
```

## 👩‍💻 Author

**B. Mrudula**

BTech CSE Student

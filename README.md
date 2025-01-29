# DeepMate - Streamlit Chatbot

## 📌 Overview

DeepMate is an interactive chatbot application built using Streamlit and LangChain. It allows users to have natural language conversations, leveraging an AI agent to generate responses dynamically.

---

## 📂 Project Structure

```
/project_root
│── app.py             # Main Streamlit application
│── prompts.py         # Prompt configuration for the chatbot
│── requirements.txt   # Dependencies list
│── .env               # Environment variables
│── README.md          # Documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 3️⃣ Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 4️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the root directory and add:

```ini
GOOGLE_API_KEY="your api key"
```

### 6️⃣ Run the Application

```sh
streamlit run app.py
```

The app will be available at:
📍 `http://localhost:8501`

---

## 🚀 Features

- ✅ Real-time chatbot interaction
- ✅ Conversation history management
- ✅ AI-powered responses using LangChain
- ✅ Configurable backend API URL
- ✅ Streamlit-based UI for a seamless user experience

---

## 🛠️ Dependencies

- Streamlit
- LangChain
- Python-Dotenv

To install all dependencies:

```sh
pip install -r requirements.txt
```

---

## 🔹 Future Enhancements

✅ Add memory persistence for long conversations  
✅ Implement different chatbot personas  
✅ Enhance UI with additional styling options

---

## 📄 License

This project is licensed under the MIT License.

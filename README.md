# 🎯 AI Interview Question Generator

A smart AI-powered web app that generates **custom interview questions** based on the content of a candidate's **resume (PDF)**. Built with **Streamlit**, powered by **Google Gemini 1.5 Flash**, and designed to assist HR professionals and candidates in preparing for job interviews.

---

## 📌 Features

- 🔍 Extracts text from uploaded **PDF resume**
- 🧠 Uses **Gemini LLM** to analyze skills, experience, and domain
- 📋 Generates **15 personalized interview questions**
  - Mix of technical + behavioral questions
- 💾 Option to **download** the questions as a `.txt` file
- 🖥️ Clean, interactive UI using **Streamlit**

---

## 🧠 Tech Stack

| Layer         | Technology             |
|---------------|------------------------|
| Frontend UI   | Streamlit              |
| Backend Logic | Python, Google Gemini  |
| PDF Parsing   | PyPDF                  |
| LLM API       | Gemini 1.5 Flash (via `google-generativeai`) |
| Secrets Mgmt  | python-dotenv + `.env` |

---

## 📁 Project Structure

ai-interview-generator/
│
├── app.py # Main Streamlit app
├── .env # Contains your Gemini API key (DO NOT COMMIT)
├── requirements.txt # All required Python packages
├── README.md # This documentation
└── .gitignore # Files/folders to ignore (like .env, pycache)


---

## 🔧 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-interview-question-generator.git
cd ai-interview-question-generator

2. Install Dependencies

pip install -r requirements.txt


3. Set Your Gemini API Key
Create a file named .env in the root folder and add:

GOOGLE_API_KEY=your_gemini_api_key_here


4. Run the App

streamlit run app.py



 Example Output

1. Can you explain your role in the e-commerce backend API project?
2. How have you used Python for data analysis?
3. Tell me about a time when you faced a challenge during teamwork.



🧑‍💼 Use Cases
Mock interview preparation

Resume-based interview question generation

HR screening automation

AI-powered hiring assistant

Deployment Link
https://interviewmate-ai.streamlit.app/

📄 Author
Suraj Kumar
AI/ML Enthusiast | Final Year B.Tech (CSE AIML)


⚠️ License
This project is for educational/demo use only.
All API usage must comply with Google's Terms of Use.

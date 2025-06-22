import streamlit as st
import os
from dotenv import load_dotenv
import pypdf
import google.generativeai as genai

#  Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from uploaded PDF
def extract_text_from_pdf(file):
    reader = pypdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

#Gemini prompt + response
def generate_interview_questions(resume_text):
    prompt = f"""
You are an AI assistant that generates interview questions based on resume content.

Resume:
{resume_text}

Your Task:
Generate 15 relevant interview questions (mix of technical and behavioral) based on the candidate's resume. 
If the resume lacks detail, generate standard software developer interview questions.
"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="AI Interview Mate", layout="centered")
st.title(" AI Interview Mate")
st.write("Upload your resume (PDF) and generate customized interview questions.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

    try:
        resume_text = extract_text_from_pdf(uploaded_file)
    except Exception as e:
        st.error(f"Failed to read resume: {e}")
        resume_text = ""

    if st.button("Generate Questions") and resume_text:
        with st.spinner("Generating smart interview questions..."):
            result = generate_interview_questions(resume_text)
            st.markdown("###  AI-Generated Interview Questions:")
            st.write(result)
            st.success("Done!")

            #  Add download button
            st.download_button(
                label=" Download Questions as TXT",
                data=result,
                file_name="AI_Interview_Questions.txt",
                mime="text/plain"
            )
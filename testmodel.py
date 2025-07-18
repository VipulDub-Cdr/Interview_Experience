import streamlit as st
import google.generativeai as genai

# ----------------- PROMPTS -----------------
APTITUDE_PROMPT = """
Generate 20 unique aptitude questions. Each question must:
- Be numbered (1-20)
- Have a clear question statement
- Include 4 options (A, B, C, D)
- Indicate the correct answer as: Answer: <Correct Option Letter>
"""

VERBAL_PROMPT = """
Generate 20 unique verbal ability questions. Each question must:
- Be numbered (1-20)
- Be grammar, vocabulary, or comprehension-based
- Include 4 options (A, B, C, D)
- Indicate the correct answer as: Answer: <Correct Option Letter>
"""

DSA_EASY_PROMPT = """
Generate 1 easy-level data structures and algorithms coding question.
- Include problem statement
- Provide sample input and output
"""

DSA_HARD_PROMPT = """
Generate 1 hard-level data structures and algorithms coding question.
- Include problem statement
- Provide sample input and output
"""

INTERVIEW_PROMPT = """
Generate 5 interview questions.
- 2 behavioral (e.g. teamwork, challenge)
- 2 technical (concepts, debugging)
- 1 situational (how to handle a case)
"""

# ----------------- GEMINI CONFIG -----------------
def configure_gemini(api_key):
    genai.configure(api_key=api_key)

def generate_questions(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# ----------------- STREAMLIT APP -----------------
st.set_page_config(page_title="AI Test Generator", layout="wide")
st.title("🧠 AI-Powered Test Platform")
st.markdown("This platform generates a unique test every time using Generative AI.")

api_key = st.sidebar.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    configure_gemini(api_key)

    if st.button("🚀 Generate Test Now"):
        with st.spinner("Generating questions using Gemini AI..."):
            aptitude = generate_questions(APTITUDE_PROMPT)
            verbal = generate_questions(VERBAL_PROMPT)
            dsa_easy = generate_questions(DSA_EASY_PROMPT)
            dsa_hard = generate_questions(DSA_HARD_PROMPT)
            interview = generate_questions(INTERVIEW_PROMPT)

        st.success("✅ Test Generated Successfully!")

        tabs = st.tabs(["📊 Aptitude", "🗣️ Verbal", "💻 DSA", "🧑‍💼 Interview"])

        with tabs[0]:
            st.subheader("Aptitude Questions")
            st.markdown(aptitude)

        with tabs[1]:
            st.subheader("Verbal Ability Questions")
            st.markdown(verbal)

        with tabs[2]:
            st.subheader("DSA Questions")
            st.markdown("### 🟢 Easy Question\n" + dsa_easy)
            st.markdown("### 🔴 Hard Question\n" + dsa_hard)

        with tabs[3]:
            st.subheader("Interview Questions")
            st.markdown(interview)

        st.button("✅ Submit Test")
else:
    st.warning("Please enter your Gemini API key in the sidebar to begin.")


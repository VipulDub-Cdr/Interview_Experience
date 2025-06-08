# AI Interviewer

An interactive AI-powered interviewer built with **Gradio**, **Google Generative AI (Gemini)**, and **gTTS (Text-to-Speech)**.

## Project Overview

This project simulates a real-time interview experience:

- Generates **custom interview questions** based on the user's skills.
- Lets the user **answer questions one by one**.
- Provides **AI-generated feedback** on the interview performance.
- Converts the feedback into **speech audio** for an interactive experience.

## Tech Stack

- **Python**
- **Gradio** — Web UI framework
- **Google Generative AI (Gemini 1.5 Flash)** — For question generation & feedback
- **gTTS** — To convert feedback text into speech
- **tempfile** — For managing temporary audio files

## How It Works

1. User enters a list of their skills.
2. The AI generates 5 interview questions tailored to those skills.
3. User answers each question through the interface.
4. After all questions, AI analyzes the interview and provides feedback:
    - Highlights mistakes.
    - Summarizes performance.
    - Outputs feedback as both text and audio.

## User Interface 

![alt text](image.png)

## Use Cases

- Interview practice for **students** and **job seekers**.
- Automated **mock interview coach**.
- Language and communication skills practice.
- HR training tool for **automated interview preparation**.


## Running the Project

### Prerequisites

- Python 3.8+
- Google Generative AI API key

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/ai-interviewer.git
    cd ai-interviewer
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your Google Generative AI API key in your script:
    ```python
    genai.configure(api_key="YOUR_API_KEY")
    ```

4. Run the app:
    ```bash
    python app.py
    ```

5. Access the Gradio interface in your browser (usually at `http://127.0.0.1:7860`).

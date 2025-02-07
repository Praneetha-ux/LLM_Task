# import streamlit as st
# import os
# import replicate
# import whisper
# from dotenv import load_dotenv
# from save_audio_files import save_uploaded_audio

# # Load environment variables
# load_dotenv()
# REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# # Function to call Replicate API
# def call_replicate(prompt, model="meta/llama-2-7b-chat"):
#     try:
#         output = replicate.run(
#             model,
#             input={"prompt": prompt, "max_tokens": 300}
#         )
#         return "".join(output)  # Convert list to string
#     except Exception as e:
#         return f"❌ Error calling Replicate API: {e}"

# # Function for Speech Recognition using Whisper
# def transcribe_audio(audio_file):
#     try:
#         print("Audio file path:", audio_file)
#         save_uploaded_audio(audio_file)
#         path1 = "uploaded_audios/"
        
#         # Load Whisper model
#         model = whisper.load_model("base")
        
#         # Transcribe audio
#         transcription = model.transcribe(path1 + audio_file.name)
#         return transcription["text"]
#     except Exception as e:
#         return f"❌ Error in transcribing audio: {e}"

# # Sidebar Menu
# st.sidebar.title("🔍 AI-Powered Tools")
# app_selection = st.sidebar.radio("📌 Select a Tool", (
#     "🏳️ Language Detection & Translation",
#     "📧 Email Spam Detection",
#     "📄 Summarization",
#     "😊 Sentiment Analysis",
#     "🔤 Grammar & Spelling Correction",
#     "🎙️ Speech Recognition",
#     "📑 Text Classification"
# ))

# # Main App
# st.title(app_selection)

# # 📌 Language Detection & Translation
# if app_selection == "🏳️ Language Detection & Translation":
#     text = st.text_area("Enter Text")
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Detect Language"):
#             detect_prompt = f"Detect the language of this text: {text}"
#             detected_language = call_replicate(detect_prompt)
#             st.write(f"Detected Language: {detected_language}")

#     with col2:
#         target_language = st.text_input("Enter target language (e.g., French, Spanish, Hindi)")
#         if st.button("Translate"):
#             translate_prompt = f"Translate this text to {target_language}: {text}"
#             st.write(call_replicate(translate_prompt))

# # 📧 Email Spam Detection
# elif app_selection == "📧 Email Spam Detection":
#     email_text = st.text_area("Enter Email Text")
#     if st.button("Analyze"):
#         prompt = f"Classify this email as Spam or Not Spam: {email_text}"
#         result = call_replicate(prompt)
#         st.json({"email_type": result.strip()})

# # 📄 Text Summarization
# elif app_selection == "📄 Summarization":
#     long_text = st.text_area("Enter Long Text (7-8 paragraphs)")
#     if st.button("Summarize"):
#         prompt = f"Summarize the following text with proper headings and formatting: {long_text}"
#         st.write(call_replicate(prompt))

# # 😊 Sentiment Analysis
# elif app_selection == "😊 Sentiment Analysis":
#     review = st.text_area("Enter Review")
#     if st.button("Analyze Sentiment"):
#         prompt = f"Determine if this review is POSITIVE, NEGATIVE, or NEUTRAL: {review}"
#         sentiment = call_replicate(prompt)
#         st.json({"Sentiment": sentiment.strip()})

# # 🔤 Grammar & Spelling Correction
# elif app_selection == "🔤 Grammar & Spelling Correction":
#     incorrect_text = st.text_area("Enter Incorrect Text")
#     if st.button("Correct Grammar"):
#         prompt = f"Correct grammar and spelling mistakes in this text: {incorrect_text}"
#         st.write(call_replicate(prompt))

# # 🎙️ Speech Recognition
# elif app_selection == "🎙️ Speech Recognition":
#     audio_file = st.file_uploader("Upload Audio File", type=["mp3", "mp4", "wav"])
#     if audio_file and st.button("Transcribe"):
#         transcription = transcribe_audio(audio_file)
#         st.write(transcription)
#         st.download_button("Download TXT", transcription, "transcription.txt")

# # 📑 Text Classification
# elif app_selection == "📑 Text Classification":
#     text = st.text_area("Enter Text")
#     if st.button("Classify"):
#         prompt = f"Categorize this text into Technology, Finance, Medical, or Agriculture: {text}"
#         label = call_replicate(prompt)
#         st.json({"Category": label.strip()})

# st.sidebar.write("🚀 Powered by **Replicate LLM** & **Whisper AI**")


import streamlit as st
import os
import replicate
import whisper
from dotenv import load_dotenv
from save_audio_files import save_uploaded_audio
from streamlit_option_menu import option_menu

# Load environment variables
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Function to call Replicate API
def call_replicate(prompt, model="meta/llama-2-7b-chat"):
    try:
        output = replicate.run(
            model,
            input={"prompt": prompt, "max_tokens": 300}
        )
        return "".join(output)  # Convert list to string
    except Exception as e:
        return f"❌ Error calling Replicate API: {e}"

# Function for Speech Recognition using Whisper
def transcribe_audio(audio_file):
    try:
        print("Audio file path:", audio_file)
        save_uploaded_audio(audio_file)
        path1 = "uploaded_audios/"
        
        # Load Whisper model
        model = whisper.load_model("base")
        
        # Transcribe audio
        transcription = model.transcribe(path1 + audio_file.name)
        return transcription["text"]
    except Exception as e:
        return f"❌ Error in transcribing audio: {e}"

# Sidebar Menu using option_menu
with st.sidebar:
    app_selection = option_menu(
        menu_title="🔍 AI-Powered Tools",
        options=[
            "🏳️ Language Detection & Translation",
            "📧 Email Spam Detection",
            "📄 Summarization",
            "😊 Sentiment Analysis",
            "🔤 Grammar & Spelling Correction",
            "🎙️ Speech Recognition",
            "📑 Text Classification"
        ],
        icons=[
            "translate", "envelope", "file-text", "emoji-smile",
            "spellcheck", "mic", "list-task"
        ],
        menu_icon="app-indicator",
        default_index=0
    )

# Main App
st.title(app_selection)

# 📌 Language Detection & Translation
if app_selection == "🏳️ Language Detection & Translation":
    text = st.text_area("Enter Text")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Detect Language"):
            detect_prompt = f"Detect the language of this text: {text}"
            detected_language = call_replicate(detect_prompt)
            st.write(f"Detected Language: {detected_language}")

    with col2:
        target_language = st.text_input("Enter target language (e.g., French, Spanish, Hindi)")
        if st.button("Translate"):
            translate_prompt = f"Translate this text to {target_language}: {text}"
            st.write(call_replicate(translate_prompt))

# 📧 Email Spam Detection
elif app_selection == "📧 Email Spam Detection":
    email_text = st.text_area("Enter Email Text")
    if st.button("Analyze"):
        prompt = f"Classify this email as Spam or Not Spam: {email_text}"
        result = call_replicate(prompt)
        st.json({"email_type": result.strip()})

# 📄 Text Summarization
elif app_selection == "📄 Summarization":
    long_text = st.text_area("Enter Long Text (7-8 paragraphs)")
    if st.button("Summarize"):
        prompt = f"Summarize the following text with proper headings and formatting: {long_text}"
        st.write(call_replicate(prompt))

# 😊 Sentiment Analysis
elif app_selection == "😊 Sentiment Analysis":
    review = st.text_area("Enter Review")
    if st.button("Analyze Sentiment"):
        prompt = f"Determine if this review is POSITIVE, NEGATIVE, or NEUTRAL: {review}"
        sentiment = call_replicate(prompt)
        st.json({"Sentiment": sentiment.strip()})

# 🔤 Grammar & Spelling Correction
elif app_selection == "🔤 Grammar & Spelling Correction":
    incorrect_text = st.text_area("Enter Incorrect Text")
    if st.button("Correct Grammar"):
        prompt = f"Correct grammar and spelling mistakes in this text: {incorrect_text}"
        st.write(call_replicate(prompt))

# 🎙️ Speech Recognition
elif app_selection == "🎙️ Speech Recognition":
    audio_file = st.file_uploader("Upload Audio File", type=["mp3", "mp4", "wav"])
    if audio_file and st.button("Transcribe"):
        transcription = transcribe_audio(audio_file)
        st.write(transcription)
        st.download_button("Download TXT", transcription, "transcription.txt")

# 📑 Text Classification
elif app_selection == "📑 Text Classification":
    text = st.text_area("Enter Text")
    if st.button("Classify"):
        prompt = f"Categorize this text into Technology, Finance, Medical, or Agriculture: {text}"
        label = call_replicate(prompt)
        st.json({"Category": label.strip()})

st.sidebar.write("🚀 Powered by **Replicate LLM** & **Whisper AI**")

# import streamlit as st
# import os
# import replicate
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# # Function to call Replicate API
# def call_replicate(prompt, model="meta/llama-2-7b-chat" ):
#     output = replicate.run(
#         model,
#         input={"prompt": prompt, "max_tokens": 300}
#     )
#     return "".join(output)  # Convert list to string

# # Sidebar for app selection
# st.sidebar.title("AI-Powered Tools")
# app_selection = st.sidebar.radio("Select a Tool", (
#     "Language Detection & Translation", "Email Spam Detection",
#     "Summarization", "Sentiment Analysis", "Grammar & Spelling Correction",
#     "Speech Recognition", "Text Classification", "Data Extraction",
#     "ChatBot Development"))

# # App Implementations
# if app_selection == "Language Detection & Translation":
#     st.title("Language Detection & Translation")
#     task = st.selectbox("Select Task", ["Detection", "Translation"])
#     text = st.text_area("Enter Text")
#     if st.button("Submit"):
#         prompt = f"Detect the language of this text: {text}" if task == "Detection" else f"Translate this text to English: {text}"
#         st.write(call_replicate(prompt))

# elif app_selection == "Email Spam Detection":
#     st.title("Email Spam Detection")
#     email_text = st.text_area("Enter Email Text")
#     if st.button("Analyze"):
#         prompt = f"Classify this email as Spam or Not Spam: {email_text}"
#         st.json({"email_type": call_replicate(prompt)})

# elif app_selection == "Summarization":
#     st.title("Text Summarization")
#     long_text = st.text_area("Enter Long Text (7-8 paragraphs)")
#     if st.button("Summarize"):
#         prompt = f"Summarize the following text with proper headings and formatting: {long_text}"
#         st.write(call_replicate(prompt))

# elif app_selection == "Sentiment Analysis":
#     st.title("Sentiment Analysis")
#     review = st.text_area("Enter Review")
#     if st.button("Analyze Sentiment"):
#         prompt = f"Determine if this review is POSITIVE, NEGATIVE, or NEUTRAL: {review}"
#         st.json({"review": call_replicate(prompt)})

# elif app_selection == "Grammar & Spelling Correction":
#     st.title("Grammar & Spelling Correction")
#     incorrect_text = st.text_area("Enter Incorrect Text")
#     if st.button("Correct Grammar"):
#         prompt = f"Correct grammar and spelling mistakes in this text: {incorrect_text}"
#         st.write(call_replicate(prompt))

# elif app_selection == "Speech Recognition":
#     st.title("Speech Recognition")
#     audio_file = st.file_uploader("Upload Audio File (.mp3)", type=["mp3"])
#     if st.button("Transcribe") and audio_file:
#         st.write("[Placeholder: Transcription will be implemented using Replicate API]")

# elif app_selection == "Text Classification":
#     st.title("Text Classification")
#     text = st.text_area("Enter Text")
#     if st.button("Classify"):
#         prompt = f"Categorize this text into Technology, Finance, Medical, or Agriculture: {text}"
#         st.json({"Label": call_replicate(prompt)})

# elif app_selection == "Data Extraction":
#     st.title("Data Extraction from Invoice PDF")
#     pdf_file = st.file_uploader("Upload Invoice PDF", type=["pdf"])
#     if st.button("Extract Data") and pdf_file:
#         st.write("[Placeholder: PDF extraction logic will be added]")

# elif app_selection == "ChatBot Development":
#     st.title("Invoice-based ChatBot")
#     user_input = st.text_input("Ask a question about the invoices")
#     if st.button("Ask"):
#         prompt = f"Based on invoice data, answer this question: {user_input}"
#         st.write(call_replicate(prompt))

# st.sidebar.write("Powered by Replicate LLM")





# import streamlit as st
# import os
# import replicate
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# # Function to call Replicate API
# def call_replicate(prompt, model="meta/llama-2-7b-chat" ):
#     output = replicate.run(
#         model,
#         input={"prompt": prompt, "max_tokens": 300}
#     )
#     return "".join(output)  # Convert list to string

# # Sidebar for app selection
# st.sidebar.title("AI-Powered Tools")
# app_selection = st.sidebar.radio("Select a Tool", (
#     "Language Detection & Translation", "Email Spam Detection",
#     "Summarization", "Sentiment Analysis", "Grammar & Spelling Correction",
#     "Speech Recognition", "Text Classification", "Data Extraction",
#     "ChatBot Development"))

# # App Implementations
# if app_selection == "Language Detection & Translation":
#     st.title("Language Detection & Translation")
#     text = st.text_area("Enter Text")
#     if st.button("Detect Language"):
#         detect_prompt = f"Detect the language of this text: {text}"
#         detected_language = call_replicate(detect_prompt)
#         st.write(f"Detected Language: {detected_language}")
    
#     if st.button("Translate"):
#         target_language = st.text_input("Enter target language (e.g., French, Spanish,telugu,hindi,urudu,italian etc)")
#         translate_prompt = f"Translate this text to {target_language}: {text}"
#         st.write(call_replicate(translate_prompt))

# elif app_selection == "Email Spam Detection":
#     st.title("Email Spam Detection")
#     email_text = st.text_area("Enter Email Text")
#     if st.button("Analyze"):
#         prompt = f"Classify this email as Spam or Not Spam: {email_text}"
#         result = call_replicate(prompt)
#         st.json({"email_type": result.strip()})

# elif app_selection == "Summarization":
#     st.title("Text Summarization")
#     long_text = st.text_area("Enter Long Text (7-8 paragraphs)")
#     if st.button("Summarize"):
#         prompt = f"Summarize the following text with proper headings and formatting: {long_text}"
#         st.write(call_replicate(prompt))

# elif app_selection == "Sentiment Analysis":
#     st.title("Sentiment Analysis")
#     review = st.text_area("Enter Review")
#     if st.button("Analyze Sentiment"):
#         prompt = f"Determine if this review is POSITIVE, NEGATIVE, or NEUTRAL: {review}"
#         sentiment = call_replicate(prompt)
#         st.json({"review": sentiment.strip()})

# elif app_selection == "Grammar & Spelling Correction":
#     st.title("Grammar & Spelling Correction")
#     incorrect_text = st.text_area("Enter Incorrect Text")
#     if st.button("Correct Grammar"):
#         prompt = f"Correct grammar and spelling mistakes in this text: {incorrect_text}"
#         st.write(call_replicate(prompt))

# elif app_selection == "Speech Recognition":
#     st.title("Speech Recognition")
#     audio_file = st.file_uploader("Upload Audio File", type=["mp3", "mp4", "wav"])
                                  
#     if audio_file and st.button("Transcribe"):
#         st.write("[Placeholder: Transcription will be implemented using Replicate API]")
#         st.download_button("Download TXT", "[Transcribed Text Here]", "transcription.txt")

# elif app_selection == "Text Classification":
#     st.title("Text Classification")
#     text = st.text_area("Enter Text")
#     if st.button("Classify"):
#         prompt = f"Categorize this text into Technology, Finance, Medical, or Agriculture: {text}"
#         label = call_replicate(prompt)
#         st.json({"Label": label.strip()})

# st.sidebar.write("Powered by Replicate LLM")



import streamlit as st
import os
import replicate
import whisper
from dotenv import load_dotenv
from save_audio_files import save_uploaded_audio

# Load environment variables
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Function to call Replicate API
def call_replicate(prompt, model="meta/llama-2-7b-chat" ):
    output = replicate.run(
        model,
        input={"prompt": prompt, "max_tokens": 300}
    )
    return "".join(output)  # Convert list to string

# Function for Speech Recognition using Whisper
def transcribe_audio(audio_file):
    try:
        print("audio file path",audio_file)
        save_uploaded_audio(audio_file)
        path1 = "uploaded_audios/"
        model = whisper.load_model("base")
        transcription = model.transcribe(path1+audio_file.name)
        return transcription["text"]
    except Exception as e:
        print('At transcribe_audio')
        print(e)

# Sidebar for app selection
st.sidebar.title("AI-Powered Tools")
app_selection = st.sidebar.radio("Select a Tool", (
    "Language Detection & Translation", "Email Spam Detection",
    "Summarization", "Sentiment Analysis", "Grammar & Spelling Correction",
    "Speech Recognition", "Text Classification", "Data Extraction",
    "ChatBot Development"))

# App Implementations
if app_selection == "Language Detection & Translation":
    st.title("Language Detection & Translation")
    text = st.text_area("Enter Text")
    if st.button("Detect Language"):
        detect_prompt = f"Detect the language of this text: {text}"
        detected_language = call_replicate(detect_prompt)
        st.write(f"Detected Language: {detected_language}")
    
    if st.button("Translate"):
        target_language = st.text_input("Enter target language (e.g., French, Spanish, Telugu, Hindi, Urdu, Italian, etc.)")
        translate_prompt = f"Translate this text to {target_language}: {text}"
        st.write(call_replicate(translate_prompt))

elif app_selection == "Email Spam Detection":
    st.title("Email Spam Detection")
    email_text = st.text_area("Enter Email Text")
    if st.button("Analyze"):
        prompt = f"Classify this email as Spam or Not Spam: {email_text}"
        result = call_replicate(prompt)
        st.json({"email_type": result.strip()})

elif app_selection == "Summarization":
    st.title("Text Summarization")
    long_text = st.text_area("Enter Long Text (7-8 paragraphs)")
    if st.button("Summarize"):
        prompt = f"Summarize the following text with proper headings and formatting: {long_text}"
        st.write(call_replicate(prompt))

elif app_selection == "Sentiment Analysis":
    st.title("Sentiment Analysis")
    review = st.text_area("Enter Review")
    if st.button("Analyze Sentiment"):
        prompt = f"Determine if this review is POSITIVE, NEGATIVE, or NEUTRAL: {review}"
        sentiment = call_replicate(prompt)
        st.json({"review": sentiment.strip()})

elif app_selection == "Grammar & Spelling Correction":
    st.title("Grammar & Spelling Correction")
    incorrect_text = st.text_area("Enter Incorrect Text")
    if st.button("Correct Grammar"):
        prompt = f"Correct grammar and spelling mistakes in this text: {incorrect_text}"
        st.write(call_replicate(prompt))

elif app_selection == "Speech Recognition":
    st.title("Speech Recognition")
    audio_file = st.file_uploader("Upload Audio File", type=["mp3", "mp4", "wav"])
    
    if audio_file and st.button("Transcribe"):
        transcription = transcribe_audio(audio_file)
        st.write(transcription)
        st.download_button("Download TXT", transcription, "transcription.txt")

elif app_selection == "Text Classification":
    st.title("Text Classification")
    text = st.text_area("Enter Text")
    if st.button("Classify"):
        prompt = f"Categorize this text into Technology, Finance, Medical, or Agriculture: {text}"
        label = call_replicate(prompt)
        st.json({"Label": label.strip()})

st.sidebar.write("Powered by Replicate LLM & Whisper AI")

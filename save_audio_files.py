# import os
# import streamlit as st

# # Define the folder where audio files will be saved
# UPLOAD_FOLDER = "uploaded_audios"

# # Ensure the folder exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# def save_uploaded_audio(audio_file):
#     """Save uploaded audio file to a specific folder and return file path"""
#     if audio_file is not None:
#         file_path = os.path.join(UPLOAD_FOLDER, audio_file.name)
        
#         # Save the file
#         with open(file_path, "wb") as f:
#             f.write(audio_file.read())
        
#         st.success(f"File saved successfully: {file_path}")
#         return file_path  # Return the saved file path
#     return None


import streamlit as st
import os
import replicate
import whisper
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Define the folder where audio files will be saved
UPLOAD_FOLDER = "uploaded_audios"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to save uploaded audio file
def save_uploaded_audio(audio_file):
    try:
        if audio_file is not None:
            file_path = os.path.join(UPLOAD_FOLDER, audio_file.name)
            with open(file_path, "wb") as f:
                f.write(audio_file.read())
            return file_path
        return None
    except Exception as e:
        print('At save_uploaded_audio')
        print(e)

# Function to call Replicate API
def call_replicate(prompt, model="meta/llama-2-7b-chat"):
    output = replicate.run(model, input={"prompt": prompt, "max_tokens": 300})
    return "".join(output)

# Function for Speech Recognition using Whisper
def transcribe_audio(audio_file):
    if audio_file is not None:
        saved_path = save_uploaded_audio(audio_file)  # Save the file first
        if saved_path and os.path.exists(saved_path):  # Ensure file exists
            model = whisper.load_model("base")
            transcription = model.transcribe(saved_path)
            return transcription["text"]
        else:
            return "Error: Audio file could not be saved or found!"
    return "Error: No audio file provided!"

# Streamlit UI for Speech Recognition
st.title("Speech Recognition")
audio_file = st.file_uploader("Upload Audio File", type=["mp3", "mp4", "wav"])

if audio_file and st.button("Transcribe"):
    transcription = transcribe_audio(audio_file)
    st.write(transcription)
    st.download_button("Download TXT", transcription, "transcription.txt")

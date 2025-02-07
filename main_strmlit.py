import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Main app navigation
st.set_page_config(page_title="AI Multipage App", layout="wide")
st.title("AI Multipage Streamlit App")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", (
    "Language Translation", 
    "Email Spam Detection", 
    "Summarisation", 
    "Sentiment Analysis", 
    "Grammar/Spelling Correction", 
    "Speech Recognition", 
    "Text Classification"
))

if page == "Language Translation":
    from pages_tmp.Language_Translation_1 import app as language_translation_app
    language_translation_app(REPLICATE_API_TOKEN)

elif page == "Email Spam Detection":
    from pages_tmp.Email_Spam_Detection_2 import app as email_spam_detection_app
    email_spam_detection_app(REPLICATE_API_TOKEN)

elif page == "Summarisation":
    from pages_tmp.Summarisation_3 import app as summarisation_app
    summarisation_app(REPLICATE_API_TOKEN)

elif page == "Sentiment Analysis":
    from pages_tmp.Sentiment_Analysis_4 import app as sentiment_analysis_app
    sentiment_analysis_app(REPLICATE_API_TOKEN)

elif page == "Grammar/Spelling Correction":
    from pages_tmp.Grammar_Spelling_Correction_5 import app as grammar_spelling_correction_app
    grammar_spelling_correction_app(REPLICATE_API_TOKEN)

elif page == "Speech Recognition":
    from pages_tmp.Speech_Recognition_6 import app as speech_recognition_app
    speech_recognition_app(REPLICATE_API_TOKEN)

elif page == "Text Classification":
    from pages_tmp.Text_Classification_7 import app as text_classification_app
    text_classification_app(REPLICATE_API_TOKEN)

# pages/6_Speech_Recognition.py
import streamlit as st
import replicate

def app(REPLICATE_API_TOKEN):
    st.header("Speech Recognition")

    uploaded_file = st.file_uploader("Upload an audio or video file", type=["mp3", "wav", "mp4"])

    if uploaded_file is not None:
        if st.button("Transcribe"):
            with st.spinner("Transcribing audio..."):
                prompt = (
                    f"You are an advanced speech recognition model. Transcribe the audio from the uploaded file accurately. "
                    f"Ensure correct punctuation, grammar, and clear formatting.\n\n"
                    f"Audio File: {uploaded_file.name}"
                )

                output = replicate.run(
                    "meta/meta-llama-3-8b-instruct", 
                    input={"audio": uploaded_file},
                    api_token=REPLICATE_API_TOKEN
                )
                result = " ".join(output) if isinstance(output, list) else output
                st.success("Transcription Complete")
                st.subheader("Transcribed Text:")
                st.write(result)

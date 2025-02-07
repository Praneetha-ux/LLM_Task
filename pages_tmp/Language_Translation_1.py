import streamlit as st
import replicate

def app(REPLICATE_API_TOKEN):
    st.header("Language Translation")

    text_to_translate = st.text_area("Enter text to translate:", "")
    source_language = st.selectbox("Select source language:", ["English", "Telugu", "Hindi", "Spanish", "French"])
    target_language = st.selectbox("Select target language:", ["Telugu", "English", "Hindi", "Spanish", "French"])

    if st.button("Translate") and text_to_translate:
        with st.spinner("Translating..."):
            prompt = (
                f"You are an expert translator. Your job is to translate accurately while preserving the original meaning. "
                f"Translate the following text from {source_language} to {target_language}. "
                f"Ensure cultural context and idiomatic expressions are handled correctly.\n\n"
                f"Text: {text_to_translate}"
            )

            output = replicate.run(
                "meta/meta-llama-3-8b-instruct", 
                input={"prompt": prompt},
                api_token=REPLICATE_API_TOKEN
            )
            result = " ".join(output) if isinstance(output, list) else output
            st.success("Translation Complete")
            st.subheader("Translated Text:")
            st.write(result)

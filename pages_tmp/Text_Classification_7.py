# pages/7_Text_Classification.py
import streamlit as st
import replicate

def app(REPLICATE_API_TOKEN):
    st.header("Text Classification")

    text_to_classify = st.text_area("Enter text to classify:", "")

    if st.button("Classify") and text_to_classify:
        with st.spinner("Classifying..."):
            prompt = (
                f"You are an expert in text classification. Classify the following text into one of these categories: Medical, Education, Real Estate, Engineering, Software, Hardware, etc. "
                f"Provide the category and a brief explanation for your classification.\n\n"
                f"Text: {text_to_classify}"
            )

            output = replicate.run(
                "meta/meta-llama-3-8b-instruct", 
                input={"prompt": prompt},
                api_token=REPLICATE_API_TOKEN
            )
            result = " ".join(output) if isinstance(output, list) else output
            st.success("Classification Complete")
            st.subheader("Classification Result:")
            st.write(result)
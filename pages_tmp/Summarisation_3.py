import streamlit as st
import replicate

def app(REPLICATE_API_TOKEN):
    st.header("Text Summarisation")

    text_to_summarize = st.text_area("Enter text to summarize:", "")

    if st.button("Summarize") and text_to_summarize:
        with st.spinner("Summarizing..."):
            prompt = (
                f"You are an expert in text summarization. Summarize the following text concisely while preserving key points, main ideas, and essential information. "
                f"Ensure the summary is clear and coherent, reducing unnecessary details.\n\n"
                f"Original Text: {text_to_summarize}"
            )

            output = replicate.run(
                "meta/meta-llama-3-8b-instruct",  
                input={"prompt": prompt},
                api_token=REPLICATE_API_TOKEN
            )
            result = " ".join(output) if isinstance(output, list) else output
            st.success("Summarization Complete")
            st.subheader("Summary:")
            st.write(result)

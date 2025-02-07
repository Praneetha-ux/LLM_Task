# pages/5_Grammar_Spelling_Correction.py
import streamlit as st
import replicate

def app(REPLICATE_API_TOKEN):
    st.header("Grammar/Spelling Correction")

    text_to_correct = st.text_area("Enter text for grammar/spelling check:", "")

    if st.button("Correct") and text_to_correct:
        with st.spinner("Checking for errors..."):
            prompt = (
                f"You are a professional editor. Review the following text for grammar and spelling mistakes. "
                f"Identify the errors, suggest corrections, and provide the corrected version of the text.\n\n"
                f"Text: {text_to_correct}"
            )

            output = replicate.run(
                "meta/meta-llama-3-8b-instruct",  
                input={"prompt": prompt},
                api_token=REPLICATE_API_TOKEN
            )
            result = " ".join(output) if isinstance(output, list) else output
            st.success("Correction Complete")
            st.subheader("Corrected Text:")
            st.write(result)

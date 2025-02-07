import streamlit as st
import replicate

def app(REPLICATE_API_TOKEN):
    st.header("Email Spam Detection")

    email_content = st.text_area("Enter email content:", "")

    if st.button("Detect Spam") and email_content:
        with st.spinner("Analyzing..."):
            prompt = (
                f"You are a cybersecurity expert specializing in email spam detection. Analyze the following email content carefully. "
                f"Identify whether it is SPAM or NOT SPAM. Provide a clear and concise explanation for your classification.\n\n"
                f"Email Content: {email_content}"
            )

            output = replicate.run(
                "meta/meta-llama-3-8b-instruct", 
                input={"prompt": prompt},
                api_token=REPLICATE_API_TOKEN
            )
            result = " ".join(output) if isinstance(output, list) else output
            st.success("Detection Complete")
            st.subheader("Spam Detection Result:")
            st.write(result)

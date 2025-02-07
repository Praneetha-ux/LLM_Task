# pages/4_Sentiment_Analysis.py
import streamlit as st
import replicate

def app(REPLICATE_API_TOKEN):
    st.header("Sentiment Analysis (Film/Food Reviews)")

    review_text = st.text_area("Enter review text:", "")

    if st.button("Analyze Sentiment") and review_text:
        with st.spinner("Analyzing..."):
            prompt = (
                f"You are an expert in sentiment analysis. Analyze the following review and determine if it reflects a Positive, Negative, or Neutral sentiment. "
                f"Explain briefly why it falls into that category.\n\n"
                f"Review: {review_text}"
            )

            output = replicate.run(
                "meta/meta-llama-3-8b-instruct",  
                input={"prompt": prompt},
                api_token=REPLICATE_API_TOKEN
            )
            result = " ".join(output) if isinstance(output, list) else output
            st.success("Sentiment Analysis Complete")
            st.subheader("Sentiment Result:")
            st.write(result)

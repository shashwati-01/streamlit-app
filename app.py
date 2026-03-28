import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini Summarizer", page_icon="📝")
st.title("📝 Text Summarizer (Gemini)")

# Use a sidebar for the API key to keep the UI clean
with st.sidebar:
    api_key = st.text_input("Enter Gemini API Key", type="password")
    st.info("Get your key at [Google AI Studio](https://aistudio.google.com/)")

text = st.text_area("Enter text to summarize", height=250)

if st.button("Summarize"):
    if not api_key:
        st.error("Please enter your API key in the sidebar.")
    elif not text:
        st.warning("Please enter some text first.")
    else:
        try:
            # 1. Configure the API
            genai.configure(api_key=api_key)

            # 2. UPDATED MODEL NAME: Use gemini-2.5-flash 
            # (Gemini 1.5 was retired in late 2025)
            model = genai.GenerativeModel(model_name="gemini-2.5-flash")

            with st.spinner("Generating summary..."):
                response = model.generate_content(f"Summarize this text concisely: {text}")
                
                if response.text:
                    st.subheader("Summary:")
                    st.success("Success!")
                    st.write(response.text)
                else:
                    st.error("Model returned an empty response. Try a different text.")

        except Exception as e:
            # If 2.5 fails, it might be a library version issue
            st.error(f"Error: {e}")
            st.info("Check if your google-generativeai library is updated: 'pip install -U google-generativeai'")
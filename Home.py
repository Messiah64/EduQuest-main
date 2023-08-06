import streamlit as st
import streamlit.components.v1 as components


<<<<<<< HEAD
OpenAI_Key = st.secrets["OpenAI_Key"]
=======
OpenAI_Key = "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"
>>>>>>> 0bb586c03e8dc85950b20913fab8769964a80e36

st.set_page_config(
    page_title="EduQuest",
    page_icon="https://cdn-icons-png.flaticon.com/512/2617/2617909.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.image("images/eduquest-logo2.png", width= 400)

st.markdown("""

            #### Welcome to EduQuest - a 5 in 1 education multitool for students.

- ##Text Summarizer** 📚🔍: Generates brief summaries from PDFs, articles, or input text, saving time on reading.
            
- **Video Summarizer** 🎥📝: Provides key points from YouTube videos via URL, eliminating the need to watch the whole video.
            
- **Semantic Search** 🔍📄: Uploading text enables quick keyword-based research for finding relevant information.
            
- **Notes and Questions** 📝❓: Generates well-structured notes and questions on input topics, aiding learning.
            
- **Chatbot** 🤖💬: Interact naturally with the Chatbot using files like .CSV or .TXT for quick answers.
""")

            

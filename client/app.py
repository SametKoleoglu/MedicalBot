import streamlit as st
from components.upload import render_uploader
from components.chatUI import render_chat
from components.history_download import render_history_download


st.set_page_config(
    page_title="Medical Assistant with RAG",
    page_icon=":robot_face:",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("🏥 Medical Assistant with RAG")

render_uploader()
render_chat()
render_history_download()

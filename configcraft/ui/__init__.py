# configcraft/ui/__init__.py
import streamlit as st
from datetime import datetime
from configcraft.model import get_ai_response

# Custom styles for the chat interface
def load_css():
    st.markdown("""
        <style>
            .chat-box {
                border: 2px solid #8CA1A5;
                border-radius: 5px;
                padding: 5px;
                margin: 10px 0;
            }
            .message {
                position: relative;
                margin: 5px 0;
                padding: 10px;
                background-color: #f0f2f6;
                border-radius: 10px;
                border: 1px solid #dae0e6;
            }
            .user-message {
                text-align: right;
            }
            .bot-message {
                text-align: left;
            }
        </style>
    """, unsafe_allow_html=True)

# Main application function
def run_app():
    # Load the custom CSS
    load_css()

    # Initialize session state for chat history if not already set
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Title of the app
    st.title('ConfigCraft.ai')

    # Display chat history first
    if st.session_state.chat_history:
        for chat in st.session_state.chat_history:
            if chat['type'] == 'user':
                st.markdown(f"<div class='chat-box message user-message'>You ({chat['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}):<br>{chat['message']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-box message bot-message'>ConfigCraft.ai ({chat['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}):<br>{chat['message']}</div>", unsafe_allow_html=True)

    # Use a form for the chat input
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("How can I help you?", key="user_input")
        submit_button = st.form_submit_button("Send")

    # On input submission, process the input and store it in chat history
    if submit_button and user_input:
        response = process_input(user_input)

        st.session_state.chat_history.append({'type': 'user', 'message': user_input, 'timestamp': datetime.now()})
        st.session_state.chat_history.append({'type': 'bot', 'message': response, 'timestamp': datetime.now()})

        st.experimental_rerun()

def process_input(user_input):
    print(st.session_state.chat_history)
    return get_ai_response(user_input)

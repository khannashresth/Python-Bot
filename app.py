import streamlit as st
import logging
from main import AICodeGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('AI Code Generator')

# Initialize the AI Code Generator
generator = AICodeGenerator()

# Set up the Streamlit app
st.title('AI Code Generator Chatbot')

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# User input
user_input = st.chat_input('Enter your code generation request:')

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.markdown(user_input)

    # Generate code
    try:
        generated_code = generator.generate_code(user_input)
        # Add assistant message to chat history
        st.session_state.messages.append({'role': 'assistant', 'content': generated_code})
        with st.chat_message('assistant'):
            st.markdown(generated_code)
    except Exception as e:
        logger.error(f'Error generating code: {str(e)}')
        st.error(f'Error: {str(e)}') 
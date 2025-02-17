import streamlit as st
import time
import random
import backend

# Define avatar images (Use local file paths or URLs)
BOT_IMAGE_URL = "https://c.wallhere.com/photos/84/cc/AI_art_digital_art_women_illustration_animal_ears_cat_girl_short_hair_portrait-2217820.jpg!d"

USER_IMAGE_URL = "https://i.pinimg.com/originals/34/bb/e2/34bbe23a8a187b1f250fde8b7b4bad58.jpg"


# Function to generate a response
def response_generator(prompt):
    response = backend.GenerateResponse(prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Chat with princess👸🪄")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with avatars
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=BOT_IMAGE_URL if message["role"] == "assistant" else USER_IMAGE_URL):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show user message with avatar
    with st.chat_message("user", avatar=USER_IMAGE_URL):
        st.markdown(prompt)

    # Show assistant response with avatar
    with st.chat_message("assistant", avatar=BOT_IMAGE_URL):
        response = st.write_stream(response_generator(prompt))

    # Store bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

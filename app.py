import streamlit as st
import openai

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("## :gray[Turn Audio into Text or Text into Audio]")

st.text("Enter your OpenAI API token")
api_key = st.text_input("Enter your OpenAI API token:", type='password', key = 'token', label_visibility='collapsed')

if not (api_key.startswith('sk-') and len(api_key) == 51):
        st.warning('Please enter your credentials!', icon = '⚠️')
else:
    st.success("The operation was successful!", icon = '✅')

transcribe, generate, minutes = st.tabs([":blue[Transcribe]", ":blue[Generate]", "Meeting Minutes"], )

def transcribe_audio(audio_file):
    openai.api_key = api_key
    transcription = openai.audio.transcriptions.create(
            model = "whisper-1", 
            file = audio_file
        )
    return transcription.text

with transcribe:
    st.subheader("Transcribes audio into the input language")

    uploaded_audio = st.file_uploader("Choose a audio file", key='audio_input', disabled=not api_key)
    st.divider()
    if uploaded_audio is not None:
        st.text(transcribe_audio(uploaded_audio))
        

with generate:
    st.subheader("Generates audio from the input text")

    txt = st.text_area("text to generate", disabled=not api_key)



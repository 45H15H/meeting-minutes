import streamlit as st
import openai

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("## :gray[Turn Audio into Text or Text into Audio]")

with st.form(key='api_form'):
    st.markdown("""
    Enter your OpenAI API token :red[*]
    """)
    api_key = st.text_input("Enter your OpenAI API token:", type='password', key = 'token', label_visibility='collapsed')
    st.form_submit_button("SUBMIT")

if not (api_key.startswith('sk-') and len(api_key) == 51):
        st.warning('Please enter your credentials!', icon = '⚠️')
else:
    st.success("The operation was successful!", icon = '✅')

transcribe, generate, minutes = st.tabs([":blue[Transcribe]", ":blue[Generate]", "Meeting Minutes"], )

@st.cache_data
def transcribe_audio(audio_file):
    openai.api_key = api_key
    transcription = openai.audio.transcriptions.create(
            model = "whisper-1", 
            file = audio_file
        )
    return transcription.text

global r
r = ""
with transcribe:
    st.subheader("Transcribes audio into the input language")

    uploaded_audio = st.file_uploader("Choose a audio file", key='audio_input', disabled=not api_key)
    if uploaded_audio is not None:
        t_button = st.button("Transcribe", type="primary", disabled=not api_key)
    st.divider()
    if uploaded_audio and t_button:
        progress_bar = st.progress(0, "Operation in progress. Please wait...")
        result = transcribe_audio(uploaded_audio)
        r = result
        progress_bar.progress(100)
        st.text_area(label="", value=result, label_visibility='collapsed', key="t_1")
    if r:
        st.download_button("Download text", data = result, mime = 'text/plain', file_name="transcript.txt")
        
@st.cache_data
def generate_audio(txt, voice, speed):
    openai.api_key = api_key
    speech_file_path = "speech.mp3"
    response = openai.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=txt,
        speed=speed
    )

    response.stream_to_file(speech_file_path)
    return speech_file_path

global a
a = ''
with generate:
    st.subheader("Generates audio from the input text")

    txt = st.text_area("Text to generate audio for", disabled=not api_key, max_chars=4096)
    if txt is not None:
        col1, col2 = st.columns(2)
        with col1:
            voice = st.selectbox("Select voice", ("alloy", "echo", "fable", "onyx", "nova", "shimmer"), index=4, disabled=not txt, help="The voice to use when generating the audio.")
        with col2:
            speed = st.slider("Specify speed", min_value=0.25, max_value=4.0, value=1.0, disabled=not txt, step=0.25, help = "The speed of the generated audio.", )
        g_button = st.button("Generate", type="primary", disabled=not txt)
    st.divider()
    if txt is not None and g_button:
        progress_bar = st.progress(0, "Operation in progress. Please wait...")
        audio_file_path = generate_audio(txt, voice, speed)
        a = audio_file_path
        progress_bar.progress(100)
        st.audio(audio_file_path, format="audio/mp3")
    if a:
        st.download_button("Download audio", data = audio_file_path, mime="audio/mp3", file_name="speech.mp3")




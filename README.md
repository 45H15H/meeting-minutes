# MinuteGen

Meeting Minutes Generator is a web application that uses OpenAI API models to automatically generate meeting minutes from audio recordings.

## Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://meeting-minutes-v1.streamlit.app/)

## Installation

Clone the repository.

Install the required libraries with pip:

```powershell
pip3 install -r requirements.txt
```
## Usage

To run the application, run the following command in the terminal:

```powershell
streamlit run app.py
```

## Features

- Generate meeting minutes from audio recordings
- Generate audio from text with different voices and speeds
- Generate transcripts from audio recordings in different languages
- Dowlnoad the generated files

## Note
In meeting minutes the analysis features are limited to two because of the rate limit on gpt-3.5-turbo model. In free tier it allows only 3 requests per minute. So, I have used two requests for meeting minutes and one for transcription. If you want to use all the features, you can upgrade to paid tier.

## Contact

Created by [Ashish Singh](https://www.linkedin.com/in/45h15h/) - feel free to contact me!

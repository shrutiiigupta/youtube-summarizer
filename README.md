pip install -r requirements.txt

to run application:
streamlit run main.py

Steps:
1. Extract Transcript
    - A. Directly from yt API
    - B. ASR(Automatic speech recognition)
        - i. Whisper OpenAI model (heavy)
2. Transcript summarization
    - A. Abstractive
        - i. Pegasus
    - B. Extractive
        - i. nltk
        - ii. Spacy



    
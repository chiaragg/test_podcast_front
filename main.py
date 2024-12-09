#ffmpeg
#ipython
#podcastfy
#dotenv
#os
#litellm
#llamaapi

from podcastfy.client import generate_podcast
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import litellm
import llamaapi

from llamaapi import LlamaAPI
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from IPython.display import Audio, display

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key and gemini_api_key:
    print(f"API key found! First few characters: {gemini_api_key[:4]}...")
    print(f"API key found! First few characters: {openai_api_key[:4]}...")
else:
    print("No API key found in .env file!")



def embed_audio(audio_file):
    """
    Embeds an audio file in the notebook, making it playable.

    Args:
            audio_file (str): Path to the audio file.
    """
    try:
            display(Audio(audio_file))
            print(f"Audio player embedded for: {audio_file}")
    except Exception as e:
            print(f"Error embedding audio: {str(e)}")



try:
    audio_file = generate_podcast(
        # urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
        urls=["https://www.wikimanche.fr/Famille_de_Hauteville"],
        llm_model_name= "gpt-3.5-turbo-0125",
        api_key_label="OPENAI_API_KEY"
    )
    print(f"Generated podcast saved to: {audio_file}")
except Exception as e:
    print(f"Error occurred: {str(e)}")
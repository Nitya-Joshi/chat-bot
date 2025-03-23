import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models
models = genai.list_models()
for model in models:
    print(model.name, "->", model.supported_generation_methods)

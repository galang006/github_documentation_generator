from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY"),
        )

        self.model_name = os.getenv("GEMINI_MODEL_NAME")

    def generate_text(self, prompt): 
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            # max_tokens=int(os.getenv("GEMINI_MAX_TOKENS", 1024)),
            # temperature=float(os.getenv("GEMINI_TEMPERATURE", 0.7))
        )
        return response.text
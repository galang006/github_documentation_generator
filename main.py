from gemini_api.gemini_client import GeminiClient

if __name__ == "__main__":
    client = GeminiClient()
    prompt = "can you make markdown documentation for this code? "
    response = client.generate_text(prompt)
    print(response)
from gemini_api.client import GeminiClient

if __name__ == "__main__":
    client = GeminiClient()
    prompt = "What is the capital of France?"
    response = client.generate_text(prompt)
    print(response)
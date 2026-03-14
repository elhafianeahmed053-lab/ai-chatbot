import requests

url = "http://localhost:11434/api/generate"

print("Local AI Chatbot (type 'exit' to quit)\n")

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    response = requests.post(
        url,
        json={
            "model": "codellama",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    print("\nAI:", data["response"], "\n")

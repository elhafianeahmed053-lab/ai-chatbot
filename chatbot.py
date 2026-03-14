import requests

url = "http://localhost:11434/api/generate"

print("Local AI Chatbot (type 'exit' to quit)\n")

conversation = ""

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    conversation += f"User: {user_input}\nAI: "

    response = requests.post(
        url,
        json={
            "model": "codellama",
            "prompt": conversation,
            "stream": False
        }
    )

    data = response.json()
    ai_reply = data["response"]

    conversation += ai_reply + "\n"

    print("\nAI:", ai_reply, "\n")


# Call OpenAI, return response.

from openai import OpenAI
import os

def getChat(text: str) -> str:
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("Chat with ChatGPT!!!")
    while True:
        userIn = input("You: ")
        if userIn.lower() == "exit":
            break
        
        reply = getChat(userIn)
        print("Chat: " + reply)
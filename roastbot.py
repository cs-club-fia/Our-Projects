import random
import time

roasts = [
    "You call *that* a question? 💀",
    "Bro... Google exists, y’know.",
    "I'm losing brain cells answering this 😭",
    "Did you copy-paste that from your homework?",
    "You're the reason AI wants to take over humanity 😈",
    "You sound like a ChatGPT prompt gone wrong 💀",
    "Hold on... let me pretend to care 🤡"
]

def roastabot():
    print("🔥 Roast-a-Bot 3000 🔥")
    print("Type 'exit' to escape the pain.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: finally... peace 😌")
            break
        time.sleep(random.uniform(0.5, 1.5))
        print("Bot:", random.choice(roasts))

roastabot()

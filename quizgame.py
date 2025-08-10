print("Welcome to the Quiz Game!")
name = input("Enter your name: ")
print(f"Hello, {name}! Let's start the game.")

score = 0
questions = {
    "What is the capital of India?": "New Delhi",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is the largest mammal on Earth?": "Blue Whale"
}

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Sorry, the correct answer is {answer}.")

print(f"Game over, {name}! Your final score is {score} out of {len(questions)}.")

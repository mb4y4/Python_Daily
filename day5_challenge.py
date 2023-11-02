#simple quiz game

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of Kenya?\n(a) Nairobi\n(b) Mombasa\n(c) Kisumu\n", "a"),
    Question("What is the name of the smallest horse?\n(a) Falabella\n(b) Shetland Pony\n(c) Miniature Horse\n", "c"),
    Question("What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n", "b"),
    # Add more questions and answers here
]

def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question.prompt)
        if user_answer.lower() == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {question.answer}.\n")

    print(f"You got {score}/{len(questions)} questions correct.")

if __name__ == "__main__":
    print("Welcome to the Python Quiz Game!")
    run_quiz(questions)

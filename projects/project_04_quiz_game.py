questions = [
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. print()", "B. input()", "C. len()", "D. type()"],
        "answer": "A"
    },
    {
        "question": "What data type is \"hello\"?",
        "options": ["A. Integer", "B. String", "C. Boolean", "D. List"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "What does len(\"python\") return?",
        "options": ["A. 5", "B. 6", "C. 7", "D. Error"],
        "answer": "B"
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C"
    }
]

def run_quiz():
    score = 0

    print("Welcome to the Python Basics Quiz!\n")

    for index, question in enumerate(questions, start=1):
        print(f"Question {index}: {question['question']}")

        for option in question["options"]:
            print(option)

        answer = input("Choose the correct option (A/B/C/D): ")

        if answer.strip().upper() == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Oops! Better luck next time. The correct answer is {question['answer']}.\n")

    print(f"\nYou got {score} out of {len(questions)}.")


run_quiz()

questions = [
    {
        "question": "1. What is 2 + 2?",
        "option": ["A). 3", "B). 4","C). 5", "D). 6"],
        "answer": "B"
    },
    {
        "question": "2. What color is the sky on a clear day?",
        "option": ["A). Red", "B). Blue","C). Green", "D). Yellow"],
        "answer": "B"
    },
    {
        "question": "3. How many legs does a spider have?",
        "option": ["A). 6", "B). 7","C). 8", "D). 9"],
        "answer": "C"
    },
    {
        "question": "4. What sound does a cow make?",
        "option": ["A). Meow", "B). Bark","C). Moo", "D). Quack"],
        "answer": "C"
    },
    {
        "question": "5. What is the opposite of hot?",
        "option": ["A). Warm", "B). Cold","C). Cool", "D). Boiling"],
        "answer": "B"
    }
]



def start_cbt():
    total_score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["option"]:
            print(option)
        
        user_answer = input("Enter your answer(A, B, C, D): ").strip().upper()

        if user_answer == q["answer"]:
            print("✅ correct answer")
            total_score += 1
        else:
            print(f"❌ Wrong Answer! The correct answer is {q["answer"]}")
    print(f"CBT Exam Completed. you scored {total_score}")
    

        



menu = """
1. Hardcore question and answer
2. exit


"""

print("Welcome 👋")

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ").strip()

    if choice == "2":
        print("Good bye 👋")
        break

    if choice not in "12":
        print("Invalid Input. Please Enter option (1 - 2)")
        continue

    if choice == "1":
        start_cbt()

import random

# Define a dictionary of questions with their corresponding answers and options
questions = {
    "What is the capital of France?": {
        "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        "answer": "B"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["A. Jupiter", "B. Mars", "C. Venus", "D. Mercury"],
        "answer": "B"
    },
    "Who wrote 'Romeo and Juliet'?": {
        "options": ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Leo Tolstoy"],
        "answer": "A"
    }
}

def display_question(question, options):
    print(question)
    for option in options:
        print(option)

def check_answer(question, user_answer):
    correct_answer = questions[question]["answer"]
    if user_answer.upper() == correct_answer:
        print("Congratulations! Your answer is correct.")
        return True
    else:
        print("Sorry, your answer is incorrect. The correct answer is", correct_answer)
        return False

def kbc_game():
    print("Welcome to KBC!")
    amount = 0
    question_list = list(questions.keys())  # Convert dictionary keys to a list for random selection

    while question_list:
        current_question = random.choice(question_list)
        display_question(current_question, questions[current_question]["options"])
        user_input = input("Enter your choice (A/B/C/D): ")
        if user_input.upper() == "QUIT":
            break
        elif user_input.upper() in ['A', 'B', 'C', 'D']:
            if check_answer(current_question, user_input):
                amount += 10000
            else:
                amount = 0  # Penalize for incorrect answers
            print("Your current amount is:", amount)
            question_list.remove(current_question)  # Remove the question from the list to avoid repetition
        else:
            print("Invalid input. Please enter A, B, C, or D.")

    print("Game Over! Your final amount is:", amount)

# Run the game
kbc_game()

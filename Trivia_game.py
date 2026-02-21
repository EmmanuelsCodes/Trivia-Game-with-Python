# My first "serious" Python exercise! 

import random

questions = {
    "Is ChatGPT better than Claude for coding?": "No",
    "When was Metal Gear Solid V released?": "2015",
    "Who is the creator of the Metal Gear Solid franchise?": "Hideo Kojima",
    "Was this trivia game hard to make?": "No",
    "Who is the worst president of America?": "Trump",
    "What does Steve Bonnell do for a living?": "Debate",
    "Is Python a goated language?": "Yes",
    "Have I always been an AI Engineer?": "No",
    "How much is 1 + 1?": "2",
    "What is Prosperty?": "A PropTech company"
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0
    
    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]
        
        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {correct_answer}.\n")
            
    print(f"Game over! Your final score is: {score}/{total_questions}")
    
python_trivia_game()
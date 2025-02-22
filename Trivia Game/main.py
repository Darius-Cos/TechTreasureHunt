# list of questions
# store the answers

# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score

import random 


# list of questions
questions= {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

def trivia_game():
    print("Welcome to the Trivia Game!")
    questions_list=list(questions.keys()) # to get all the values from the dictionary
    total_questions=5 # thw questions that are going to be asked
    score=0
    selected_questions = random.sample(questions_list, total_questions) # randomly select 5 questions from the dictionary
    print(selected_questions)

    for index,question in enumerate(selected_questions):
        print(f"{index+1}. {question}")
        user_answer=input("Enter your answer: ").lower().strip() #strip() to remove leading and trailing whitespaces and lower() to convert the answer to lowercase
        
        correct_answer=questions[question]
        if user_answer==correct_answer.lower():
            print("Correct!\n")
            score+=1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")   

    print(f"Your final score is {score}/{total_questions}")

trivia_game()




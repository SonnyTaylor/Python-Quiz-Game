import random
# import the random library so that questions can be picked at random

# list of all the questions with their corresponding options and answers
questions = [
    {
        "question": "What is the output of this code in python: print(3 + '3')",
        "options": ["A. 6", "B. 33", "C. TypeError", "D. '6'"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for web development?",
        "options": ["A. Python", "B. Java", "C. Ruby", "D. JavaScript"],
        "answer": "D"
    },
    {
        "question": "What does OOP mean?",
        "options": ["A. Original Objectified Python", "B. Object Orginated Programs", "C. Object Orginated Programming", "D. Orange Orangatang Pie"],
        "answer": "C"
    }
    {
        "question": "What is the correct symbol for adding a comment in python?",
        "options": ["A. //", "B. #", "C. <!-- -->", "D.  /* */"],
        "answer": "B"  
    }
    {
        "question": "Who created python?",
        "options": ["A. Guido van Rossum", "B. Linus Torvals", "C. Terry A. Davis", "D. Tim Berners-Lee"],
        "answer": "A" 
    }
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. int", "B. double", "C. list", "D. tuple"],
        "answer": "B"
    },
    
]


def ask_question(question):
    """Takes a question from the question list, asks user the questions then returns the answe as user_answer

    Args:
        question (list): list of all questions with their corresponding answers and options

    Returns:
        user_answer: returns the users answer as a string
    """
  print(question['question'])
  for option in question['options']:
    print(option)

  user_answer = input("Enter your answer (A, B, C, D): ").upper() # ask the user a question and convert to uppercase to avoid errors
  return user_answer == question['answer']

if __name__ == "__main__":
  score = 0 # set the score to 0 when starting
  random.shuffle(questions) # shuffle the questions to make it more random

  for i in range(1, 6):
    print(f"Question {i} of 5")
    question = questions[i]

    if ask_question(question):
      print("Correct!\n")
      score += 1 # add to score if answer is correct
    else:
      print(f"Wrong! The correct answer is {question['answer']}.\n") # dont add to score if it is incorrect

  print(f"You scored {score}/5.") # print total score after answering all questions


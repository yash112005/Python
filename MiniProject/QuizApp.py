# Questions and answers
questions = {
    "What is the capital of India?": "New Delhi",
    "Who is known as the Father of Computers?": "Charles Babbage",
    "Which planet is known as the Red Planet?": "Mars",
    "What is 5 + 7?": "12",
    "Who wrote 'Hamlet'?": "William Shakespeare"
}

# Quiz logic
score = 0
print("Welcome to the Quiz App!\n")

for question, answer in questions.items():
    print(question)
    user_answer = input("Your answer: ").strip()
    if user_answer.lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is: {answer}\n")

# Final score
print(f"Quiz completed! Your final score is {score}/{len(questions)}.")





 

  


  

  
  
  
  




def Ask_Question(question, option1, option2, option3, option4, correct_index):
    # Printing question and options
    print(question)
    print(f"1. {option1}")
    print(f"2. {option2}")
    print(f"3. {option3}")
    print(f"4. {option4}")

    # Taking Answer of the question
    answer = (input("Choose the correct option (1-4): "))

    # If the answer is digit and the answer is integer , then we will do - 1 because indexing starts from 0 
    if answer.isdigit() and int(answer) - 1 == correct_index:
        print("Correct!\n") # If the correct answer is option3. then 3 - 1 = 2. [0,1,2] total = 3
        return True
    else:
        print(f"The correct was: {option1 if correct_index == 0 else option2 if correct_index == 1 else option3 if correct_index == 2 else option4}\n")
        return False

def Quiz_Game():
    print("Welcome to the Quiz Game!") 
    score = 0
    
    if Ask_Question("What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 1):
        score += 1
    if Ask_Question("Which planet is closest to the Sun?", "Earth", "Venus", "Mercury", "Mars", 2):
        score += 1
    if Ask_Question("How many days are in a leap year?", "365", "366", "364", "367", 1):
        score += 1
    if Ask_Question("What is 12 x 12?", "124", "144", "132", "148", 1):
        score += 1
    if Ask_Question("Which is the largest ocean?", "Atlantic", "Indian", "Arctic", "Pacific", 3):
        score += 1
    if Ask_Question("What language is used in AI/ML?", "Java", "C++", "Python", "Ruby", 2):
        score += 1
    if Ask_Question("Who invented the telephone?", "Edison", "Tesla", "Graham Bell", "Newton", 2):
        score += 1
    if Ask_Question("What does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Processing Unit", "Core Processing Unit", 1):
        score += 1
    if Ask_Question("Which is the fastest animal?", "Lion", "Horse", "Cheetah", "Leopard", 2):
        score += 1
    if Ask_Question("How many bones in human body?", "205", "206", "207", "208", 1):
        score += 1

    print(f"The Game is over. Your score is {score} out of 10")

Quiz_Game()

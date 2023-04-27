#!/usr/bin/env python3
"""
Return unique answers based on the input provided... multiple results should be possible.
AS BEST YOU'RE ABLE, control for user errors (suggested: methods, try/except, while loop)
Use at least one while loop.
Make all code "your own."
ROUGH minimum of 40 lines of code... if code is spread out across multiple files, they are cumulative.

Which power tool brand should you select.
Questions
Answers (need try-catch for wrong entry)
Points for each question
Total Points
if-else for brands based on points
Print result
"""
def power_tool_quiz():
    print("Welcome to the Power Tool Brand Quiz!")
    print("Answer the following questions to find out which power tool brand is best for you.\n")

# Questions
    questions = [   "1. Do you not want your power tools to suck?",
                    "2. What is your budget for your power tools?",
                    "3. How durable do you need your tools to be?",
                    "4. Do you need plug-in or battery operated tools?",
                    "5. What color do you prefer your tools to be?"]

# Answers
    answers = [ ["Yes", "No", "Don't Care"],
                ["$", "$$", "$$$"],
                ["I only need it once", "Durable", "Very Durable"],
                ["Plug", "Battery", "Don't Care"],
                ["Black", "Yellow", "Red"]]

# Points for to each answer
    points = [  [1, 3, 0],
                [1, 2, 3],
                [1, 2, 3],
                [1, 3, 0],
                [1, -7, 5]]

    total_points = 0

# Go through each question and get user's input
    for i in range(len(questions)):
        print(questions[i])
        for j in range(len(answers[i])):
            print(f"{j + 1}. {answers[i][j]}")
        
# User input and handle errors
        while True:
            try:
                user_input = int(input("Enter your answer (1-3): "))
                if user_input < 1 or user_input > 3:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input! Please select a valid answer (1-3).\n")
        
        total_points += points[i][user_input - 1]
        print()

# Determine the power tool brand based on total points
    if total_points <= 5:
        result = "I can't help you because yellow brands suck"
    elif 6<= total_points <= 9:
        result = "Black and Decker would be your best bet"
    elif total_points == 10:
        result = "you are biased towards Dewalt but, yellow brands suck so you should just get Milwaukee"
    else:
        result = "Milwaukee will best suit your needs."

    print(f"Based on your answers to the questions, {result}.")


power_tool_quiz()

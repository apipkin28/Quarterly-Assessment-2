import sqlite3

# connect to db
conn = sqlite3.connect('QuizBowl.db')
cursor = conn.cursor()

# defining function for questions from chosen category
def quizCateg(category):
    cursor.execute(f"SELECT * FROM {category}")
    values = cursor.fetchall()

    # keep score
    score = 0

    # iterate each question
    for value in values:
        question = value[1]
        correctAns = value[2]  
        print(question)
        userAns = input("Your answer: ")
        if userAns.strip().lower() == correctAns.strip().lower():
            # green
            print("\033[92mCorrect!\033[0m")
            # add point since correct answer
            score += 1
        else:
            # red
            print("\033[91mIncorrect. The correct answer is:", correctAns, "\033[0m")

    # tell user their final score
    print("Your final score is", score, "out of", len(values))

# defining main function of program
def main():
    print("""Out of the five categories, which would you like to be quizzed on?
             1. Business App Development
             2. Behavioral Economics
             3. Economics Workshop
             4. Risk Management and Insurance
             5. Calculus II
             """)
    # prompt user
    userCateg = input("Which number do you choose? ")

    # dictionary
    categories = {
        "1": "Business_Applications_Development",
        "2": "Behavioral_Economics",
        "3": "Economics_Workshop",
        "4": "Risk_Management_And_Insurance",
        "5": "Calculus_II"
    }
    
    if userCateg in categories:
        # call quizcateg function -- have to call or the questions do not show
        quizCateg(categories[userCateg])
    else:
        print("This is not an option. Please respond with a valid option, 1-5.")

# make sure script running as main program
if __name__ == "__main__":
    main()
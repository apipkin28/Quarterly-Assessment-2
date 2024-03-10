import sqlite3

# connect to db
conn = sqlite3.connect('QuizBowl.db')
cursor = conn.cursor()

# defining function for questions from chosen category
def quizCateg(category):
    cursor.execute(f"SELECT * FROM {category}")
    values = cursor.fetchall()

    # iterate each question
    for value in values:
        question = value[1]
        correctAns = value[2]  
        print(question)
        userAns = input("Your answer: ")
        if userAns.strip().lower() == correctAns.strip().lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correctAns)

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

# make sure script running as main program
if __name__ == "__main__":
    main()
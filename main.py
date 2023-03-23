def main():
    print("Welcome to my computer quiz!")
    if input_accepted():
        start_game()
    else:
        print("Bye...")


def input_accepted() -> bool:
    response = input("Do you want to play? ")
    return response.lower().strip() == "yes"


def start_game():
    print("Okay! Let's play :)")
    ask_questions({"What does CPU stand for?": "central processing unit",
                   "What does GPU stand for?": "graphics processing unit",
                   "What does RAM stand for?": "random access memory",
                   "What does PSU stand for?": "power supply"})


def ask_questions(questions: dict[str]):
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print_summary(score)


def print_summary(score: int) -> None:
    print("You got " + str(score) + " questions correct")
    print("You got " + str(score / 4 * 100) + "% correct")


if __name__ == '__main__':
    main()

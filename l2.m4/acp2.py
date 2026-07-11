import requests
import random
import html

url = "https://opentdb.com/api.php?amount=5&type=multiple"

def quiz():
    try:
        data = requests.get(url)
        questions = data.json()["results"]
    except:
        print("Unable to fetch questions.")
        return

    score = 0

    print(" TRIVIA QUIZ \n")

    for i, q in enumerate(questions, 1):
        question = html.unescape(q["question"])
        answer = html.unescape(q["correct_answer"])

        options = [html.unescape(x) for x in q["incorrect_answers"]]
        options.append(answer)
        random.shuffle(options)

        print(f"Question {i}: {question}\n")

        for j, option in enumerate(options, 1):
            print(f"{j}. {option}")

        while True:
            try:
                choice = int(input("\nEnter your answer (1-4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except:
                print("Invalid input. Try again.")

        if options[choice - 1] == answer:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer: {answer}\n")

    print(" RESULT ")
    print("Correct Answers:", score)
    print("Total Questions:", len(questions))
    print("Score:", round((score / len(questions)) * 100, 2), "%")

quiz()
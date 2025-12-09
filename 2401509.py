import random

def load_question_bank(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]
        
        # Pair questions and answers (each question is followed by its answer)
        question_answer_pairs = []
        for i in range(0, len(lines), 2):
            if i+1 < len(lines):
                question = lines[i]
                answer = lines[i+1]
                question_answer_pairs.append((question, answer))

        return question_answer_pairs

    except FileNotFoundError:
        print("The file path is incorrect. Please try again.\n")
        return None


def create_exam(qbank, number_of_questions, output_file):
    selected_pairs = random.sample(qbank, number_of_questions)

    with open(output_file, "w", encoding="utf-8") as file:
        for i, (q, a) in enumerate(selected_pairs, start=1):
            file.write(f"Q{i}: {q}\n")
            file.write(f"Answer: {a}\n\n")


def main():
    print("Welcome to professor assistant version 1.0.")
    name = input("Please Enter Your Name: ")

    print(f"Hello Professor {name}, I am here to help you create exams from a question bank.")

    while True:
        choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ").strip().lower()

        if choice == "no":
            print(f"Thank you Professor {name}. Have a good day!")
            break

        elif choice == "yes":
            # Load question bank
            path = input("Please Enter the Path to the Question Bank: ").strip()
            qbank = load_question_bank(path)

            if qbank is None:
                continue

            print("Yes, indeed the path you provided includes questions and answers.")

            # Number of questions
            while True:
                try:
                    num = int(input("How many question-answer pairs do you want to include in your exam? "))
                    if num > len(qbank):
                        print(f"There are only {len(qbank)} questions available. Please enter a smaller number.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")

            # Output file
            output_file = input("Where do you want to save your exam? ").strip()

            create_exam(qbank, num, output_file)

            print(f"Congratulations Professor {name}. Your exam is created and saved in {output_file}.\n")

        else:
            print("Invalid input. Please enter Yes or No.\n")


if __name__ == "__main__":
    main()

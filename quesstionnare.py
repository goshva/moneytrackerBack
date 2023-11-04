class Questionnaire:
    def __init__(self):
        self.questions = []  # list to store the questions
        self.branches = {}  # dictionary to store the branching logic

    def add_question(self, question):
        self.questions.append(question)

    def add_branch(self, question, answer, result):
        if question in self.branches:
            self.branches[question].append((answer, result))
        else:
            self.branches[question] = [(answer, result)]

    def run_questionnaire(self):
        answers = {}  # dictionary to store user's answers

        # Ask each question in order and store the answers
        for question in self.questions:
            print(question)
            answer = input("Your answer: ")
            answers[question] = answer

        # Determine the result based on the answers using the branching logic
        result = None
        for question, answer in answers.items():
            if question in self.branches:
                for branch in self.branches[question]:
                    if branch[0] == answer:
                        result = branch[1]
                        break

        # Display the result
        if result:
            print("Your result is:", result)
        else:
            print("No result found based on your answers.")


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def ongoing(self):
        return self.question_number < len(self.question_list)

    def next_question(self, ):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text}: (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.title() == current_answer:
            print("You got it right!!!")
            self.score += 1
        else:
            print(f"Oops, that's wrong, it's actually {current_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

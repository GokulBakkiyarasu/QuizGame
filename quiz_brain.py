class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        return self.check_score(user_input, current_question.answer)

    def check_score(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is: {self.score}/{self.score}.")
            return True
        else:
            print("You were wrong.")
            print(f"The correct answer was: {correct_answer}.")
            print(f"Your current score is: {self.score}/{self.score+1}.")
            return False


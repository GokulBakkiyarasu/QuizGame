from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))

quiz = QuizBrain(question_bank)
should_continue = True
while should_continue:
    if quiz.still_has_question():
        should_continue = quiz.next_question()


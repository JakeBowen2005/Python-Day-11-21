from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    new_q = Question(data["text"], data["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_q():
    quiz.next_question()
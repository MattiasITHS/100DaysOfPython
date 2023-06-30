from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

questions_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_question():
    quiz.next_question()
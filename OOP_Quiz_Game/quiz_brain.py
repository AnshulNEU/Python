class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        que =  self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f'Q.{self.question_number}:{que.text} (True/False)?:')
        self.check_answer(user_ans, que.answer)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("You're correct")
            self.user_score += 1
        else:
            print("Sorry, that's wrong")
        print(f'The correct answer is {correct_answer}')
        print(f"Your current score: {self.user_score}/{self.question_number}")


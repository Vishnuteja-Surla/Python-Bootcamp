class QuizBrain:

    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        que = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q.{self.question_no}: {que.text} (True/False)?: ")
        self.check_answer(ans, que.answer)

    def still_has_questions(self):
        if self.question_no == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, ans, c_ans):
        if ans.lower() == c_ans.lower():
            print("That is correct!")
            self.score += 1
        else:
            print("You are wrong!")
            print("Correct answer : ", c_ans)
        print(f"Your Score : {self.score}/{self.question_no}")
        print("\n")

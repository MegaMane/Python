class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        user_answer = input(f"\nQ.{self.question_number + 1}: " + 
                            f"{self.questions_list[self.question_number].text}" +
                            f"\n\n(True or False?)>>")
        if self.check_answer(user_answer):
            print("You got it right!")
        else:
            print("Sorry that's not correct.")

        print(f"Score: {self.score}/{len(self.questions_list)}")
        self.question_number +=1



    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self,answer):
        if answer.title() == self.questions_list[self.question_number].answer:
            self.score += 1
            return True
        return False


    #TODO: asking the questions
    #TODO: checking if the answer was correct
    #TODO: checking if we're the end of the quiz
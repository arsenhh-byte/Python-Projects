# Creating a class called QuizBrain
class QuizBrain:
    def __init__(self,q_list):
        # Initialize the question_number to 0
        # initialize the question_list to an input
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
# Creating a method that returns a boolen value for a while loop
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    
    
    
# Creating another method called next_question in QuizBrain
    def next_question(self):
        # getting the current question from the question list and passing question number to get current question
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Passing the current question as an input
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
# Checking user answer and keeping score 
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
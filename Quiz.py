import tkinter as tk
from Question import Question
from data import questions

class Quiz:
    def __init__(self, parent):

        self.frame = parent.frame

        self.questions = []
        for question in questions:
            self.questions.append(Question(self, question["question"], question["answers"]))

        self.i = 0
        self.questions[0].start()


        self.nextbtn = tk.Button(self.frame, text = "Далее", font = 12, command = self.next_question)  
        self.nextbtn.grid(pady = 24, row = 1)


    def next_question(self):
        self.questions[self.i].end()

        if self.i < len(self.questions) - 1:
            self.i += 1
            self.questions[self.i].start()
        else:
            self.lbl = tk.Label(self.frame, text = f"Тестирование завершено. Ваш результат: {self.get_score()}/{len(questions)}", font = (18))
            self.nextbtn.destroy()
            self.lbl.grid(row = 0)

    def get_score(self):
        score = 0
        for i in range(len(questions)):
            right_answer = questions[i]["right_answer"]
            user_answer = self.questions[i].var.get()
            if user_answer == right_answer:
                score += 1

        return score

    def start(self):
        self.frame.grid()

    def end(self):
        self.frame.grid_forget()    

    
    

        

        
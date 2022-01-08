THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:

    def __init__(self, quiz : QuizBrain):
        self.window = Tk()
        self.score_so_far = 0
        self.quiz = quiz
        self.score = Label(text=f"Score: {self.score_so_far}", bg = THEME_COLOR, fg="white")
        self.score.grid(column=1,row=0)
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150,125, text="", fill=THEME_COLOR, font = ("Aria;",20, "italic"), width =280)
        self.canvas.grid(column=0,row=1, columnspan=2, padx = 20,pady =20)
        self.photo_f = PhotoImage(file="images/false.png")
        self.f_button = Button(image=self.photo_f, command=self.pick_false)
        self.f_button.grid(column=1,row=2)
        self.photo_t = PhotoImage(file="images/true.png")
        self.t_button = Button(image=self.photo_t, command=self.pick_true)
        self.t_button.grid(column=0, row=2)
        self.window.title("Quizzler")
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"You've read the end of the quiz your score is {self.score_so_far}/10")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")
    def pick_true(self):
        if self.quiz.check_answer("true"):
            self.score_so_far +=1
            self.score.config(text=f"Score:{self.score_so_far}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def pick_false(self):
        if self.quiz.check_answer("false"):
            self.score_so_far += 1
            self.score.config(text=f"Score:{self.score_so_far}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



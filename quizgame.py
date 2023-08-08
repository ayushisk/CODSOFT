import tkinter as tk

class QuizGame(tk.Tk):
    def __init__(self, questions):
        super().__init__()

        self.title("Quiz Game")
        self.geometry("600x500")

        self.questions = questions
        self.current_question = 0
        self.score = 0
        
         
        self.welcome_label = tk.Label(self, text="Welcome to the Quiz!", font=("Calibri", 20, "bold"))
        self.welcome_label.pack(pady=10)

        self.rules_label = tk.Label(self, text="Rules:\n1. Answer all questions.\n2. Each question carries 1 point.", font=("Calibri ", 16))
        self.rules_label.pack(pady=10)
        
       
        self.question_label = tk.Label(self, text="", font=("Calibri", 12))
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.option1_radio = tk.Radiobutton(self, text="", variable=self.radio_var, value=1)
        self.option1_radio.pack(pady=5)
        self.option2_radio = tk.Radiobutton(self, text="", variable=self.radio_var, value=2)
        self.option2_radio.pack(pady=5)
        self.option3_radio = tk.Radiobutton(self, text="", variable=self.radio_var, value=3)
        self.option3_radio.pack(pady=5)

        self.next_button = tk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(self, text="")
        self.score_label.pack(pady=10)

        self.display_question()

    def display_question(self):
        question = self.questions[self.current_question]
        self.question_label.configure(text=question["question"])
        self.option1_radio.configure(text=question["options"][0])
        self.option2_radio.configure(text=question["options"][1])
        self.option3_radio.configure(text=question["options"][2])

    def check_answer(self):
        question = self.questions[self.current_question]
        answer = question["answer"]
        user_answer = self.radio_var.get()

        if user_answer == answer:
            self.score += 1

    def next_question(self):
        self.check_answer()
        self.current_question += 1

        if self.current_question == len(self.questions):
            self.show_score()
        else:
            self.display_question()

    def show_score(self):
        self.question_label.configure(text="Quiz Completed!")
        self.option1_radio.pack_forget()
        self.option2_radio.pack_forget()
        self.option3_radio.pack_forget()
        self.next_button.pack_forget()
        self.score_label.configure(text=f"Your Score: {self.score}/{len(self.questions)}")
        self.score_label.pack(pady=10)

questions = [
    {
        "question": "Who is the Author of Mahabharata?",
        "options": ["Krishna Dvaipayana(Vedavyasa)", "Valmiki", "Chanakya"],
        "answer": 1
    },
    {
        "question": "Who is the ancient Indian Scholars calculated the exact value of pi?",
        "options": ["Aryabhatta", "Brahmagupta", "Bhaskaracharya"],
        "answer": 2
    },
    {
        "question": "Who is father of Indian Medicine?",
        "options": ["Charaka", "Patanjali", "Panini"],
        "answer": 1
    }
]
game = QuizGame(questions)
game.mainloop()

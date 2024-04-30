#import
#todo eventuelt import csv fil
import tkinter as tk
from tkinter import messagebox, simpledialog

#todo def LevelSystem
#If AmountOfPoints>MaxPoint
#Level up
#Show AmountOfPoints

#todo class menu
# def StartQuiz
# def ChooseTopic
# def Quit
# input, if user presses: 1, 2 or 3
# 1: StartQuiz
# 2: ChooseTopic
# 3: Quit


#todo StartQuiz


#todo ChooseTopic
# have en csv fil med forskellige emner, delt op

#todo Quit
# Quit("Program ended. Cya, biatch!")
# mangler eventuelt tkinter commands
#hjkghjvivy
#add 1 point




class QuizMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Menu")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Velkommen til denne quiz", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz_window)
        self.start_button.pack(pady=5)

        self.highscores_button = tk.Button(root, text="View Highscores", command=self.view_highscores)
        self.highscores_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def start_quiz_window(self):
        self.quiz_questions = [
            {"question": "When was the first known use of the word 'quiz'?", "options": ["1778", "1781", "1790", "1802"], "answer": "1781"},
            {"question": "Which built-in function can get information from the user?", "options": ["input", "print", "int", "str"], "answer": "input"}
        ]

        self.ask_question(self.quiz_questions)

    def ask_question(self, questions):
        for idx, question in enumerate(questions, start=1):
            user_answer = simpledialog.askstring(f"Question {idx}", f"{question['question']}\n\nOptions: {', '.join(question['options'])}\n\nChoose an option:")
            if user_answer == question['answer']:
                messagebox.showinfo("Result", "Correct!")
            else:
                messagebox.showinfo("Result", f"Incorrect. The correct answer is '{question['answer']}'")

    def view_highscores(self):
        messagebox.showinfo("Highscores", "View Highscores!")
        print("Viewing highscores...")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizMenu(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class QuizMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Menu")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Welcome to the Quiz Menu", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz_window)
        self.start_button.pack(pady=5)

        self.highscores_button = tk.Button(root, text="View Highscores", command=self.view_highscores_window)
        self.highscores_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def start_quiz_window(self):
        messagebox.showinfo("Quiz", "Quiz Started!")
        # Add code to start the quiz window here

    def view_highscores_window(self):
        highscores_window = tk.Toplevel(self.root)
        highscores_window.title("Highscores")
        highscores_window.geometry("200x150")

        highscores_label = tk.Label(highscores_window, text="Highscores", font=("Helvetica", 16))
        highscores_label.pack(pady=10)

        # Display sample highscores
        highscores = [
            "1. John - 100",
            "2. Alice - 90",
            "3. Bob - 85",
            "4. Sarah - 80",
            "5. Emma - 75"
        ]
        for score in highscores:
            score_label = tk.Label(highscores_window, text=score)
            score_label.pack()

        highscores_close_button = tk.Button(highscores_window, text="Close", command=highscores_window.destroy)
        highscores_close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizMenu(root)
    root.mainloop()

# Name: Ranithu Dinsara
# Student Number: 10635536
# This file is provided to you as a starting point for the "wyr.py" program of the Project
# of Programming Principles in Semester 2, 2023. It aims to give you just enough code to help ensure
# that your program is well structured. Please use this file as the basis for your assignment work.
# You are not required to reference it.
# The "pass" command tells Python to do nothing. It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program. Replace them with your own code as you complete the assignment.

# Import the required modules.
import json
import tkinter as tk
from tkinter import messagebox

class ProgramGUI:
    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of wyr.py" section of the assignment brief.
        try:
            with open("data.txt", "r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Missing/Invalid file")
            return
        
        self.question_num = 0
        self.over_12 = messagebox.askyesno("Age Confirmation", "Are you over the age of 12?")
        
        self.main = tk.Tk()
        self.main.title("Would You Rather!!!")
        self.main.geometry("400x200")
        
        self.show_question()
        self.main.mainloop()

    def show_question(self):
        # This method is responsible for displaying the current question's options in the GUI and ending the program.
        # See Point 1 of the "Methods in the GUI class of wyr.py" section of the assignment brief.
        try:
            current_question = self.data[self.question_num]
        except IndexError:
            messagebox.showinfo("End of Questions", "No more questions available.")
            self.main.destroy()
            return
        
        if not current_question["children"] and not self.over_12:
            self.question_num += 1
            self.show_question()
        else:
            top_question = "Would you rather..."
            option_1 = current_question["option_1"] + "?"
            option_2 = current_question["option_2"] + "?"
            
            for window in self.main.winfo_children():
                window.destroy()
            
            prompt_label = tk.Label(self.main, text=top_question, font=("Arial", 12, "bold"), pady=10)
            prompt_label.pack()
            
            button_1 = tk.Button(self.main, text=option_1, width=30, height=2, bg="#c0ffb9", command=lambda: self.record_vote("votes_1"))
            button_1.pack()
            
            button_2 = tk.Button(self.main, text=option_2, width=30, height=2, bg="#c0ffb9", command=lambda: self.record_vote("votes_2"))
            button_2.pack()

    def record_vote(self, vote):
        # This method is responsible for recording the user's choice when they select an option of a question.
        # See Point 2 of the "Methods in the GUI class of wyr.py" section of the assignment brief.
        current_question = self.data[self.question_num]
        
        if vote not in current_question:
            current_question[vote] = 0
        
        current_question[vote] += 1
        
        liked = messagebox.askyesno("Question Feedback", "Did you like the question?")
        
        if "likes" not in current_question:
            current_question["likes"] = 0
        if "dislikes" not in current_question:
            current_question["dislikes"] = 0
        
        if liked:
            current_question["likes"] += 1
        else:
            current_question["dislikes"] += 1
        
        self.save_data()
        self.question_num += 1
        self.show_question()

    def save_data(self):
        with open("user_data.txt", "w") as file:
            json.dump(self.data, file, indent=4)

# Create an instance of ProgramGUI
if __name__ == "__main__":
    gui = ProgramGUI()

import tkinter as tk
from tkinter import *
from student import Student
from tkinter import messagebox as msb

class StudentProgram:
    def __init__(self, master):
        self.window = tk.Tk()
        self.window.geometry('500x600')
        self.window.title('Student Manager')
        
        self.students = []
        self.curr = -1
        
        # Create labels
        self.lbl_id = Label(self.window, text='Id')
        self.lbl_id.grid(column=0, row=0)
        self.lbl_name = Label(self.window, text="Name")
        self.lbl_name.grid(column=1, row=0)
        self.lbl_grade = Label(self.window, text='Grade')
        

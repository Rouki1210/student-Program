import tkinter as tk
from tkinter import *
from student import Student
from tkinter import messagebox as msb

class StudentProgram:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x400')
        self.window.title('Student Manager')
        
        self.students = []
        self.curr = -1
        
        # Create labels
        self.lbl_id = Label(self.window, text='Id')
        self.lbl_id.grid(column=0, row=0)
        self.lbl_name = Label(self.window, text="Name")
        self.lbl_name.grid(column=0, row=1)
        self.lbl_grade = Label(self.window, text='Grade')
        self.lbl_grade.grid(row=2, column=0)   
        
        # Create entries
        self.txt_id = Entry(self.window)
        self.txt_id.grid(column=1, row=0, columnspan=4)
        self.txt_name = Entry(self.window)
        self.txt_name.grid(row=1, column=1, columnspan=4)
        self.txt_grade =  Entry(self.window)
        self.txt_grade.grid(row=2, column=1, columnspan=4)
        
        # Create browser buttons
        self.btn_first = Button(self.window, text='|<', command=self.btn_first_clicked)
        self.btn_first.grid(row=3, column=1)
        self.btn_prev = Button(self.window, text='<', command=self.btn_prev_clicked)
        self.btn_prev.grid(row=3, column=2)
        self.btn_next = Button(self.window, text='>', command=self.btn_next_clicked)
        self.btn_next.grid(row=3, column=3)
        self.btn_last = Button(self.window, text='>|', command=self.btn_last_clicked)
        self.btn_last.grid(row=3, column=4)
        
        # create action buttons
        self.btn_add = Button(self.window, text='Add', command=self.btn_add_clicked)
        self.btn_add.grid(row=4, column=1, columnspan=2)
        self.btn_delete = Button(self.window, text='Delete', command=self.btn_delete_clicked)
        self.btn_delete.grid(row=4, column=3, columnspan=2)
        self.btn_update = Button(self.window, text='Update', command=self.btn_update_clicked)
        self.btn_update.grid(row=5, column=1, columnspan=4)
    
    def btn_prev_clicked(self):
        if self.curr == 0:
            msb.showwarning('Previous Student', 'Already first student!')
            return
        
        self.curr -= 1
        self.show_student()
    
    def btn_next_clicked(self):
        if self.curr == len(self.students) - 1:
            msb.showwarning('Next Student', 'Already last student!')
            return
        
        self.curr += 1
        self.show_student()
    
    def btn_first_clicked(self):
        self.curr = 0
        self.show_student()
    
    def btn_last_clicked(self):
        self.curr = len(self.students) - 1
        self.show_student()

    def show_student(self):
        # show current student on text boxes
        curr_student = self.students[self.curr]
        name = curr_student.name
        id = curr_student.id
        grade = curr_student.grade
        self.txt_id.delete(0, END)
        self.txt_id.insert(0, str(id))
        self.txt_name.delete(0, END)
        self.txt_name.insert(0, name)
        self.txt_grade.delete(0, END)
        self.txt_grade.insert(0, str(grade))
    
    def btn_add_clicked(self):
        id = self.txt_id.get()
        name = self.txt_name.get()
        grade = self.txt_grade.get()
        student = Student(id, name, grade)
        self.students.append(student)
        msb.showinfo('Add Student', 'Student added successfully')
    
    def btn_delete_clicked(self):
        self.students.pop(self.curr)
        msb.showinfo('Delete Student', 'Delete successfully')
    
    def btn_update_clicked(self):
        name = self.txt_name.get()
        grade = self.txt_grade.get()

        self.students[self.curr].name = name
        self.students[self.curr].grade = grade
        msb.showinfo('Update Student', 'Update successfully') 

    def run(self):
        self.window.mainloop()

### main ###
program = StudentProgram()
program.run()
        

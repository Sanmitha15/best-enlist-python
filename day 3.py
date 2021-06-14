#importing library
from tkinter import *
from tkinter import ttk

window =Tk()
window.title("Registration Screen")
window.geometry('500x500')
#Decaring window color
window.configure(background = "blue");
#below four fields are declared

Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
Lastname = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 2,column = 0)
Mobile = Label(window ,text = "contact Number").grid(row = 3,column = 0)
Employeeid = Label(window ,text = "Employee id").grid(row = 4,column = 0)
Employeeage = Label(window ,text = "Employee age").grid(row = 5,column = 0)
Hobbies = Label(window ,text = "Hobbies").grid(row = 6,column = 0)
Technicalskill = Label(window ,text = "Technical skill").grid(row=7,column=0)
Linkedinid = Label(window ,text = "Linkedin id").grid(row=8,column=0)
HighestQualification = Label(window ,text = "Highest qualification").grid(row=9,column=0)
list1=['Degree','PUC','10th'];
c=StringVar()
droplist =OptionMenu(window,c, *list1)
c.set('select your qualification')
droplist.grid(row=9,column=1)
Gender = Label(window ,text = "Gender").grid(row=11,column=0)
var = IntVar()
Radiobutton(window ,text="Male",padx=30,variable=var,value=1).grid(row=11,column=1)
Radiobutton(window ,text="Female",padx=20,variable=var,value=2).grid(row=11,column=2)

               
Firstname1=Entry(window).grid(row=0,column=1)
lastname1=Entry(window).grid(row=1,column=1)
Email1=Entry(window).grid(row=2,column=1)
Mobile1=Entry(window).grid(row=3,column=1)
Employeeid=Entry(window).grid(row=4,column=1)
Employeeage=Entry(window).grid(row=5,column=1)
Hobbies=Entry(window).grid(row=6,column=1)
Technicalskill=Entry(window).grid(row=7,column=1)
Linkedinid=Entry(window).grid(row=8,column=1)

variable=IntVar()
Checkbutton(window,text="I accept all the terms and condition",variable=variable).grid(row=12,column=0)


#function declaration             
def clicked():
               res = "Welcome to" + txt.get()
               lbl.configure(text= res)
btn = ttk.Button(window, text="Submit").grid(row=15,column=1)
window.mainloop()
        
        
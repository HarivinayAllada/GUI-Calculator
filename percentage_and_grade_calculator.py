# importing all modules from tkinter library
from tkinter import *

# to create a window
window = Tk()

# Title of window
window.title("Percentage and Grade calculator")

# size of window
window.geometry("500x600")

# calculation part
def calculate():
    telugu = int(telugu_entry.get())
    hindi = int(hindi_entry.get())
    english = int(english_entry.get())
    mathematics = int(mathematics_entry.get())
    general_science = int(general_science_entry.get())
    social_studies = int(social_studies_entry.get())

    # calculating total from all subjects
    # and placing the total label in window
    total = (telugu+hindi+english+mathematics+general_science+social_studies)
    Label(text=f"{total}/600",font=("arial",15,"bold"),fg="#1551e8").place(x=250,y=280)

    # calculating the percentage of all subjects
    # and placing the percentage label in window
    percentage = int((total/600)*100)
    Label(text=f"{percentage}",font=("arial",15,"bold"),fg="#1551e8").place(x=250,y=330)

    # creating a grade label and placing it in window
    # if percentage or any subject is less than 35 then it shows FAIL
    # else it shows PASS
    if percentage<35 or telugu<35 or hindi<35 or english<35 or mathematics<35 or general_science<35 or social_studies<35:
        grade = "FAIL"
    else:
        grade = "PASS"

    Label(text=f"{grade}",font=("arial",15,"bold"),fg="#1551e8").place(x=250,y=380)

# creating different labels for different subjects in window
# and placing  subject labels in window
subject1 = Label(window,text="Telugu :",font=("arial",10,"bold"))
subject1.place(x=50,y=30)
sub1 = Label(window,text="out of 100",font=("arial",10))
sub1.place(x=330,y=30)

subject2 = Label(window,text="Hindi :",font=("arial",10,"bold"))
subject2.place(x=50,y=70)
sub2 = Label(window,text="out of 100",font=("arial",10))
sub2.place(x=330,y=70)

subject3 = Label(window,text="English :",font=("arial",10,"bold"))
subject3.place(x=50,y=110)
sub3 = Label(window,text="out of 100",font=("arial",10))
sub3.place(x=330,y=110)

subject4 = Label(window,text="Mathematics :",font=("arial",10,"bold"))
subject4.place(x=50,y=150)
sub4 = Label(window,text="out of 100",font=("arial",10))
sub4.place(x=330,y=150)

subject5 = Label(window,text="General Science :",font=("arial",10,"bold"))
subject5.place(x=50,y=190)
sub5 = Label(window,text="out of 100",font=("arial",10))
sub5.place(x=330,y=190)

subject6 = Label(window,text="Social Studies :",font=("arial",10,"bold"))
subject6.place(x=50,y=230)
sub6 = Label(window,text="out of 100",font=("arial",10))
sub6.place(x=330,y=230)

# creating a total label in window
# placing percentage label in window
total = Label(window,text="Total :",font=("arial",13,"bold"))
total.place(x=50,y=280)

# creating a percentage label in window
# placing percentage label in window
percentage = Label(window,text="Percentage :",font=("arial",13,"bold"))
percentage.place(x=50,y=330)

# creating grade label in window for different subjects
# placing grade label in window
grade = Label(window,text="Grade :",font=("arial",13,"bold"))
grade.place(x=50,y=380)

telugu_value = StringVar()
hindi_value = StringVar()
english_value = StringVar()
mathematics_value = StringVar()
general_science_value = StringVar()
social_studies_value = StringVar()

# creating entry labels in window for different subjects
# placing entry labels in window
telugu_entry = Entry(window,textvariable=telugu_value,font=("arial",15),bg="#d8f2da",width=5)
telugu_entry.place(x=250,y=30)

hindi_entry = Entry(window,textvariable=hindi_value,font=("arial",15),bg="#d8f2da",width=5)
hindi_entry.place(x=250,y=70)

english_entry = Entry(window,textvariable=english_value,font=("arial",15),bg="#d8f2da",width=5)
english_entry.place(x=250,y=110)

mathematics_entry = Entry(window,textvariable=mathematics_value,font=("arial",15),bg="#d8f2da",width=5)
mathematics_entry.place(x=250,y=150)

general_science_entry = Entry(window,textvariable=general_science_value,font=("arial",15),bg="#d8f2da",width=5)
general_science_entry.place(x=250,y=190)

social_studies_entry = Entry(window,textvariable=social_studies_value,font=("arial",15),bg="#d8f2da",width=5)
social_studies_entry.place(x=250,y=230)

# creating a Calculate button in window
# placing a calculate button in window
button = Button(text="Calculate",font=("times new roman",15),bg="grey",bd=5,command=calculate)
button.place(x=200,y=450)




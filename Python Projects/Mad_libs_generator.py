from tkinter import Tk, Label, Button
screen = Tk()

screen.title("PythonGeeks Mad Lib Generator")
screen.geometry('400x400')
screen.config(bg='pink')
Label(screen,text='PythonGeeks Mad Libs Generator').place(x=100,y=20)

story1button= Button(screen,text='A momorable day',font= ('Times New Roman', 13),command=lambda:story1(screen),bg='Blue')
story1button.place(x=140,y=90)

story2button= Button(screen,text='Ambitions',font= ('Times New Roman', 13),command=lambda:story2(screen),bg='Blue')
story2button.place(x=150,y=150)

screen.update()
screen.mainloop()
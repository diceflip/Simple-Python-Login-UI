from tkinter import *

window = Tk()
window.geometry('550x450')
window.configure(bg="black")
window.title("Dice Simple Login UI")

loggedin = 0

icon = PhotoImage(file="DiceFliplogonobg.png")

window.iconphoto(True, icon)

heading = Label(window, text = "Please Login", fg = "#00FF00", bg = "black", font=("Arial", 40, 'bold', 'underline'))
heading.pack()

entrybox = Entry(window, font=("Arial", 30))
entrybox.pack(pady = 20)

button_frame = Frame(window, bg="black")
button_frame.pack(pady=30)

def submit():
    user_input = entrybox.get()
    if not user_input:
        information.configure(text="Please input your name to login!")
    else:
        information.configure(text="You have been logged in as " + user_input + "!")
        global loggedin
        loggedin = 1

def logout():

    global loggedin

    if loggedin == 0:
        information.configure(text="First login u idiot!")
    else:

        information.configure(text="You have been logged out!")
        entrybox.delete(0, END)

        loggedin = 0

submit_button = Button(button_frame, text = "submit", font=("Arial", 20), command=submit)
submit_button.pack(side="left")
logout_button = Button(button_frame, text = "logout", font=("Arial", 20), command=logout)
logout_button.pack(side="left")
information = Label(window, text = "", bg="black",fg= "red", font=("Arial", 20, 'bold') )
information.pack(pady=50)

window.mainloop()

from tkinter import * 
from tkinter import messagebox, ttk
import json


icons = {

            "main" : "icons/cloud_password.ico",
            "search" : "icons/serch.ico",
            "password" : "icons/password_security_icon_154431.ico",
            "error" : "icons/cloud_password.ico",
            "remouve":"icons/removetheuser_elimina_3541.ico"

    }

symbols = (

            ",", "!", "@", "#", "$", "%", "^", "&", "*","-","_",
            "=", "+", "/", "?", ">", ".", "<", ";",":", "\"","\'",
            "\\","[", "]", "(", ")","{", "}", "|", "`", "~"       
    )

def get_passwords() -> list:
    try:
        with open("Passwords.json", "r") as file:
            passwords = json.load(file)
    except():
        passwords = []
    return passwords


def update_passwords(new_list_of_passwords:list):
    with open("Passwords.json", "w") as passwrds_file:
        json.dump(new_list_of_passwords, passwrds_file, indent=4)

    
        

# -----------------------------------------------------------
def missing(error:str):

    if type(error) == str:
        messagebox.showerror("problem", error)
    
    else:
        missing("error from input type")


# -------------------------------------------------------------
def font(size:int, font_wight="bold") -> tuple:
    if type(size) != int:
        try:
            size = int(size)

        except ValueError:
            missing("size font type error")

    if type(size) == int:
            
        if type(font_wight) == str:
            if font_wight in ("bold", "italic", "normal"):
                return ("Helvetica", size, font_wight)
            
            elif font_wight[0:3] == "bold":
                if font_wight[5:9] == "italic":
                    return ("Helvetica", size, font_wight)
                else: missing(f"{font_wight[5:-1]} is not define")
                 
            else:
                missing("font wight not define")
        else:
            missing("font wight not str")


# --------------------------------------add password-------------------------------------------
def add_password():
    
    win = Tk()
    result = None
    win.title("Add a password")
    win.geometry('400x200')
    win.iconbitmap(icons["password"])
    win.resizable(False, False)


    user_name_label = Label(win, font=font(10), text='User name:')
    user_name_label.grid(row=0, column=0)

    user_name_entry = Entry(win, width=50, font=font(10))
    user_name_entry.grid(row=0, column=1)

    app_of_password_label = Label(win, font=font(10), text='App of password:')
    app_of_password_label.grid(row=1, column=0)

    app_of_password = Entry(win, width=50, font=font(10))
    app_of_password.grid(row=1, column=1)

    password_label = Label(win, font=font(10), text='Password:')
    password_label.grid(row=2, column=0)

    password_entry = Entry(win, width=50, font=font(10))
    password_entry.grid(row=2, column=1)

    def access():
        # All Problems of input
        if (not user_name_entry.get()) and (not app_of_password.get()) and (not password_entry.get()): 
            missing('No Informations')
        
        elif (
                (not user_name_entry.get()) 
                or (not app_of_password.get()) 
                or (not password_entry.get())
            ): 

            if not user_name_entry.get():
                missing('No User name')

            elif not app_of_password.get():
                missing('No App of this Password')

            elif not password_entry.get():
                missing('No Password')

        # Password Problems
        elif (
                (len(password_entry.get()) <= 8)
                or (password_entry.get().isspace())
                or (not any(char.isnumeric() for char in password_entry.get()))
                or (password_entry.get().islower()) or (password_entry.get().isupper())
                or (not any((char in symbols for char in password_entry.get())))
                
            ):
            
            if password_entry.get().isspace():
                missing("No Password")

            elif len(password_entry.get()) <= 8:
                # missing("Weak Password")
                missing("Weak password, Password should be longest")

            elif not any((char.isnumeric() for char in password_entry.get())):
                missing("Weak password, Password should continu sam numbers")

            elif password_entry.get().islower():
                missing("Weak password, Password should continu sam capital leterses")
            
            elif password_entry.get().isupper():
                missing("Weak password, Password should continu sam small leterses")
            else:
                missing("Weak password, Password should continu sam symbols")
        # User name Problems
        elif(
                (not user_name_entry.get().istitle()) 
                or (user_name_entry.get().count(" ") < 1 or user_name_entry.get().count(" ") > 8 )
                or (any((char in symbols for char in user_name_entry.get())))
        
            ):

            if not user_name_entry.get().istitle():
                missing("User name error, all words should be capital in the front")

            elif user_name_entry.get().count(" ") < 1 or user_name_entry.get().count(" ") >= 8:
                if user_name_entry.get().count(" ") < 1:
                    missing("User name error, No completed name (missing fathers names)")
                
                elif user_name_entry.get().count(" ") >= 8:
                    missing("User name error, spaces problems")       

            else:
                missing("User name error, cannot add symbols")
                
        # App of password Problems
        elif(
                (not app_of_password.get().istitle())
                or (any((char in symbols for char in app_of_password.get()))) 
                or (user_name_entry.get().isupper())
            ):
            
            if not app_of_password.get().istitle():
                missing("App of password error, the first letter should be capital")
            
            elif any((char in symbols for char in app_of_password.get())):
                missing("App of password error, can't using any symbol")

            elif app_of_password.get().isupper():
                missing("App of password error, all of letters App of password can't be capital")


        else: 
            
            nonlocal result
            result = (app_of_password.get(), password_entry.get(), user_name_entry.get())
            return True
        
    # command of Buttons
    def finish():
        if access():
            win.destroy()

    def clear():
        user_name_entry.delete(0, END)
        password_entry.delete(0, END)
        app_of_password.delete(0, END)
        

    return_button = Button(win, text="Finish", font=font(10), bg="green", command= finish, width=10)
    return_button.place(x=280, y=140)

    Button(win, command=clear, text="clear all", font=font(10), background="red4", width=10).place(x=35, y=140)


    win.mainloop()
    return result if result else "error"
...

# return the form tuple -> ((app_of_password.get(), password_entry.get(), user_name_entry.get()))

# add_password()

# --------------------------------------- serch ---------------------------------------

def search():
    
    passwords = get_passwords()
    if passwords == []:
        missing("No Passwords")
        
    else:
        win = Tk()
        win.title("serche for a password")
        win.geometry('400x200')
        win.iconbitmap(icons["search"])
        win.resizable(False, False)

        def squert(title:str, button:Button):


            def show_results():
                introdiction.destroy()
                serch_app.destroy()
                serch_name.destroy()
                serched.destroy()
                cadre = LabelFrame(
                        win,
                        text=f" {title} ", 
                        font=font(7),
                        padx=10, pady=10,
                        relief="groove",
                        width=400, height=200
                    )
                
                cadre.pack()
                scrollbar = Scrollbar(cadre)
                scrollbar.pack(side = RIGHT, fill =Y)
                
                result =  Text(
                        cadre, 
                        yscrollcommand = scrollbar.set,
                        wrap = "word",
                        font = font(10, "bold italic"),
                        bd = 1,
                        highlightthickness = 0,
                        width = 50, height = 9
                    )
                result.pack()
                scrollbar.config(command = result.yview)
                result.insert(END, continu)
                result.config(state="disabled")
                Button(win, text = "OK", command = win.destroy, font = font(10), bg = "green").pack(side = "bottom")
            if serched.get():
                continu = ""

                if button is serch_name:
                    
                    for index in passwords:
                        if index["user_name"] == serched.get():
                            continu += f"{index["password"]}\n"
                    
                    if continu == "": missing("invalid user name")

                    else: show_results()
                    

                else:
                        for index in passwords:
                            if index["application"] == serched.get():
                                continu += f"\n{index["password"]}\n"

                        if not continu : missing("No any application use the serched password")

                        else: show_results()
                            
            
            else:
                missing("No element to serch")


            # if not serched.get() in passwords[]


        def serch_with_user_name():
            squert("passwords found by user name", serch_name)
        

        
        def sersh_with_app_name():
            squert("passwords found by app", serch_app)    


        introdiction = Label(win, text="serch with user name or app name", font=font(10))
        introdiction.pack()

        serched = Entry(win, width=61, font=font(10))
        serched.pack()
        
        serch_name = Button(win, text="serch with user name", font=font(10), command=serch_with_user_name, bg="yellow")
        serch_name.place(x=5, y=170)
        serch_app = Button(win, text="sersh with app name", font=font(10), command=sersh_with_app_name, bg="yellow")
        serch_app.place(x=250, y=170)
        win.mainloop()
        



def remouve():
    passwords = get_passwords()
    if passwords == []:
        missing("No Passwords")

    elif len(passwords) == 1:
            passwords.pop(0)
            messagebox.showinfo(title="Remouve Password", message='One password is remouved')

    else:
        def finish():
            if not combo.get():
                missing("No Password Sellcted")
            
            else:
                for i, dct in enumerate(passwords, 0):
                    if dct['password'] == combo.get():
                        passwords.pop(i)
                update_passwords(passwords)
                missing("Password remouved successfully")
                win.after(1000, win.destroy())


        def remouve_all():
            if messagebox.askyesnocancel("", "Do you want sure to remouve all passwords"):
                update_passwords([])
                win.after(1000, win.destroy())

        win = Tk()
        win.title("Remouve Password")
        win.geometry('400x200')
        win.iconbitmap(icons["remouve"])
        win.resizable(False, False)

        combo = ttk.Combobox(win, value=(tuple(app["password"] for app in passwords)), state="readonly", font=font(10))
        combo.pack()

        Button(win, text="  Remove Password  ", font=font(10), command=finish).place(x=20, y=160)
        Button(win, text="Remove All Passwords", font=font(10), command=remouve_all).place(x=230, y=160)
        Button(win, text="Cancel", font=font(10), command=win.destroy).place(x=170, y=160)


        win.mainloop()

# remouve()
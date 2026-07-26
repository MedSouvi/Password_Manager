from tkinter import * 
from tkinter import messagebox, ttk
import json
# -----------------------------------------------------------     
# type

icons = {

            "main" : "icons/cloud_password.ico",
            "search" : "icons/serch.ico",
            "password" : "icons/password_security_icon_154431.ico",
            "error" : "icons/cloud_password.ico",
            "remove":"icons/removetheuser_elimina_3541.ico"

    }
# -----------------------------------------------------------     


symbols = (

            ",", "!", "@", "#", "$", "%", "^", "&", "*", "-", "_",
            "=", "+", "/", "?", ">", ".", "<", ";", ":", "\"", "\'",
            "\\","[", "]", "(", ")","{", "}", "|", "`", "~", "¥", 
            "€", "£", "→", "←", "²", "❁", "©", "°", "•"
    )
# -----------------------------------------------------------     


def get_passwords() -> list:
    try:
        with open("Passwords.json", "r") as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = []
    return passwords
# -----------------------------------------------------------     


def update_passwords(new_list_of_passwords:list):
    with open("Passwords.json", "w") as passwrds_file:
        json.dump(new_list_of_passwords, passwrds_file, indent=4)    
# -----------------------------------------------------------

def show_error(error:str):
    messagebox.showerror("problem", error)
# -------------------------------------------------------------


def font(size:int, font_weight="bold") -> tuple:
    if not isinstance(size, int):
        try:
            size = int(size)

        except ValueError:
            show_error("size font type error")

    if isinstance(size, int):
    
        if  isinstance(font_weight, str):
            if font_weight in ("bold", "italic", "normal"):
                return ("Helvetica", size, font_weight)
            
            elif font_weight[0:3] == "bold":
                if font_weight[5:9] == "italic":
                    return ("Helvetica", size, font_weight)
                
                else: show_error(f"{font_weight[5:-1]} is not define")
                 
            else:
                show_error("font wight not define")
        else:
            show_error("font wight not str")


# --------------------------------------add password-------------------------------------------
def open_add_password_window(window:Tk):
    
    win = Toplevel(window)
    result = None
    win.title("Add a password")
    win.geometry('400x200')
    win.iconbitmap(icons["password"])
    win.resizable(False, False)

    Label(win, font=font(10), text='User name:').grid(row=0, column=0)

    user_name_entry = Entry(win, width=50, font=font(10))
    user_name_entry.grid(row=0, column=1)

    Label(win, font=font(10), text='App of password:').grid(row=1, column=0)

    application_entry = Entry(win, width=50, font=font(10))
    application_entry.grid(row=1, column=1)

    Label(win, font=font(10), text='Password:').grid(row=2, column=0)

    password_entry = Entry(win, width=50, font=font(10))
    password_entry.grid(row=2, column=1)

    def validate_password_data():

        # All Problems of input
        if (not user_name_entry.get()) and (not application_entry.get()) and (not password_entry.get()): 
            show_error('No Informations')
        
        elif (
                (not user_name_entry.get()) 
                or (not application_entry.get()) 
                or (not password_entry.get())
            ): 

            if not user_name_entry.get():
                show_error('No User name')

            elif not application_entry.get():
                show_error('No App of this Password')

            elif not password_entry.get():
                show_error('No Password')

        # Password Problems
        elif (
                (len(password_entry.get()) <= 8)
                or (password_entry.get().isspace())
                or (not any(char.isnumeric() for char in password_entry.get()))
                or (password_entry.get().islower()) or (password_entry.get().isupper())
                or (not any((char in symbols for char in password_entry.get())))
                
            ):
            
            if password_entry.get().isspace():
                show_error("No Password")

            elif len(password_entry.get()) <= 8:
                # missing("Weak Password")
                show_error("Weak password, Password should be longest")

            elif not any((char.isnumeric() for char in password_entry.get())):
                show_error("Weak password, Password should continu sam numbers")

            elif password_entry.get().islower():
                show_error("Weak password, Password should continu sam capital leterses")
            
            elif password_entry.get().isupper():
                show_error("Weak password, Password should continu sam small leterses")
            else:
                show_error("Weak password, Password should continu sam symbols")

        # User name Problems
        elif(
                (not user_name_entry.get().istitle()) 
                or (user_name_entry.get().count(" ") < 1 or user_name_entry.get().count(" ") > 8 )
                or (any((char in symbols for char in user_name_entry.get())))
        
            ):

            if not user_name_entry.get().istitle():
                show_error("User name error, all words should be capital in the front")

            elif user_name_entry.get().count(" ") < 1 or user_name_entry.get().count(" ") >= 8:
                if user_name_entry.get().count(" ") < 1:
                    show_error("User name error, No completed name (missing fathers names)")
                
                elif user_name_entry.get().count(" ") >= 8:
                    show_error("User name error, spaces problems")       

            else:
                show_error("User name error, cannot add symbols")
                
        # App of password Problems
        elif(
                (not application_entry.get().istitle())
                or (any((char in symbols for char in application_entry.get()))) 
                or (user_name_entry.get().isupper())
            ):
            
            if not application_entry.get().istitle():
                show_error("App of password error, the first letter should be capital")
            
            elif any((char in symbols for char in application_entry.get())):
                show_error("App of password error, can't using any symbol")

            elif application_entry.get().isupper():
                show_error("App of password error, all of letters App of password can't be capital")


        else: 
            
            nonlocal result
            result = (application_entry.get(), password_entry.get(), user_name_entry.get())
            return True
        
    # command of Buttons
    def submit_password():
        if validate_password_data():
            win.destroy()
            
        

    def clear_all():
        user_name_entry.delete(0, END)
        password_entry.delete(0, END)
        application_entry.delete(0, END)
        

    submit_button = Button(win, text="Finish", font=font(10), bg="green", command= submit_password, width=10)
    submit_button.place(x=280, y=140)

    Button(win, command=clear_all, text="clear all", font=font(10), background="red4", width=10).place(x=35, y=140)
    win.wait_window()
    return result if result else "error"


# return_button
...

# return the form tuple -> ((app_of_password.get(), password_entry.get(), user_name_entry.get()))

# add_password()

# --------------------------------------- serch ---------------------------------------

def search(window:Tk):

    global passwords
    passwords = get_passwords()

    if not passwords:
        show_error("No Passwords")
        
    else:
        win = Toplevel(window)
        win.title("serche for a password")
        win.geometry('400x200')
        win.iconbitmap(icons["search"])
        win.resizable(False, False)

        def search_query(title:str, button:Button):


            def show_results():
                introdiction.destroy()
                serch_app.destroy()
                serch_name.destroy()
                search_entry.destroy()
                
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

            if search_entry.get():
                continu = ""

                if button is serch_name:
                    
                    for index in passwords:
                        if index["user_name"].lower() == search_entry.get().lower():
                            continu += f"{index["password"]}\n"
                    
                    if continu == "": show_error("invalid user name")

                    else: show_results()
                    

                else:
                        for index in passwords:
                            if index["application"].lower() == search_entry.get().lower():
                                continu += f"\n{index["password"]}\n"

                        if not continu : show_error("No any application use the serched password")

                        else: show_results()
                            
            
            else:
                show_error("No element to serch")


            # if not serched.get() in passwords[]


        def serch_with_user_name():
            search_query("passwords found by user name", serch_name)
        

        
        def sersh_with_app_name():
            search_query("passwords found by app", serch_app)    


        introdiction = Label(win, text="serch with user name or app name", font=font(10))
        introdiction.pack()

        search_entry = Entry(win, width=61, font=font(10))
        search_entry.pack()
        
        serch_name = Button(win, text="serch with user name", font=font(10), command=serch_with_user_name, bg="yellow")
        serch_name.place(x=5, y=170)
        serch_app = Button(win, text="sersh with app name", font=font(10), command=sersh_with_app_name, bg="yellow")
        serch_app.place(x=250, y=170)
        
        

# serched

def remouve(window:Tk):
    global passwords
    passwords = get_passwords()
    if passwords == []:
        show_error("No Passwords")

    elif len(passwords) == 1:
            passwords.pop(0)
            update_passwords(passwords)
            messagebox.showinfo(title="Remouve Password", message='One password is remouved')

    else:
        def finish():
            if not combo.get():
                show_error("No Password Sellcted")
            
            else:
                for i, dct in enumerate(passwords, 0):
                    if f"{dct["application"]} - {dct['user_name']}" == combo.get():
                        passwords.pop(i)
                        break

                update_passwords(passwords)
                show_error("Password remouved successfully")
                win.after(1000, win.destroy())


        def remouve_all():
            if messagebox.askyesnocancel("", "Do you want sure to remouve all passwords"):
                update_passwords([])
                win.after(1000, win.destroy())

        win = Toplevel(window)
        win.title("Remouve Password")
        win.geometry('400x200')
        win.iconbitmap(icons["remove"])
        win.resizable(False, False)

        combo = ttk.Combobox(win, value=(tuple(f"{app["application"]} - {app["user_name"]}" for app in passwords)), state="readonly", font=font(10), height=10)
        combo.pack()

        Button(win, text="  Remove Password  ", font=font(10), command=finish).place(x=20, y=160)
        Button(win, text="Remove All Passwords", font=font(10), command=remouve_all).place(x=230, y=160)
        Button(win, text="Cancel", font=font(10), command=win.destroy).place(x=170, y=160)


        

# remouve()
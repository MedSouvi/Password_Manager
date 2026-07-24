import control
if __name__ == "__main__":
    from tkinter import *

    root = Tk()
    root.title("Password Manager")
    root.geometry('400x350')
    root.iconbitmap(control.icons["main"])
    root.resizable(False, False)


    class Password:
        def __init__(self, value:str, user_name:str, application:str):
            self.password = value
            self.user_name = user_name
            self.application = application
        
        def save(self):   
            passwords = control.get_passwords()
            control.update_passwords(passwords + [self.__dict__])
            

    def add_password():
        # return the form tuple -> ((app_of_password.get(), password_entry.get(), user_name_entry.get()))
        info = control.add_password()
        
        if info == "error":
            control.missing("error")
        
        else:
            global password
            app    = info[0]
            pass_word = info[1]
            user_name = info[2]
            
            password = Password(pass_word, user_name, app)
            password.save()


    Label(root, text="Welcome to the password managere\n", font=control.font(10)).pack()#introdiction

    Button(root, text="Add Password", command=add_password, font=control.font(10)).pack()

    # Label(root, text="Search For Password", font=control.font(10))
    Button(root, text="Search For Password", command=control.search, font=control.font(10)).pack()
    Button(root, text="Remouve Password", command=control.remouve, font=control.font(10)).pack()
    root.mainloop()

else:
    control.missing('Error. can\'t run the app')

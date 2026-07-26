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
            control.update_passwords(control.get_passwords() + [self.__dict__])
            

    def add_password():
        # return the form tuple -> ((app_of_password.get(), password_entry.get(), user_name_entry.get()))
        info = control.open_add_password_window(window=root)
        
        if info == "error":
            control.show_error("error")
        
        else:
            app = info[0]
            pass_word = info[1]
            user_name = info[2]
            
            Password(pass_word, user_name, app).save()


    Label(root, text="Welcome to the password managere\n", font=control.font(10)).pack()#introdiction

    Button(root, text="Add Password", command=add_password, font=control.font(10)).pack()

    # Label(root, text="Search For Password", font=control.font(10))
    Button(root, text="Search For Password", command=lambda:control.search(window=root), font=control.font(10)).pack()
    Button(root, text="Remouve Password", command=lambda:control.remouve(window=root), font=control.font(10)).pack()
    root.mainloop()

else:
    control.show_error('Error. can\'t run the app')

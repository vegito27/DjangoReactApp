from tkinter import*

root= Tk()
blank_space=""
root.title= (blank_space*50+"Manu project")
root.resizable(width= FALSE, height=False)
root.geometry("438x573+460+40")

coverframe = Frame (root, bd=20, pady=2 , relief= RIDGE)
coverframe.grid()

root.mainloop

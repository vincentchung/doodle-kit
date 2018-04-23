from tkinter import Tk, Label, Button

class DisplayTextWidgets:
    def __init__(self, master,txt):
        self.master = master
        master.title("DoodleIoT Text Widget")

        self.label = Label(master, text=txt)
        self.label.pack()

        #self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack()

        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = DisplayTextWidgets(root,"hello world")
root.mainloop()

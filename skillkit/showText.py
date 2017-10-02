#
#  show text
#	 show text string on display device
#

from tkinter import Tk, Label, Button
import threading
import os

def default():
    return string()

def string():
    #root = Tk()
    #my_gui = DisplayTextWidgets(root,"hello world")
    #root.mainloop()
    os.system("python ./skillkit/display.py")
    return "ok"


class DisplayTextWidgets(threading.Thread):
    def __init__(self, master,txt):
        threading.Thread.__init__(self)

        #self.master = master
        master.title("DoodleIoT Text Widget")

        self.label = Label(master, text=txt)
        self.label.pack()
        self.start()
        #self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack()

        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack()

    def run(self):
        loop_active = True
        #label = Label(master, text=user_input)
        #label.pack()

    def greet(self):
        print("Greetings!")

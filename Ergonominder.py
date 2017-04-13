import setproctitle
import Tkinter as tk
import tkMessageBox
import time

setproctitle.setproctitle("ergonominder")

root = tk.Tk()

while (True):
    time.sleep(1201)
    root.withdraw()
    tkMessageBox.showwarning('Change position!', 'You\'e been static for too long! Change position + movement')
    root.update()
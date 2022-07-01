
from cmath import log
from tkinter import filedialog
import tkinter.ttk as ttk
from tkinter import *

# GLOBAL VARIABLES
root = Tk()
root.title("AutoWriter")
root.geometry("400x400")
root.resizable( False, False)

# FUNTIONS
def addFile():
    files = filedialog.askopenfilenames(title="파일을 선택하세요", filetypes=(("xlsx", "*.xlsx"), ("모든파일", "*.*")))
    logbox.insert(END, files)

# GUI
fileSelectLabel = Label(root, text="File Select")
fileSelectButton = Button(root, text = "양식", command=addFile)
fileSelectLabel.grid(row=0, column=0)
fileSelectButton.grid(row=0, column=1)

dataSelectLabel = Label(root, text = "Data Select")
dataSelectButton = Button(root, text = "데이터")
dataSelectLabel.grid(row=1, column=0)
dataSelectButton.grid(row=1, column=1)

saveAsLabel = Label(root, text = "Save As")
saveAsButton = Button(root, text = "추출경로")
saveAsLabel.grid(row=2, column=0)
saveAsButton.grid(row=2, column=1)
 
fileNameEntry = Entry(root)
startButton = Button(root, text = "시작")
fileNameEntry.grid(row=3, column=0)
startButton.grid(row=3, column=1)

# PROGRESS BAR
progressbar = ttk.Progressbar(root, maximum = 100, mode="indeterminate")
progressbar.grid(row=4, column=0)

# LOG LIST BOX 
logbox = Listbox(root, selectmode="extended", height=0)
logbox.grid(row=5, column=0)


root.mainloop()
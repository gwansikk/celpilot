from tkinter import *

root = Tk()
root.title("AutoWriter")
root.geometry("400x400")
root.resizable( False, False)

# 기본 GUI 구성
fileSelectLabel = Label(root, text="File Select")
fileSelectButton = Button(root, text = "양식")
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

# 프로그래스 바 추가하기

# LOG창 추가하기 

root.mainloop()
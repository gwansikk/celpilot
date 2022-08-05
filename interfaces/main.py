import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QWidget, qApp, QDesktopWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QTextEdit)

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        # 레이아웃
        widget = QWidget()
        grid = QGridLayout(widget)

        grid.addWidget(QLabel('양식:'), 0, 0)
        grid.addWidget(QLabel('데이터:'), 1, 0)
        grid.addWidget(QLabel('저장:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QLineEdit(), 2, 1)
        grid.addWidget(QTextEdit(), 3, 1)

        self.setCentralWidget(widget)

        # 기능 
        exitAction = QAction('종료', self)
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)
        # 메뉴바
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        filemenu = menuBar.addMenu('&파일')
        filemenu.addAction(exitAction)
        menuBar.addMenu('&편집')

        # 상태바
        self.statusBar().showMessage('준비완료')

        # 윈도우
        self.setWindowTitle('AutoWriter')
        self.resize(400, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainView()
    app.exec_()
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QWidget, qApp, QDesktopWidget, QGridLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QListWidget)

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):

        # 리스트
        listWidget = QListWidget()
        listWidget.addItem("프로그램이 정상적으로 실행되었습니다!")
        listWidget.currentItemChanged.connect(self.ItemChange)

        # 버튼
        self.buttonSelectDoc = QPushButton("양식 파일", self)
        self.buttonSelectData = QPushButton("데이터 파일", self)
        self.buttonSelectSave = QPushButton("저장 경로", self)

        # 레이아웃
        widget = QWidget()
        grid = QGridLayout(widget)

        grid.addWidget(self.buttonSelectDoc, 0, 1)
        grid.addWidget(self.buttonSelectData, 1, 1)
        grid.addWidget(self.buttonSelectSave, 2, 1)

        grid.addWidget(QLineEdit(), 0, 0)
        grid.addWidget(QLineEdit(), 1, 0)
        grid.addWidget(QLineEdit(), 2, 0)
        grid.addWidget(listWidget, 3, 0, 1, 0)

        self.setCentralWidget(widget)

        # 기능 
        exitAction = QAction('종료', self)
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)

        # 메뉴바
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        filemenu = menuBar.addMenu('&파일')
        menuBar.addMenu('&편집')

        filemenu.addAction(exitAction)

        # 상태바, 업데이트 확인
        self.statusBar().showMessage('최신버전입니다!')

        # 윈도우
        self.setWindowTitle('AutoWriter')
        self.setFixedSize(400, 600)
        self.WindowCenter()
        self.show()

    def WindowCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def ItemChange(self, item):
        print(item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainView()
    app.exec_()
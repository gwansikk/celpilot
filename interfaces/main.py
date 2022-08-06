import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QListWidget, QFileDialog)
from PySide6.QtGui import (QAction, QGuiApplication)

class MainView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):

        # 리스트
        self.listWidget = QListWidget()
        self.listAddMassage("프로그램이 정상적으로 실행되었습니다")

        # 입력창
        self.inputPathDoc = QLineEdit()
        self.inputPathData = QLineEdit()
        self.inputPathSave = QLineEdit()

        # 버튼
        self.buttonSelectDoc = QPushButton("양식 파일", self)
        self.buttonSelectData = QPushButton("데이터 파일", self)
        self.buttonSelectSave = QPushButton("저장 경로", self)

        self.buttonSelectDoc.clicked.connect(self.FileSelectDoc)
        self.buttonSelectData.clicked.connect(self.FileSelectData)
        self.buttonSelectSave.clicked.connect(self.FileSelectSave)

        # 레이아웃
        widget = QWidget()
        grid = QGridLayout(widget)

        grid.addWidget(self.buttonSelectDoc, 0, 1)
        grid.addWidget(self.buttonSelectData, 1, 1)
        grid.addWidget(self.buttonSelectSave, 2, 1)

        grid.addWidget(self.inputPathDoc, 0, 0)
        grid.addWidget(self.inputPathData, 1, 0)
        grid.addWidget(self.inputPathSave, 2, 0)
        grid.addWidget(self.listWidget, 3, 0, 1, 0)

        self.setCentralWidget(widget)

        # 기능 
        exitAction = QAction('종료', self)
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(QApplication.quit)

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

    def listAddMassage(self, massage):
        self.listWidget.addItem(massage)
        self.listWidget.currentItemChanged.connect(self.ItemChange)

    def WindowCenter(self):
        qr = self.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def ItemChange(self, item):
        print(item.text())

    def FileSelectDoc(self):
        fileName = QFileDialog.getOpenFileName(self, '양식파일을 선택합니다.', '', 'xlsx Files (*.xlsx)')
        self.inputPathDoc.setText(fileName[0])
        self.listAddMassage("양식파일이 정상적으로 선택되었습니다.")
    
    def FileSelectData(self):
        fileName = QFileDialog.getOpenFileName(self, '데이터파일을 선택합니다.', '', 'xlsx Files (*.xlsx)')
        self.inputPathData.setText(fileName[0])
        self.listAddMassage("데이터파일이 정상적으로 선택되었습니다.")

    def FileSelectSave(self):
        path = QFileDialog.getExistingDirectory(self, '저장할 경로를 선택합니다.')
        self.inputPathSave.setText(path[0])
        self.listAddMassage("저장할 경로를 선택했습니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = MainView()
    app.exec_()
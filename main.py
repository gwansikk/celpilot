import sys
from packages.ui.main import MainView
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    view = MainView()
    app.exec()

if __name__ == '__main__':
    main()

from PyQt5.QtCore import QSize
from auth import *
import main_window
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()


def window(newJira):
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = main_window.MainWindow(newJira)
    mainwindow.show()
    app.exec_()


def auth():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
    return window.jira


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    jira = auth()
    if jira:
        window(jira)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
import main_window_design
import functional


class MainWindow(QMainWindow, main_window_design.Ui_MainWindow):
    def __init__(self, jira):
        super().__init__()
        self.setupUi(self)
        self.jira = jira
        self.pushButton.clicked.connect(self.report)

    def report(self):
        jql = "Sprint in openSprints()"
        totalIssues = self.jira.search_issues(jql, maxResults=1000)
        msgBox = QMessageBox(self)
        reply = msgBox.question(
            self, 'Warning',
            'Вы хотите записать вывод в файл?',
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            functional.sort_status_to_file(totalIssues, functional.get_status(totalIssues))
        if reply == QMessageBox.No:
            this = QTextEdit(self)
            this.setPlainText(functional.sort_status(totalIssues, functional.get_status(totalIssues)))
            this.setFixedSize(QSize(800, 600))
            this.show()
           #functional.sort_status(totalIssues, functional.get_status(totalIssues))

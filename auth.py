from PyQt5 import QtWidgets
import auth_design
from jira import JIRA


class Window(QtWidgets.QMainWindow, auth_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.jira = {}
        self.setupUi(self)
        self.pushButton.clicked.connect(self.authentication)

    def authentication(self):
        jira_address = "https://jira.effective-group.ru/"
        jira_user = self.textEdit_2.toPlainText()
        jira_password = self.textEdit.toPlainText()
        if not jira_user or not jira_password:
            QtWidgets.QMessageBox.critical(self, "CRITICAL", "Ты долбаеб по русски написано логин пароль блять")
        else:
            try:
                jira = JIRA(server=jira_address,
                            basic_auth=(jira_user, jira_password),
                            max_retries=0)
            except Exception:
                QtWidgets.QMessageBox.warning(self, "WARNING", "Invalid creds, invalid user...")
            else:
                self.jira = jira
                self.close()

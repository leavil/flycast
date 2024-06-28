import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox, QLabel
from PyQt5.QtCore import Qt
import google.auth
from googleapiclient.discovery import build

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Login")
        self.layout = QVBoxLayout()
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.layout.addWidget(self.email_input)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Password")
        self.layout.addWidget(self.password_input)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout.addWidget(buttons)
        self.setLayout(self.layout)

    def get_credentials(self):
        email = self.email_input.text()
        password = self.password_input.text()
        # Here you would use the email and password to authenticate with Google's API
        # For this example, we'll just use the google.auth library to authenticate
        creds, project = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
        return creds

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Main Window")
        self.setCentralWidget(QLabel("You are logged in!"))

    def login(self):
        dialog = LoginDialog()
        if dialog.exec_() == QDialog.Accepted:
            creds = dialog.get_credentials()
            # Use the credentials to authenticate with Google's API
            service = build('compute', 'v1', credentials=creds)
            # Now you can use the service to make API calls
            print(service.instances().list(project='flycast-id', zone='us-central1-a').execute())
        else:
            print("Login cancelled")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.login()
    sys.exit(app.exec_())
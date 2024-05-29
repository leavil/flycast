# view.py
from PyQt5.QtWidgets import QMainWindow, QLabel

class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Datos:", self)
        self.label.setGeometry(10, 10, 150, 30)
    
    def update_label(self, data):
        self.label.setText(f"Datos: {data}")


# presenter.py
class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.update_label(self.model.get_data())

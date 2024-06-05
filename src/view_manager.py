import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class FlightTrackingView(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the layout
        self.layout = QVBoxLayout()

        # Initialize the map label
        self.map_label = QLabel()
        self.layout.addWidget(self.map_label)

        # Initialize the update button
        self.update_button = QPushButton("Update Map")
        self.update_button.clicked.connect(self.update_map)
        self.layout.addWidget(self.update_button)

        # Initialize the central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def update_map(self):
        # Call the presenter's update_map method
        self.presenter.update_map()

    def set_map_image(self, image):
        # Set the map label's pixmap
        self.map_label.setPixmap(image)

    def set_presenter(self, presenter):
        # Set the presenter
        self.presenter = presenter
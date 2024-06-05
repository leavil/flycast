import sys
import requests
import json

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QLabel
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file
        loadUi('ui_file.ui', self)

        # Initialize map
        self.map_widget = QLabel(self)
        self.map_widget.resize(800, 600)
        self.map_widget.move(0, 0)

        # Set map as central widget
        self.setCentralWidget(self.map_widget)

        # Connect update button to update_map method
        self.update_button.clicked.connect(self.update_map)
        
        
        
    def update_map(self):
        # Fetch real-time flight data from OpenSky Network REST API
        response = requests.get('https://opensky-network.org/api/states/all')
        data = json.loads(response.text)

        # Parse data and extract latitude and longitude of each aircraft
        positions = []
       for flight in data['states']:
            lat = flight[0]
            lon = flight[1]
            positions.append((lat, lon))

        # Display positions on map
        self.map_widget.setPixmap(self.create_map(positions))

    def create_map(self, positions):
        # Create map image
        map_image = QImage(800, 600, QImage.Format_RGB32)
        map_image.fill(Qt.white)

        # Create QPainter object
        painter = QPainter(map_image)

        # Set pen color and width
        pen = QPen(Qt.blue)
        pen.setWidth(2)

        # Draw positions on map
        painter.setPen(pen)
        for pos in positions:
            painter.drawPoint(pos[1], pos[0])

        # Release QPainter object
        painter.end()

        # Return map image as QPixmap
        return QPixmap.fromImage(map_image)
    
    
    if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
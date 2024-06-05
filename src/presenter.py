import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class Presenter:
    def __init__(self, view):
        self.view = view
        self.view.pushButton.clicked.connect(self.update_map)

    def update_map(self):
        # Make an API request to get the latest flight data
        response = requests.get('https://api.flightradar24.com/data/flights/list')
        data = response.json()

        # Extract the relevant information from the API response
        flights = [
            {'callsign': flight['callsign'], 'latitude': flight['latitude'], 'longitude': flight['longitude']}
            for flight in data['flights']
            if flight['latitude'] and flight['longitude']
        ]

        # Update the view with the latest flight data
        self.view.update_map(flights)

class View(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('flight_tracker.ui', self)

    def update_map(self, flights):
        # Clear the previous map
        self.map.clear()

        # Add markers for each flight
        for flight in flights:
            marker = self.map.addMarker(flight['latitude'], flight['longitude'])
            marker.setTitle(flight['callsign'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    presenter = Presenter(view)
    view.show()
    sys.exit(app.exec_())
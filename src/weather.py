import sys
import json
import urllib.request
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
from folium.plugins import MarkerCluster

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather Map App')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        self.map_view = QWebEngineView()
        layout.addWidget(self.map_view)

        self.map = folium.Map(prefer_canvas=True, zoom_start=2)
        self.map_view.setHtml(self.map._repr_html_())

        self.show_weather_button = QPushButton('Show Weather', self)
        self.show_weather_button.clicked.connect(self.show_weather_dialog)
        layout.addWidget(self.show_weather_button)

    def show_weather_dialog(self):
        location, ok = LocationDialog.get_location(self)
        if ok:
            self.show_weather(location)

    def show_weather(self, location):
        # Clear previous markers
        self.map = folium.Map(prefer_canvas=True, zoom_start=2)

        # Get weather data from a public endpoint (example: OpenWeatherMap)
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=YOUR_API_KEY&units=metric'  # Replace YOUR_API_KEY with your actual API key
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        
        if data:
            lat = data['coord']['lat']
            lon = data['coord']['lon']
            weather_state = data['weather'][0]['main']
            temperature = data['main']['temp']

            # Add marker to the map
            folium.Marker([lat, lon], popup=f'Temperature: {temperature}°C, Weather: {weather_state}').add_to(self.map)

        # Refresh map view
        self.map_view.setHtml(self.map._repr_html_())

    def closeEvent(self, event):
        self.map_view.close()
        event.accept()

class LocationDialog(QDialog):
    @staticmethod
    def get_location(parent=None):
        dialog = LocationDialog(parent)
        result = dialog.exec_()
        location = dialog.location_line_edit.text()
        return location, result == QDialog.Accepted

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Enter Location')
        layout = QVBoxLayout(self)
        self.location_label = QLabel('Enter location:')
        layout.addWidget(self.location_label)
        self.location_line_edit = QLineEdit()
        layout.addWidget(self.location_line_edit)
        self.ok_button = QPushButton('OK')
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

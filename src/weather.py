import sys
import json
import urllib.request
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium

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

        # Get weather data from Visual Crossing API
        api_key = 'VPZFXMYBUW7RUM4GYJ3Z7CA44'
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=days%2Calerts&key={api_key}&contentType=json'

        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())

            print("JSON response:")
            print(json.dumps(data, indent=4))  # Print the JSON response to understand its structure

            if 'days' in data:
                for day_data in data['days']:
                    # Default coordinates to the location provided
                    lat = data.get('latitude', 40.463667)
                    lon = data.get('longitude', -3.74922)

                    # Extract daily weather data
                    date = day_data['datetime']
                    temp_max = day_data['tempmax']
                    temp_min = day_data['tempmin']
                    conditions = day_data['conditions']

                    # Add markers for each day
                    popup_text = f'Date: {date}<br>Max Temp: {temp_max}°C<br>Min Temp: {temp_min}°C<br>Weather: {conditions}'
                    folium.Marker([lat, lon], popup=popup_text).add_to(self.map)

                    # Color the map based on temperature
                    color = self.get_color(temp_max)
                    folium.CircleMarker(
                        location=[lat, lon],
                        radius=10,
                        color=color,
                        fill=True,
                        fill_color=color
                    ).add_to(self.map)

                # Convert Folium map to HTML and update QWebEngineView
                html_map = self.map._repr_html_()
                self.map_view.setHtml(html_map)

        except Exception as e:
            print(f"Error fetching weather data: {e}")

    def get_color(self, temp):
        if temp <= 0:
            return 'blue'
        elif 0 < temp <= 10:
            return 'green'
        elif 10 < temp <= 20:
            return 'yellow'
        elif 20 < temp <= 30:
            return 'orange'
        else:
            return 'red'

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

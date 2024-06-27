import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QTimer
import folium

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rastreador de Aviones en Tiempo Real")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.map_view = QWebEngineView()
        layout.addWidget(self.map_view)

        button_refresh = QPushButton("Actualizar Aviones")
        button_refresh.clicked.connect(self.refresh_planes)
        layout.addWidget(button_refresh)

        # Configurar el temporizador para actualizar automáticamente cada 60 segundos
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_planes)
        self.timer.start(300000)  # Intervalo en milisegundos (60000 ms = 60 s) 300k = 5 min

        self.refresh_planes()  # Llamar a la función para cargar los aviones al inicio

    def refresh_planes(self):
        try:
            # Obtener datos de la API de OpenSky Network
            url = "https://opensky-network.org/api/states/all"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                # Crear mapa folium centrado en una ubicación específica
                my_map = folium.Map(location=[40.730610, -73.935242], zoom_start=8)
                
                # Limitar el número de aviones mostrados
                max_planes = 50
                plane_count = 0
                
                # Iterar sobre los aviones y agregar marcadores al mapa
                for flight in data["states"]:
                    if plane_count >= max_planes:
                        break
                    
                    # Obtener la latitud y longitud del avión
                    lat = flight[6]
                    lon = flight[5]
                    if lat and lon:
                        # Información detallada del avión
                        popup_text = (f"Avión: {flight[1]}<br>"
                                      f"Origen: {flight[2]}<br>"
                                      f"Destino: {flight[3]}<br>"
                                      f"Latitud: {lat}<br>"
                                      f"Longitud: {lon}<br>"
                                      f"Velocidad: {flight[9]} m/s<br>"
                                      f"Altitud: {flight[13]} m")
                        # Añadir marcador al mapa con icono personalizado
                        icon = folium.Icon(icon="plane", prefix='fa', color="blue")
                        folium.Marker([lat, lon], popup=popup_text, icon=icon).add_to(my_map)
                        plane_count += 1
                
                # Guardar el mapa folium como HTML temporal y mostrarlo en QWebEngineView
                my_map.save("map.html")
                self.map_view.setHtml(open("map.html").read())
            else:
                print(f"Error al obtener datos de la API: {response.status_code}")
        except Exception as e:
            print(f"Error al crear el mapa folium: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

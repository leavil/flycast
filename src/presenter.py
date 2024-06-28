from PyQt5 import QtWidgets, QtCore
from view2 import View
from model import Model
from login  import LoginDialog
import subprocess

class Presenter:
    def __init__(self):
        self.view = View()  # Instancia de la vista
        self.model = Model()
        self.view.setupUi(self.view)  # Configuración de la interfaz gráfica
        
        # Lista para mantener referencias a los procesos subprocess
        self.subprocesses = []

        # Conectar botones a métodos del Presenter
        self.view.bn_min.clicked.connect(self.hide_window)
        self.view.bn_close.clicked.connect(self.close_window)
        self.view.toodle.clicked.connect(self.toggle_frame_bottom)
        self.view.bn_plane.clicked.connect(self.on_bn_plane_clicked)
        self.view.bn_weather.clicked.connect(self.on_bn_weather_clicked)
        self.view.bn_settings.clicked.connect(self.on_bn_settings_clicked)

        # Configurar datos iniciales en la vista
        self.view.lab_appname.setText("Fly Cast")
        self.view.lab_user.setText("User Name")  # Aquí deberías obtener el nombre de usuario del modelo

        # Estado inicial de la ventana (maximizada)
        self.is_maximized = True

    def hide_window(self):
        self.view.hide()

    def close_window(self):
        self.view.close()

    def start(self):
        # Maximizar la ventana al iniciar
        self.view.resize(self.view.maximumSize())
        self.view.show()  # Mostrar la vista al iniciar la aplicación
        self.on_bn_settings_clicked
        # Conectar evento aboutToQuit de QApplication para cerrar subprocessos
        QtWidgets.QApplication.instance().aboutToQuit.connect(self.close_subprocesses)

    def toggle_frame_bottom(self):
        if self.is_maximized:
            # Guardar tamaño actual antes de cambiar a personalizado
            self.view.previousSize = self.view.size()
            # Cambiar a tamaño personalizado que ajusta al contenido visible
            self.view.resize(self.view.minimumSizeHint())
            self.is_maximized = False
        else:
            # Maximizar la ventana de nuevo
            if hasattr(self.view, 'previousSize'):
                self.view.resize(self.view.previousSize)
                del self.view.previousSize  # Eliminar el tamaño personalizado guardado
                self.is_maximized = True

    def on_bn_plane_clicked(self):
        try:
            # Ejecutar tracker.py utilizando subprocess
            process = subprocess.Popen(['python', 'tracker.py'])
            self.subprocesses.append(process)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.view, "Error", f"No se pudo iniciar tracker.py: {str(e)}")

    def on_bn_weather_clicked(self):
        try:
            # Ejecutar weather.py utilizando subprocess
            process = subprocess.Popen(['python', 'weather.py'])
            self.subprocesses.append(process)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.view, "Error", f"No se pudo iniciar weather.py: {str(e)}")

    def on_bn_settings_clicked(self):
        try:
            # Obtener el correo electrónico ingresado del LoginDialog
            dialog = LoginDialog()
            if dialog.exec_() == LoginDialog.Accepted:
                email = dialog.email_input.text()
                # Eliminar todo después del primer '@'
                username = email.split('@')[0]
                self.view.lab_user.setText(username)  # Actualizar el QLabel con el nombre de usuario
                
                # Ejecutar login.py utilizando subprocess
                process = subprocess.Popen(['python', 'login.py'])
                self.subprocesses.append(process)
                
            else:
                QtWidgets.QMessageBox.warning(self.view, "Warning", "Login cancelled.")
                
        except Exception as e:
            QtWidgets.QMessageBox.critical(self.view, "Error", f"No se pudo iniciar login.py: {str(e)}")


    def close_subprocesses(self):
        # Cerrar todos los subprocessos abiertos
        for process in self.subprocesses:
            process.kill()  # Opcionalmente puedes usar .terminate() dependiendo de la necesidad

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    presenter = Presenter()
    presenter.start()
    sys.exit(app.exec_())

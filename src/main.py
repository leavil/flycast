# En el archivo main.py o donde estés configurando tu aplicación
from PyQt5 import QtWidgets
from view import View
from model import Model
from presenter import Presenter

def main():
    app = QtWidgets.QApplication([])  # Instancia de la aplicación PyQt
    view = View()  # Instancia de la vista
    model = Model()  # Instancia del modelo
    presenter = Presenter(view, model)  # Instancia del presenter con la vista y el modelo
    
    view.show()  # Mostrar la vista
    app.exec_()  # Ejecutar la aplicación

if __name__ == "__main__":
    main()

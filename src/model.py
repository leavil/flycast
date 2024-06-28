# En el archivo model.py
import subprocess
import os
class Model:
    def __init__(self):
        # Aquí podrías inicializar el modelo si es necesario
        pass
    
    def execute_tracker_script(self):
        # Obtener la ruta del directorio actual del script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construir la ruta al script tracker.py utilizando una ruta relativa
        script_path = os.path.join(current_dir, "..", "src", "tracker.py")
        
        # Verificar si el archivo existe antes de ejecutarlo
        if os.path.exists(script_path):
            try:
                subprocess.run(["python", script_path])  # Ejecutar el script tracker.py
                # Aquí puedes manejar cualquier resultado o acción después de ejecutar el script
            except Exception as e:
                print(f"Error al ejecutar el script tracker.py: {e}")
        else:
            print(f"No se encontró el archivo {script_path}")
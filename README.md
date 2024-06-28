# FlyCast ✈️

FlyCast es una aplicación de gestión de rutas de vuelo diseñada para pilotos y entusiastas de la aviación. Permite a los usuarios planificar vuelos teniendo en cuenta el análisis predictivo del clima y proporciona herramientas para una navegación segura y conveniente.
![Interfaz](\src\images\deploy.png)

## Características 🚀

- **Análisis Predictivo del Clima**: Accede a datos históricos de Meteomatics para predecir las condiciones climáticas futuras en una ruta de vuelo específica.
- **Perfil de Usuario Personalizado**: Los usuarios pueden crear y gestionar perfiles personalizados para guardar rutas favoritas y preferencias de vuelo.
- **Login y Gestión de Usuarios**: Seguridad y comodidad garantizadas mediante Firebase y Sign Up With Google para la autenticación de usuarios.
- **Entrada de Datos de Vuelo**: Ingrese las coordenadas de salida y llegada o seleccione ubicaciones a través de una API como Google Maps.
- **Selección de Fecha y Hora**: Especifica la fecha y hora de salida para planificar los vuelos.
- **Análisis a una Semana Vista**: Accede a análisis del clima para la semana siguiente para una planificación más precisa del vuelo.
- **Notificaciones de Cambios Climáticos Severos**: Recibe notificaciones en tiempo real sobre cambios climáticos que puedan afectar la ruta de vuelo.
- **Seguimiento en Tiempo Real de Otros Aviones**: Sigue y visualiza otros aviones en tiempo real que realicen la misma ruta de vuelo.
- **Interfaz de Usuario Intuitiva**: Una interfaz amigable que permite a los usuarios navegar fácilmente por las diferentes funcionalidades.

## Diagrama de Clases 📐

El siguiente diagrama de clases representa la estructura y las relaciones entre las principales clases dentro del sistema FlyCast. Este diagrama es fundamental para comprender cómo están organizados los componentes del proyecto y cómo interactúan entre sí.

![Diagrama de Clases](\src\images\diagram\UML.png")

### Explicación de las Clases Principales:

1. **Usuario (`User`)**:

   - **Descripción**: Representa a un usuario registrado en el sistema.
   - **Atributos**: Incluye datos como el nombre de usuario, correo electrónico y preferencias de notificación.
   - **Métodos**: Pueden incluir métodos para la gestión de perfiles y configuraciones de cuenta.

2. **Ruta (`FlightRoute`)**:

   - **Descripción**: Modela una ruta de vuelo planificada por un usuario.
   - **Atributos**: Puede incluir coordenadas de inicio y destino, fecha y hora de salida, y detalles meteorológicos asociados.
   - **Métodos**: Podría tener métodos para calcular la duración estimada del vuelo y realizar análisis predictivo del clima.

3. **Notificación (`Notification`)**:

   - **Descripción**: Representa una notificación enviada al usuario sobre cambios climáticos severos u otras actualizaciones importantes.
   - **Atributos**: Incluye detalles del mensaje y la fecha/hora de envío.
   - **Métodos**: Pueden incluir métodos para gestionar el estado de la notificación y su visualización en la interfaz de usuario.

4. **Interfaz de Usuario (`UserInterface`)**:
   - **Descripción**: Gestiona la interacción del usuario con la aplicación FlyCast.
   - **Atributos**: Puede contener referencias a otras clases como `FlightRoute` y `Notification`.
   - **Métodos**: Facilita la navegación por la aplicación y la presentación de información relevante al usuario.

### Relaciones entre Clases:

- **Asociaciones**: Indicadas por líneas sólidas que conectan las clases. Por ejemplo, `User` puede tener múltiples `FlightRoute` asociadas.
- **Herencias y Composiciones**: Se muestran con flechas y líneas punteadas según corresponda, para representar relaciones más específicas como herencia o composición entre clases.

### Uso del Diagrama de Clases:

El diagrama de clases proporciona una vista estructurada y detallada del diseño del sistema FlyCast. Facilita la comprensión de cómo interactúan los diferentes componentes del sistema y cómo se organizan las responsabilidades entre las clases. Este diagrama es crucial tanto para desarrolladores nuevos que se unan al proyecto como para el mantenimiento y la evolución continua de la aplicación.

## Instalación 🛠️

1. Clona este repositorio: `git clone https://github.com/leavil/flycast.git`
2. Instala las dependencias, escriba en el terminal: `pip install -r requirements.txt`

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, sigue estos pasos:

1. Fork el proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia 📝

Este proyecto está bajo la [Licencia MIT](LICENSE).

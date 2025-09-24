# Diario de Emociones

Este proyecto es una aplicación de escritorio para el registro y seguimiento de emociones personales, desarrollada en Python con la biblioteca `tkinter` para la interfaz de usuario y diseñada para integrarse conceptualmente con una base de datos MySQL.

El sistema permite gestionar las siguientes entidades mediante formularios modulares y una interfaz gráfica intuitiva:

- **Usuarios**: Registro de las personas que utilizan el diario emocional.
- **Emociones**: Catálogo de emociones disponibles (nombre y emoji).
- **Entradas**: Registro de reflexiones o eventos emocionales del usuario.
- **Reportes**: Generación de resúmenes simulados de emociones más frecuentes.


---

## Contenido del Repositorio

- `diario.emociones.sql`: Archivo SQL con el esquema de la base de datos (`CREATE DATABASE`, `CREATE TABLE`).
- `DiarioEmocionesProyecto.py`: El script principal de Python que ejecuta la interfaz gráfica con POO y 4 módulos.

---

## Requisitos

Para poder ejecutar este proyecto, necesitas tener instalados los siguientes componentes:

- **Python 3.x**: El lenguaje de programación.
- **MySQL Server**: El sistema de gestión de bases de datos (puedes usar XAMPP).
- **Bibliotecas de Python**:
  - `tkinter`: Generalmente viene incluido en la instalación de Python.
  - `tkcalendar`: Para el selector de fechas en las entradas.  
    Puedes instalarlo usando pip:
    ```bash
    pip install tkcalendar
    ```

---

## Configuración y Uso

### Configuración de la Base de Datos:
1. Asegúrate de que tu servidor MySQL esté en ejecución (inicia XAMPP si lo usas).
2. Importa el archivo `diario.emociones.sql` en tu servidor MySQL usando HeidiSQL para crear la base de datos y las tablas necesarias.
3. **No es necesario configurar conexión en el código**, ya que las operaciones CRUD no están implementadas en esta entrega académica.

### Ejecutar la Aplicación:
1. Abre una terminal o línea de comandos.
2. Navega al directorio donde se encuentra el archivo `DiarioEmocionesProyecto.py`.
3. Ejecuta el script de Python:
   ```bash
   python DiarioEmocionesProyecto.py

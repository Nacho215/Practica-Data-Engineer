# Consigna 🎯
Utilizando los conceptos aprendidos en el módulo 20 - Datos con Pandas II, resolver el siguiente ejercicio.
Desarrollar una aplicación que realice la siguientes tareas:
1. Conectarse a la url que contiene el archivo CSV de medallas
olímpicas.
2. Descargar los datos y obtener un sub dataset que contenga a
todas las medallas de oro (Gold) Estados Unidos (USA) a partir del
año 1950.
3. Crear una base de datos “olympics” en SQLite y la tabla “medals”.
4. Guardar en la base de datos. los datos generados en el sub
dataset.
5. Consultar la base de datos y validar que los datos se hayan
cargado correctamente.
# Notas 📄
- En la carpeta 'src' se encuentra el script 'main.py' que resuelve la consigna.
- En la carpata 'databases' se encuentra la base de datos SQLite 'olympics.db' que genera el script.
- Se agregó la columna 'IdMedal' en la tabla 'medals' para almacenar el índice proveniente de la fuente de datos original.
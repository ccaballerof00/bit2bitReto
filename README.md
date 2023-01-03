# bit2bitReto

Los pasos para poder ejecutar la aplicación son:

1. Clonar el repositorio
2. Situarse en la carpeta app, donde están los archivos requirements.txt y manage.py
3. Ahora hay que crear un entorno virtual para instalar las librerías necesarias, esto se hace con los siguientes comandos:
- pip install virtualenv
- virtualenv newenv
- source newenv/Scripts/activate
4. Una vez con el venv activado, se procede a instalar las librerías con el siguiente comando:
- pip install -r requirements.txt
5. Una vez finalizada la instalación de librerías, se ejecuta el servidor con el siguiente comando:
- python manage.py runserver
6. Con esto el servidor ya estará montado en localhost,ahora hay que dirigirse al index de la página colocando /index en la URL del servidor.
7. No es necesario realizar ninguna acción con respecto a la base de datos debido a que la dejé hosteada en un servidor de Azure.
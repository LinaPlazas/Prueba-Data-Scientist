# Prueba-Data-Scientist

Este repositorio muestra el paso a paso para lanzar una aplicación utilizando heroku, en la cual se exponen los resultados obtenidos luego de realizar análisis de sentimientos sobre los comentarios de los usuarios en una aplicación móvil.

### Comenzando <img src="/imagenes/cohete.jpg" width="30" height="30"> 
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Pre-requisitos <img src="/imagenes/requisitos.jpg" width="30" height="30"> 

Instalar: <br>
- bs4 <br>
- selenium <br>
- google-cloud <br>
- fast api <br>
- uvicorn <br>
- jsonschema <br>
- pandas <br>

### Instalación <img src="/imagenes/instalacion.jpg" width="30" height="30"> 

- pip install bs4
- pip install selenium
- sudo -H pip install --upgrade google-cloud-language
- pip install fastapi==0.67.0
- pip install uvicorn==0.14.0
- pip install jsonschema==3.0.1

### Ejecutando pruebas <img src="/imagenes/portatil.png" width="30" height="30"> 

#### Web scraping

Para obtener los comentarios de la aplicación, ejecute web_scraping.py

- python3 web_scraping.py

Tendra como resultado un archivo excel con los comentarios encontrados en la pagina web

- comentarios.xlsx

#### Análisis de sentimientos

Para realizar el análisis de sentimientos de los comentarios en el paso anterior ejecute sentiment_analysis.py

- python3 sentiment_analysis.py

<p style='text-align: justify;'> En este paso se utiliza la Api de Google Cloud Natural Language la cual arroja un número decimal dependiendo de que tan positivo o negativo fue el comentario analizado. Posteriormente con la libreria pandas.cut se convierte la variable continua (score) en variable categórica (cantidad de estrellas). Se tendra como resultado un archivo json con el comentario, score obtenido, cantidad de estrellas y sentimiento (positivo,negativo o neutro).</p>

- Resultados_comentarios.json


#### Creación de App

Para crear la app se utilizó fastAPI, utilice el siguiente comando para correr la aplicación:

- uvicorn main:app --reload

Y escriba en su navegador lo siguiente:

-http://127.0.0.1:8000/docs

Oprima Get y luego Try it out, deberá aparecerle lo siguiente:

<img src="/imagenes/api.png"> 

Digite el número de comentarios que desea visualizar y oprima execute. Deberá obtener lo siguiente:

<img src="/imagenes/api2.png"> 

Como puede observar al oprimir execute se muestra la cantidad de comentarios que ha ingresado, asi como su correspondiente calificación, cantidad de estrellas y sentimiento encontrado.

#### Despliegue de App

Para desplegar la aplicación se utilizó heroku y el link en el que puede encontrar el resultado final es el siguiente:

##### https://prueba-data-scientist.herokuapp.com/docs



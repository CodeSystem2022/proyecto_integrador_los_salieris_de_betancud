API REST para la gestión de gastos  

  

¡Bienvenido al repositorio del proyecto integrador grupo los salaries de Betancud tercer semestre API REST para la gestión de gastos! Esta API es una aplicación construida con Python y el framework FastAPI que permite administrar y realizar un seguimiento de los gastos personales. 

  

Características principales 

  

Registro de gastos: Los usuarios pueden registrar sus gastos con detalles como la fecha, la descripción y el monto. 

  

Consulta de gastos: Los usuarios pueden buscar, filtrar y ordenar sus gastos utilizando diferentes criterios como rango de fechas o monto.  

  

Estadísticas de gastos: Los usuarios pueden obtener estadísticas sobre sus gastos, como el total gastado en un período de tiempo, el promedio de gastos diarios o el porcentaje de gastos por categoría. 

  

Requisitos de instalación  

* Python 3.7 o superior  

* Pip (administrador de paquetes de Python) 

  

Configuración  

1.  Clona este repositorio en tu máquina local: 

  

``` 

git clone https://github.com/tu-usuario/gestion-de-gastos-api.git 

``` 

  

2. Ve al directorio del proyecto: 

  

``` 

cd gestion-de-gastos-api  

``` 

  

3. Crea un entorno virtual: 

  

``` 

python -m venv venv  

``` 

  

4. Activa el entorno virtual: 

  

* En Windows: 

  

``` 

venv\Scripts\activate  

``` 

  

* En macOS y Linux: 

  

``` 

source venv/bin/activate  

``` 

  

5. Instala las dependencias del proyecto: 

  

``` 

pip install -r requirements.txt  

``` 

  

6. Configura las variables de entorno: 

  

Crea un archivo `.env` en el directorio raíz del proyecto y define las siguientes variables: 

  

``` 

#Archivo .env 

  

#Configuración de la base de datos 

MONGODB_URI="srv://" 

``` 

  

7. Inicia el servidor de desarrollo: 

  

``` 

uvicorn app.main:app --reload  

``` 

  

La API ahora estará disponible en http://localhost:8000.  

Puedes usar herramientas como Postman o curl para interactuar con la API. 

  

Uso  

  

La API proporciona los siguientes endpoints: 

  

GET /gastos: Obtiene todos los gastos. 

GET /gastos/{id}: Obtiene un gasto por su id. 

POST /gastos: Crea un gasto. 

PUT /gastos/{id}: Modifica un gasto. 

 DELETE /gastos: Elimina un gasto. 

  

  Puedes encontrar más detalles sobre el uso de cada endpoint en la documentación interactiva de la API, que estará disponible en http://localhost:8000/docs cuando el servidor esté en ejecución. 

  

Contribución 

  

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue los siguientes pasos: 

  

1. Realiza un fork de este repositorio.  

2. Crea una rama para tu función/feature:  

  

``` 

git checkout -b feature/awesome-feature  

``` 

  

3. Realiza tus cambios y haz commit de ellos:  

  

``` 

git commit -m "Añadir función increíble"  

``` 

  

4. Envía tus cambios a tu repositorio remoto:  

  

``` 

git push origin feature/awesome-feature  

``` 

  

5. Abre un pull request en este repositorio.  

  

Licencia 

  

Este proyecto está bajo la licencia MIT. Puedes consultar el archivo LICENSE para obtener más detalles. 

  

¡Gracias por utilizar la API REST para la gestión de gastos! Si tienes alguna pregunta o sugerencia, no dudes en crear un issue en este repositorio. ¡Disfruta del desarrollo! 

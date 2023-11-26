# API RestFull-Flask

## Resumen
La aplicación desarrollada tiene como objetivo gestionar y controlar las entregas de alimentos durante una jornada especial de donación llevada a cabo por un reconocido restaurante. El sistema permite a los colaboradores del restaurante registrar a los residentes de la región a través de un formulario en una aplicación web. Los datos recopilados son nombre, apellidos, teléfono, correo, edad, dirección, confirmacion de la comida entregada y observaciones. En esta se pueden listar, agregar, borrrar y actualizarr los datos de los residentes, ademas de filtrar por Id, nombre o correcto electronico y tambien organizar por edad (de mayor a menor) y nombre (de la A a la Z)

## Librerias Usadas
- Flask: Framework que proporciona una estructura robusta y modular para la API, permitiendo un desarrollo ágil y eficiente.

- psycopg2: que es un adaptador de base de datos PostgreSQL para Python.

- SQLAlchemy: Biblioteca de SQL para Python, que nos proporciona un kit de herramientas SQL y un ORM que optimiza las interacciones con la base de datos MySQL, garantizando un rendimiento óptimo.

- Flask-SQLAlchemy: es una extensión para Flask que agrega soporte para SQLAlchemy a su aplicación. Simplifica el uso de SQLAlchemy con Flask mediante la configuración de objetos comunes y patrones para usar esos objetos, como una sesión vinculada a cada solicitud web, modelos, y motores.

- Flask-Cors: es permitir el intercambio de recursos entre dominios diferentes, lo cual es esencial para aplicaciones web que utilizan servicios o recursos alojados en servidores externos.

## Estructura del proyecto
- **/src**  *(Contiene los archivos principales de la aplicación)*
  - **/controllers**
    - ResidentController.py *(manejan la lógica de negocio relacionada con los residentes)*
  - **/models**
    - ResidentModel.py  *(Definición del modelo de datos)*
  - **/routes**
    - ResidentRoutes.py *(Definición de las rutas de la aplicación)*
  - **/utils**
    - field_validation.py  *(Utilidades para validar campos en la aplicación)*
    - respons_utils.py *(Utilidad para estandarizar respuestas JSON)*
    
  - config.py *(Archivo de configuración de la aplicación)*
  - app.py *(Punto de entrada principal de la aplicación)*

## URLs
##### Obtener todos los residentes existentes en la base de datos.
**https://www.ejemplo.com/api/residents/**
lista todos los residentes que esten en la base de datos, los mostrara de 10 en 10, para obtener los registros siguientes se debe agregar **?page=2** -->**https://www.ejemplo.com/api/residents/?page=2**
##### Obtener residentes especificos
**https://www.ejemplo.com/api/residents/4e6f7a90-2d40-4703-ab91-473974bf3ae0**
**https://www.ejemplo.com/api/residents/Alice**
**https://www.ejemplo.com/api/residents/john.doe@example.com**
Esta ruta se utiliza para obtener uno o varios residentes específico según el parámetro proporcionado en la URL, los parametros de busqueda pueden ser el ID, Nombre y Correo electronico, igualmente puedes agregar **?page=2** si tienes mas de 10 registros con ese parametro.

##### Agregar un Nuevo Residente
**https://www.ejemplo.com/api/add**
Esta ruta se utiliza para agregar un nuevo residente a la base de datos utilizando datos proporcionados en la solicitud POST, este es un ejemplo de los datos que se deben introducir. 
{
    "address": "789 Pine St",
    "age": 22,
    "delivered_food": false,
    "email": "alice.johnson@example.com",
    "last_name": "Johnson",
    "name": "Alice",
    "observation": "None",
    "phone": "1555555555"
}


##### Eliminar un Residente por ID
https://www.ejemplo.com/api/delete/numero_id
Esta ruta se utiliza de tipo DELETE es para eliminar un residente específico de la base de datos según el ID proporcionado en la URL.

##### Actualizar un Residente por ID
https://www.ejemplo.com/api/updated/numero_id
Esta ruta de tipo PUT se utiliza para actualizar la información de un residente específico según el ID proporcionado en la URL. tiene que tener en cuenta que no  se puede modificar el id, si lo hace mostrara un error.
{
    "address": "202 Maple St",
    "age": 28,
    "delivered_food": false,
    "email": "eva.brown@example.com",
    **"id": "b54acc2e-a05b-4ec1-b399-3ef163c83be1",**
    "last_name": "Brown",
    "name": "Eva",
    "observation": "Gluten-free",
    "phone": "1999999999"
}
##### Filtrar Residentes por Edad Descendente
https://www.ejemplo.com/api/order/age
Esta ruta se utiliza para obtener todos los residentes ordenados por edad de manera descendente.igualmente puedes agregar **?page=2** si tienes mas de 10 registros con ese parametro.

##### Filtrar Residentes por Nombre Ascendente
https://www.ejemplo.com/api/order/name
Esta ruta se utiliza para obtener todos los residentes ordenados alfabéticamente por nombre de manera ascendente.puedes agregar **?page=2** si tienes mas de 10 registros con ese parametro.
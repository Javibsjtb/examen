# Serie 4 - API de animales

Proyecto con Django REST Framework y MySQL. Sin autenticación.

Autor: Javier Alejandro Mejía Catalán, carné 090-23-7345.

## Ejecutar

Requiere Python 3.10 o superior y MySQL 8.0.11 o superior.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En MySQL, ejecutar `crear_base.sql`, crear un usuario para la base y asignarle permisos. Configurar las variables de `.env.example` con los valores propios. Django lee variables del entorno; no carga el archivo `.env` automáticamente. En macOS/Linux pueden exportarse así:

```sh
set -a
source .env
set +a
python manage.py migrate
python manage.py runserver 127.0.0.1:8001
```

Copiar primero `.env.example` a `.env` y editar la contraseña. El puerto de MySQL por defecto de este proyecto es 3307; usar DB_PORT=3306 si la instalación de MySQL usa el puerto habitual.

## Rutas

- POST y GET: http://127.0.0.1:8001/api/animales/
- GET, PUT y DELETE por id: http://127.0.0.1:8001/api/animales/1/

Campos obligatorios: nombre, especie, raza, edad. Edad entera entre 0 y 200. El id, created_at y updated_at los genera el servidor.

POST válido devuelve 201; GET, PUT y DELETE devuelven 200. DELETE responde con un mensaje JSON. Los datos inválidos devuelven 400 y un id inexistente devuelve 404.

## Pruebas

Se usó el cliente HTTP local `cliente_http.html`, que envía solicitudes reales con fetch. Para abrirlo:

```sh
python3 -m http.server 5173 --bind 127.0.0.1
```

Entrar a http://127.0.0.1:5173/cliente_http.html y enviar las seis solicitudes. Las capturas están en `evidencias/` y los cuerpos y respuestas exactos en `evidencias/resultados.json`. Se verificó además que, después de DELETE, el detalle devuelve 404 y la lista queda vacía.

El ejemplo de React está en `react/Animales.jsx` y tiene 13 líneas. Permite la aplicación React en localhost:5173 o 127.0.0.1:5173 mediante CORS. El servidor es local, no está publicado en Internet.

El PDF de entrega está en `entrega/`.

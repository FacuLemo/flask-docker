# flask-docker

El primer paso para hacer funcionar el programa es clonar el repositorio en tu computadora.

Una vez clonado, podemos construir una imagen. Pero primero necesitamos tener instalado Docker y Docker-compose.
Se construye la imagen a partir del dockerfile con el siguiente comando del docker-compose:
```bash
  sudo docker-compose build
```
ejecutamos la imagen para crear el contenedor con:
```bash
  sudo docker-compose up -d #la flag permite seguir usando la terminal
```
Una vez hecho esto podemos acceder tipeando en el navegador:

```bash
  http://localhost:5020
```

Y para cerrarla con:
```bash
  sudo docker-compose stop
```
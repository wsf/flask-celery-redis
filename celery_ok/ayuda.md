# Problema
Cuello de botella


# Solución
Encolar 

## Arquitectura de la solución

# Herramientas técnicas
Ce

# Instalaciones

- Flask
  - `pip intall flask`
- Celery
  - celery
    - `pip install celery`
  - monitor
    - `pip install flower`
- Redis
  - Instalar servidor
    - `sudo apt install redis-server`
    - configurar server 
      - sudo nano /etc/redis/redis.conf
    - poner a correr el servicio redis
      - `sudo systemctl restart redis.service`
      - `sudo systemctl status redis`
      
  - Instalar módulo python
    - `pip install redis`
- Gunicorn
  - `pip install gunicorn`


# Arquitectura 
Implementación

# Configuración 


# Ejecución

## Ejecutamos el flask
gunicorn app:app 

## Ejecutamos el worker de celery

celery -A nombre_archivo worker --loglevel=info

> Ejemplo concreto: celery -A worker worker --loglevel=info


## Ejecutamos el monitor del worker de celery 

celery -A nombre_archivo flower --port=5555
> Ejemplo concreto: celery -A worker flower --port=5555

# Referencias
- Celery 
https://testdriven.io/courses/flask-celery/getting-started/

https://github1s.com/miguelgrinberg/flask-celery-example/blob/HEAD/app.py

https://github1s.com/katanaml/sample-apps/blob/master/11/README.md
# tutorial-flask
Repositorio para seguir el tutorial de Flask de https://j2logo.com/tutorial-flask-espanol/


1. [La primera aplicación Flask](https://j2logo.com/leccion-1-la-primera-aplicacion-flask)
2. [Uso de plantillas para las páginas HTML](https://j2logo.com/tutorial-flask-leccion-2-plantillas)
3. [Uso de formularios en Flask](https://j2logo.com/tutorial-flask-leccion-3-formularios-wtforms)
4. [Login de usuarios en Flask](https://j2logo.com/tutorial-flask-leccion-4-login)
5. [Añadiendo una base de datos: SQLAlchemy](https://j2logo.com/tutorial-flask-leccion-5-base-de-datos-con-flask-sqlalchemy)
6. [Estructura de un proyecto con Flask. Blueprints](https://j2logo.com/tutorial-flask-leccion-6-estructura-proyecto-flask-blueprints)
7. [Parámetros de configuración de un proyecto Flask](https://j2logo.com/tutorial-flask-leccion-7-parametros-de-configuracion-proyecto)
8. [Gestión y manejo de errores y excepciones](https://j2logo.com/tutorial-flask-leccion-8-gestion-manejo-errores-excepciones)
9. [Logs en Flask](https://j2logo.com/tutorial-flask-leccion-9-logs-en-flask)
10. [Añadiendo seguridad en las vistas](https://j2logo.com/tutorial-flask-leccion-10-anadiendo-seguridad-vistas-decoradores)
11. [Actualizar la base de datos SQLAlchemy](https://j2logo.com/tutorial-flask-leccion-11-actualizar-base-de-datos-sqlalchemy)
12. [Test con Flask](https://j2logo.com/tutorial-flask-leccion-12-tests-con-flask-unittest)
13. [Paginar las consultas de base de datos](https://j2logo.com/tutorial-flask-leccion-13-paginar-las-consultas-de-base-de-datos)
14. [Enviar emails con Flask](https://j2logo.com/tutorial-flask-leccion-14-enviar-emails-con-flask)
15. [Trabajar con Fechas en Flask](https://j2logo.com/tutorial-flask-leccion-15-trabajar-con-fechas-en-flask)
16. [Procesar ficheros en Flask](https://j2logo.com/tutorial-flask-leccion-16-procesar-ficheros-en-flask)
17. [Desplegar una aplicación Flask en producción con Nginx + Gunicorn](https://j2logo.com/tutorial-flask-leccion-17-desplegar-flask-produccion-nginx-gunicorn)


## Flask-Migrate

### Los tres comandos principales de Flask-Migrate son:

- flask db init: Crea una estructura de directorios y ficheros necesarios para la ejecución de esta extensión. Se ejecuta solo una vez, al principio.
        $> flask db init

- flask db migrate: Navega entre los modelos en busca de actualizaciones y genera los ficheros de migración de base de datos con los cambios detectados.
        $> flask db migrate -m "Initial database"

- flask db upgrade: Lleva a cabo la migración de la base de datos.
        $> flask db upgrade

### En resumen, los pasos para usar Flask-Migrate son:

    1. Crea tus modelos iniciales.
    2. Crea la base de datos
    3. Ejecuta el comando init.
    4. Ejecuta el comando migrate.
    5. Revisa el código del fichero que contiene las instrucciones para la migración y verifica que está todo correcto.
    6. Ejecuta el comando upgrade.
    7. Realiza cambios en tus modelos.
    8. Vuelve al PASO 4.

    
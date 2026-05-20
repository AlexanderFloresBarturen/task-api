# Task API

API REST construida con Python y FastAPI para gestionar tareas y usuarios.

## Objetivo

Este proyecto tiene como objetivo practicar y demostrar conocimientos de:

- Desarrollo backend
- APIs REST
- Python
- Autenticación
- Bases de datos
- Docker
- Buenas prácticas de desarrollo

Además, el proyecto sirve como base para explorar conceptos relacionados con seguridad web y APIs.

## Tecnologías

- Python
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- SQLite
- Passlib
- bcrypt
- python-jose
- JWT
- python-dotenv

## Estructura del proyecto

```text
task-api/
│
├── app/
│   ├── config.py
│   ├── main.py
│   │
│   ├── auth/
│   │   ├── dependencies.py
│   │   ├── jwt_handler.py
│   │   └── security.py
│   │
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── task_crud.py
│   │   └── user_crud.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── conection.py
│   │   └── dependencies.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task_model.py
│   │   └── user_model.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── tasks.py
│   │   └── users.py
│   │
│   └── schemas/
│       ├── __init__.py
│       └── task.py
│       └── user.py
│
├── .env
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Readme.md
└── requirements.txt
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/AlexanderFloresBarturen/pentesting-book/tree/main/Proyectos/task-api

cd task-api
```

Crear entorno virtual:

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Iniciar el servidor:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

Documentación automática:

```text
http://127.0.0.1:8000/docs
```

## Estado del proyecto

🚧 En desarrollo

### Progreso actual

- [x] Configuración inicial
- [x] FastAPI funcionando
- [x] Documentación automática
- [x] Task endpoints
- [x] Base de datos
- [x] CRUD de tareas
- [x] Menejo de errores
- [x] Registro de usuarios
- [x] Password hashing
- [x] User login
- [x] Generación JWT
- [x] Autenticación JWT
- [x] Protección de endpoints
- [x] Propiedad de tareas por usuario
- [x] Variables de entorno
- [x] Separación de la capa CRUD
- [x] Estructura limpia de route
- [x] Docker

## Aprendizajes

- Si aparece alguna advertencia sobre algún import, lo podemos solucionar abriendo la paleta de comandos (Ctrl+Shift+P) y ejecutando `Developer: Reload Window`, esto forzará de Pylance para que vuelva a escanear el proyecto y los paquetes instalados.
- Se encontró un problema de compatibilidad entre `passlib` y `bcrypt 5.x`.
- Se fijó `bcrypt==4.0.4` para mantener la compatibilidad durante el desarrollo.
- Verificaciones de seguridad para prevenir que usuarios consulten tareas que no son de su propiedad (IDOR).
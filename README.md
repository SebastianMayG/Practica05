# Práctica 5: Pruebas Automatizadas a API Web (JSONPlaceholder)

## 📋 Endpoints Probados
Se han automatizado los flujos CRUD (Crear, Leer, Actualizar, Eliminar) para:
- `/posts`
- `/todos`
- `/albums`

## ⚙️ Instalación y Configuración

Sigue estos pasos para configurar el entorno en tu máquina local:

### 1. Clonar el repositorio (o descargar los archivos)
Asegúrate de tener los archivos `.py` y `requirements.txt` en una carpeta.

### 2. Crear y activar un entorno virtual (Recomendado)
Para no afectar las librerías de tu sistema principal:

**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
### 3. Instalar las dependencias
pip install -r requirements.txt

### 4. Ejecutar el script
pytest -v test_posts.py

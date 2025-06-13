
---
### 🔹 `bash/backup.sh`
Script para generar respaldos automáticos de una base de datos o archivos críticos.

- Usa `tar` y `cron`
- Permite logs diarios
- Parametrizable

### 🔹 `bash/deploy.sh`
Automatiza despliegues en servidores remotos usando `scp` y `ssh`.

### 🔹 `python/conectar_azure.py`
Conecta a una base de datos SQL en Azure usando `pyodbc`.

- Lee variables desde `.env`
- Ejecuta queries simples

### 🔹 `python/validaciones.py`
Realiza validaciones automáticas en tablas: nombres nulos, tipos de datos, etc.

---

## 🚀 Requisitos

- Python 3.x
- Bash (Linux/macOS o Git Bash en Windows)
- Conexión a internet para acceso a Azure
- Paquetes: `pyodbc`, `dotenv`

Instalación rápida (Python):

```bash
pip install -r requirements.txt


# SCRIPTS

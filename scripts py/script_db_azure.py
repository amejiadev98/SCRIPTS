import os
from pathlib import Path
from datetime import datetime
from azure.storage.blob import BlobServiceClient

# ======================== CONFIGURACIÓN GENÉRICA ==========================
STORAGE_ACCOUNT_NAME = "TU_CUENTA_STORAGE"
STORAGE_ACCOUNT_KEY = "TU_LLAVE_STORAGE"  # Se recomienda usar variable de entorno en producción
CONTAINER_NAME = "TU_CONTENEDOR"
LOCAL_DOWNLOAD_PATH = "C:\\ruta_local\\ultimo_backup.sql.gz"  # Cambiar por la ruta deseada

# ======================== CONEXIÓN A AZURE ==========================
blob_service_client = BlobServiceClient(
    account_url=f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net",
    credential=STORAGE_ACCOUNT_KEY
)

container_client = blob_service_client.get_container_client(CONTAINER_NAME)

# ======================== FUNCIONES ==========================
def obtener_blobs_ordenados_por_fecha(container_client):
    blobs = list(container_client.list_blobs())
    return sorted(blobs, key=lambda b: b.creation_time)

def descargar_ultimo_blob(container_client, ruta_local):
    blobs_ordenados = obtener_blobs_ordenados_por_fecha(container_client)
    if not blobs_ordenados:
        print("No hay blobs disponibles.")
        return None

    ultimo_blob = blobs_ordenados[-1]
    blob_client = container_client.get_blob_client(ultimo_blob.name)

    with open(ruta_local, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    print(f"El archivo '{ultimo_blob.name}' ha sido descargado a '{ruta_local}'")
    return ruta_local

# ======================== EJECUCIÓN ==========================
print("Buscando el último archivo en Azure Blob Storage...")
descargar_ultimo_blob(container_client, LOCAL_DOWNLOAD_PATH)

# ======================== LISTAR BACKUPS LOCALES ==========================
directorio_local_backups = Path("C:\\ruta_local\\")  # Cambiar por tu carpeta de backups
archivos_locales = sorted(
    [f for f in directorio_local_backups.rglob("*.sql.*") if f.is_file()],
    key=lambda x: x.stat().st_mtime,
    reverse=True
)

print("Backups locales encontrados:")
for archivo in archivos_locales:
    fecha = datetime.fromtimestamp(archivo.stat().st_mtime)
    print(f"- {archivo.name} | Última modificación: {fecha}")

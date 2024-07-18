@echo off
set POSTMAN_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
set COLLECTION_UID=6064096-511f5e5a-a1b3-44ff-9627-2a2a0f235c3b
set ENVIRONMENT_UID=6064096-a2c90317-53c0-4c29-a5fd-5123b5ce3a88
set COLLECTION_PATH=collection.json
set ENV_PATH=environment.json
set REPORT_PATH=reporte.html

:: Descargar la colección
curl --header "X-Api-Key: %POSTMAN_API_KEY%" https://api.getpostman.com/collections/%COLLECTION_UID% > %COLLECTION_PATH%

:: Descargar el entorno
curl --header "X-Api-Key: %POSTMAN_API_KEY%" https://api.getpostman.com/environments/%ENVIRONMENT_UID% > %ENV_PATH%

:: Ejecutar Newman con el reporte htmlextra
newman run %COLLECTION_PATH% -e %ENV_PATH% -r htmlextra --reporter-htmlextra-export %REPORT_PATH%

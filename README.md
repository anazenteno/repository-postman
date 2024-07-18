TODOIST
**************************************************************************************
Instrucciones para Configurar y Ejecutar Pruebas Automatizadas de API en Postman
**************************************************************************************
# Requisitos Previos
  	1. Instalación de Postman: Asegúrate de tener la última versión de Postman 
  	   instalada. Puedes descargarla desde aquí.(https://www.postman.com/)

	2. Node.js y Newman: Instala Node.js desde aquí (https://nodejs.org/en).Newman es 
	   el CLI de Postman y puede ser instalado utilizando npm (el gestor de paquetes de Node.js).

		Ejecutar por consola 
		Instalar newman
		-------------------------------------------------------------------------------
		- npm install -g newman
		-------------------------------------------------------------------------------
		Instalar newman reporter htmlextra para generar reportes en HTML
		-------------------------------------------------------------------------------
		- npm install -g newman-reporter-htmlextra
		-------------------------------------------------------------------------------

# Archivo JSON de Colección de Postman
	1. Descargar Archivo JSON: Descarga el archivo JSON de la colección y ambiente de
	   Postman desde el siguiente enlace
	   --------------------------------------------------------------------------------
	   - Todoist.postman_collection.json
	   - Todoist-Tasks.postman_environment.json
	   --------------------------------------------------------------------------------

# Configuración en Postman
	1. Importar la Colección:
		- Abre Postman.
		- Haz clic en Import en la parte superior izquierda.
		- Selecciona Upload Files y elige el archivo JSON descargado.
		- Haz clic en Import.

	2. Verificar Variables de Entorno:
		- Algunas pruebas pueden requerir variables de entorno. Asegúrate de tener 
		  configuradas las variables de entorno necesarias en Postman.
		- Importa el archivo de entorno si es necesario:

# Ejecución de Pruebas en Postman	
	1. Ejecutar Manualmente:
		- Selecciona la colección importada.
		- Haz clic en Run para abrir el Collection Runner.
		- Selecciona el entorno adecuado si es necesario.
		- Haz clic en Start Run para ejecutar las pruebas.

# Ejecución de Pruebas con Newman HTML
	1. Descargar el script .bat para windwos
	   -------------------------------------------------------------------------------
	   - collection-todoist.bat
	   -------------------------------------------------------------------------------
	3. Abrir el script collection-todoist.bat con editor de texto y en el sector 
	   POSTMAN_API_KEY modificar la informacion con el API Key de postman y guardar.
	   -------------------------------------------------------------------------------
	   - set POSTMAN_API_KEY= XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	   -------------------------------------------------------------------------------
	   Nota:
	    - Tienes que genera tu API Key en Postman

	2. Ejecutar el script haciendo doble click en el collection-todoist.bat y se
	   generara el reporte en el navegador

# Notas Adicionales
	1. Documentación: Revisa la documentación oficial de Postman y Newman para más 
	   detalles y opciones avanzadas.
	2. Soporte: Si encuentras problemas o tienes preguntas, no dudes en contactar con 
	   mi persona.
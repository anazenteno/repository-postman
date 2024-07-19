# TODOIST
Instrucciones para Configurar y Ejecutar Pruebas Automatizadas de API en Postman

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
	1. Clonar el repositorio del proyecto Postman
	   --------------------------------------------------------------------------------
	   - git clone https://github.com/anazenteno/repository-postman.git
	   --------------------------------------------------------------------------------

# Configuración en Postman
	1. Importar la Colección:
		- Abre Postman.
		- Haz clic en Import en la parte superior izquierda.
		- Selecciona  los dos archivos JSON.
		- Haz clic en Import.

# Ejecución de Pruebas en Postman	
	1. Ejecutar Manualmente:
		- Selecciona la colección importada.
		- Haz clic en collection Todoist 3 puntos
		- Haz click en editar ir seccion Authorization selecionar Authorization el tipo de auth Bearer Token 
		- Ingresar el api token que la app Todoist te proporciona
		  esta es la ruta don se encuentra el api token 
		  tu_cuenta_todoist->configuracion->integraciones->desarrolladores.
		- Guardar cuando se introduce el API token
		- Haz clic en Run para abrir el Collection Runner.
		- Selecciona el entorno Todoist-Tasks.
		- Haz clic en Start Run para ejecutar las pruebas.
		

# Ejecución de reportes con Newman HTML
	3. Abrir el script collection-todoist.bat con editor de texto y cambiar los 
	   siguientes datos: 
	   -------------------------------------------------------------------------------
	   - set POSTMAN_API_KEY= XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  Cambiar esto con API Key de postman
	   - set COLLECTION_UID= XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  Cambiar esto por lo generado en postman
	   - set ENVIRONMENT_UID= XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  Cambiar eto por lo generado en portman
	   -------------------------------------------------------------------------------
	   Nota:
	    - Tienes que genera tu API Key en Postman
	    - Para obtner el UID collecion ejecutar este requiest para postman https://api.getpostman.com/collections
	      y autentificarte con el API Key de postman
	    - Para obtner el UID environments ejecutar este requiest para postman https://api.getpostman.com/environments
	      y autentificarte con el API Key de postman 
	    - Guardar todos los cambios en el script.
	
	3. Ejecutar el script haciendo doble click en el collection-todoist.bat y se
	   generara el reporte, dentro del carpte clonada donde se encuenta el script vera 
	   diferentes archivos entre estos hay uno con icono del navegador abrir esto y vera
	   el reporte que se ejecuto
	   -------------------------------------------------------------------------------
	   - collection-todoist.bat
	   -------------------------------------------------------------------------------
	   Nota: Se creo este script para ejecutar de una manera mas facil los reportes sin la necesidad
	   de estar descargando el Json de postman este script lo hace directo y cualquier modificacion 
	   que se haga en los request y se ejecute el reporte se reflejara los cambios. 

# Notas Adicionales
	1. Documentación: Revisa la documentación oficial de Postman y Newman para más 
	   detalles y opciones avanzadas.
	2. Soporte: Si encuentras problemas o tienes preguntas, no dudes en contactar con 
	   mi persona.
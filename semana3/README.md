# curso-calidad-de-software

## semana 3 
### actividad1: Crear un job que imprima su nombre completo y posteriormente clone un repositorio donde ejecute un alguno de los test unitarios sencillos usados en la primera semana (o si desea usar un proyecto existente en cualquier otra tecnologia que ejecute test lo puede hacer), entregable capturas de pantalla de la ejecución del job
![Screenshot 2024-12-20 195502](https://github.com/user-attachments/assets/4c86bfc6-69ee-45d5-a791-a202404e85b8)

### Actividad 2 - Del job de la actividad anterior configurar la notificación por correo cuando falle, y cambiar el mensaje que se agrego al template de prueba jenkis por su nombre completo, subir al repositorio un cambio con un test fallando, ejecutar el job, se debe tomar captura de pantalla a la ejecución del job y al mail recibido.

configuracion smtp
![Screenshot 2025-01-09 153312](https://github.com/user-attachments/assets/d287db5d-a2eb-449f-a9ee-f8d3b724fe90)

evidencia de envio:
![send_email_jenkinx](https://github.com/user-attachments/assets/20a3059e-8928-4d4a-887a-ba4bd8e39705)

estoy tratando de usar el sevidor smtp de outlook pero falla en jenkins por que no tiene activo el uso de STARTTLS

### actividad 3
Actividad 3- Crear un repositorio que contenga test automatizados de selenium (minimo 5, que sean elaborados, ejemplo, llenar formulario, extraer informacion) con sus respectivos test unitarios, debe estar integrado con jenkis, donde vez que haga push a la rama de desarrollo o develop solo a esa, ejecute los siguientes pasos, preparacion del entorno (instalacion de dependencias), ejecución de test unitarios, esto debe estar en un archivo de jenkis (Jenkisfile), debe mostrar el estatus de la ejecucion de los trabajos desde github, y si falla me deve enviar un correo electronico indicando que ha fallado la ejecucion. El entregable es un video corto, maximo 5 min, mostrando y explicando el flujo
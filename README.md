# post-sl-ugr
Dame posts y te diré de quienes son
--
Tarea
--
La tarea no es complicada, para cada post que aparece en la página principal del blog de la Oficina de Software Libre de la UGR, deberás obtener lo siguiente:

    Título.
    Autor.
    Contenido.
    Lista de categorías.
    Lista de etiquetas.

Estos datos deberán ser almacenados en algún fichero (por ejemplo en formato XML), y si alguna de estas entradas no tiene asignada ninguna etiqueta, almacenar los datos en otro fichero distinto (también puede ser en formato XML).

Entrega
--
Tienes dos formas de poder entregar la tarea, que son las siguientes:
- Archivo comprimido.
  Comprime el directorio de la tarea con TODOS los ficheros que se generen y súbelo a la plataforma.
- Uso de una forja.
 Si decides subir el código a una forja, entrega un fichero de texto con la url donde está alojado. Continua leyendo el apartado de la evaluación.

Evaluación
--
- Si el proyecto no funciona la valoración no será más de 50/100.

- Si se usa GITHUB desde la primera línea de código que se escribe (no es buena práctica subir todo el proyecto con un sólo commit & push) la valoración será triplemente positiva. Puedes añadirme en GITHUB como 'seravb'.

- Así el diseño del scraper se valorará en un 50% y el otro 50% se valorará sobre el control de eventos, funciones, controlar errores básicos, control de excepciones...

- Si los resultados obtenidos aparte de almacenarlos en un fichero XML o JSON los guardas de forma que se cree un fichero HTML y que en este aparezca una tabla con los datos formateados este aspecto se valorará altamente. Recomendación: No te compliques y almacena los datos básicos y más simples en la tabla si no quieres que se muestre todos los datos que si son básicos para el formato de exportación.

INSTALACION
==
	git clone https://github.com/deepb/post-sl-ugr.git
	cd post-sl-ugr
	scrapy crawl PostGrabber -o posts.xml
	

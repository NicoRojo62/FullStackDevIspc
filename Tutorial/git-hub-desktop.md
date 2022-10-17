# Git Hub Desktop

## Clonar un Repositorio

Comenzamos clonando un repositorio:

Nos apretamos la opción `clone repository...`

![image](https://user-images.githubusercontent.com/95236196/196178253-47e0c418-fe28-4ac8-8cf2-86517f57a706.png)

Y nos abrirá el siguiente menú. Por defecto estaremos en la sección `Gitihub.com` y debemos ir a `URL` como en la siguiente imágen, y elegimos el "Local path" que es donde colocaremos el archivo, y elegí una carpeta llamada "Prueba Git Hub" (El repositorio creará otra carpeta dentro con el nombre del mismo) y le damos click en `Clone`

![image](https://user-images.githubusercontent.com/95236196/196178846-3b3d8cd1-f3ac-4c5a-aef7-0ad5afd3ce3d.png)

Luego copiamos el link del repositorio en la parte de clone (lo dejaré abajo para que puedas copiarlo de aqui mismo)

![image](https://user-images.githubusercontent.com/95236196/196179456-04b2343e-3336-4f47-83b5-e72a1f2b6d23.png)

```
https://github.com/NicoRojo62/FullStackDevIspc.git
``` 

Así podremos ver que se agregó la carpeta "FullstackDevIspc", tanto localmente commo en el menú lateral izquierdo de Git Hub Desktop

![image](https://user-images.githubusercontent.com/95236196/196179845-0fd3d0c2-826a-4326-b16a-d82eae6694a8.png)

![image](https://user-images.githubusercontent.com/95236196/196179941-324e31b2-c216-422b-b71c-f91c05468df8.png)

Podemos ver las branches que tenemos diposnibles en el siguiente menú:

![image](https://user-images.githubusercontent.com/95236196/196180083-b0943e5c-dbb6-4f13-ae51-5b535068808a.png)

Y si me paro en la branch de `desarrollador-facumd`

![image](https://user-images.githubusercontent.com/95236196/196181520-2acb4315-12f4-463a-806c-b2d7b35b7dbc.png)

Voy a ver en mi local cierta disposición de carpetas y archivos de acuerdo a lo que haya en esa branch

![image](https://user-images.githubusercontent.com/95236196/196181687-db9b6cef-599b-4fb9-a5df-6f724d3e21cc.png)

> **Nota Importante** Siempre antes de comenzar a realizar algún cambio es recomendable hace run `Fetch origin` para traer cualquier cambio que hubiera a nivel remoto, y así tener nuestra branch actualizada (En este caso, no hay necesidad de hacerlo porque acabamos de clonar el repositorio).

> Por otro lado también hay que tener en cuenta que es bueno siempre traer los cambios del main a mi rama antes de comenzar a trabajar en ella.

![image](https://user-images.githubusercontent.com/95236196/196184218-39c63b73-b8c7-40d7-9c75-8a28dd4cb450.png)

---------

Volviendo a lo anterior... su canmbui de la rama en la que me encontraba a la otra como por ejemplo: `Alicia-Viviana-Montenegro`

![image](https://user-images.githubusercontent.com/95236196/196180424-dddb085c-a76d-4ba9-8380-9cae88198f11.png)

Cuando vaya a mi carpeta local veré como habíamos dicho otra disposición de los archivos según la organización que tiene esta rama.

![image](https://user-images.githubusercontent.com/95236196/196180349-c3c80eee-26eb-44aa-b30a-cd6ca4229a71.png)

## Realizar Cambios

En el caso de querer realizar un cambio para luego pushearlo al main, lo hago de la siguiente manera: Muevo, organizo o edito los archivos en mi carpeta local (En este caso estamos moviendo el archivo "ModeloRealcional.pdf" a la carpeta "Documentación")

![image](https://user-images.githubusercontent.com/95236196/196181848-9b2f61ff-5ac8-4003-b381-03d19e008086.png)

Git Hub Desktop notará los cambios y los listará en el menú lateral izquierdos, si están tildados en azul, quiere decir que incluiré esos cambios en el commit que posteriormenteharé:

![image](https://user-images.githubusercontent.com/95236196/196181952-4a76f668-fec6-4d76-9cf8-c7e267799e36.png)

Es una buena practica escribir los commits en verbo infinitivo, deben ser corto y explicar que se está haciendo y porqué:

- En el Título: explicamos que estamos haciendo

- Y en al Descripción (Esta es opcinal): Explicamos porqué lo estamos haciendo en un pequelo y resumido msj

![image](https://user-images.githubusercontent.com/95236196/196182341-f9c0130f-fb05-46ad-81ca-b366557f671e.png)

Yo no voy a commitear esto, porque no es mi branch en este caso y quiero que el su dueño haga dicho commit...

Pero voy a commitear a mi rama, este tutorial de la siguiente manera:

Agrego en mi local el archivo que quiero subir al remoto...

![image](https://user-images.githubusercontent.com/95236196/196182955-8e4b82cf-d7ca-414c-bf9a-80d792e090e4.png)

Y commiteo los cambios que estoy haciendo

![image](https://user-images.githubusercontent.com/95236196/196183227-1c3b3f08-921b-4632-929b-26196374e107.png)

Una vez que hicimos click en `Commit to desarrollador-facumd` ya subimos el commit, y hasta podemos deshacerlo (`Undo`), pero aun no esta pusheado a la rama remota.

![image](https://user-images.githubusercontent.com/95236196/196183377-78a6bba7-da16-42df-aec3-7755d6681341.png)


Le damos push Origin y listo.

![image](https://user-images.githubusercontent.com/95236196/196183559-d157cc34-58d6-4f70-86db-1f2f89c7485c.png)

Ahora podemos ver en el repositorio remoto, los cambios subidos

![image](https://user-images.githubusercontent.com/95236196/196183955-8726aaf0-9bda-40aa-95a0-1cdba677ae92.png)
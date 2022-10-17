# Repaso Git Consola

[Mini Tutorial de GitHub Desktop](./git-hub-desktop.md#git-hub-desktop)

Esto un simple repaso para quien pudiera servirle recordar los pasos, a la hora de crear branches en un repositorio remoto:

Primero debemos clonar el repositorio en nuestro Local:

![image](https://user-images.githubusercontent.com/95236196/195966529-456d94fb-24f7-4153-bec9-6b3076bfb346.png)


Creamos una carpeta donde queremos que vaya, y luego allí le damos `git bash`

![image](https://user-images.githubusercontent.com/95236196/195966577-2adcb3e5-9054-454b-bc17-6c769fa6a7ee.png)

Una vez en la consola de git, colocamos el comando para clonar el repo:

```
git clone https://github.com/NicoRojo62/FullStackDevIspc.git
```

Y se creará otra carpeta con el nombre que vemos allí arriba: **FullStackDevIspc** (Se llamrá según el nombre del repositorio que creamos)

Para entrar a esa carpeta usamos el comando `cd` (change directory)

> Con la tecla `tab`, el nombre de la carpeta se autocompleta para que no tengamos que escribirla

```
git cd FullStackDevIspc
```

![image](https://user-images.githubusercontent.com/95236196/195966779-45ad0a40-76e9-46ff-acc6-78c07936d021.png)

Una vez allí podemos crear nuestra rama con el nombre que deseemos. En mi caso voy a crear una con el nombre de `desarrollador-facumd`

```
git branch desarrollador-facumd
```

Y con el comando `git branch`, veremos las ramas que de las cuales ahora disponemos

```
git branch
```

![image](https://user-images.githubusercontent.com/95236196/195966814-59b2a3ee-0aa0-420d-b6ad-e33a8a2e77d1.png)

Luego nos cambiamos de la rama main, en la cual nos encontraremos por defecto a la rama que creamos con anterioridad.

```
git checkout desarrollador-facumd
```

![image](https://user-images.githubusercontent.com/95236196/195966854-e3f0f99e-9ee7-499f-8861-f1aeacaad81c.png)

Ahora estaremos parados en nuestra rama y para subirla al remoto, usaremos el comando git push

```
git push
```

ó

```
git push origin
```

Pero esto nos dará un error porque, no la rama no existe en el repositorio remoto, y este mismo incluso no está seteado.

Por lo que git-hub nos da un comando para Subirla, y setear el "upstream", el comando es el siguiente pero a diferencia que llevará el nombre de tu rama.

![image](https://user-images.githubusercontent.com/95236196/195967028-fd6cfb2e-5b7a-4c1e-b78b-4fbb7bad6f14.png)


```
git push --set-upstream origin desarrollador-facumd
```

Y tendremos el siguiente mensaje:

![image](https://user-images.githubusercontent.com/95236196/195967094-aba27d00-023f-40e4-9729-aa4f212b70c6.png)

Resultado:

![image](https://user-images.githubusercontent.com/95236196/195967224-935d5d07-1bb1-42f8-8fab-b19f07c50a75.png)
# Pype
> BOT de Discord multipropósito escrito en Python.
## Estructura de directorios (carpetas)
### data
> Archivos usados para el cambio de estado del bot. Modificables a gusto del consumidor.<br>

### images
> **animageslib** - Todos los gifs de las interacciones de anime.<br>
> **assets** - Assets tipo logos y cosas así. Su nombre tiene que coincidir con el de ```config.py```.<br>
> **hentaimages** - Lo mismo que ```animageslib``` pero con imágenes hentai...<br>

### src
> Como su propio nombre indica incluye el source code.
> **bot.py** - Archivo principal. No tocar nada a menos que sepas lo que haces, en ese caso adelante, por algo es freeware.<br>
> **config.py** - Archivo de configuración donde deberás introducir datos para que el bot funcione según lo deseado.<br>

## Comandos de Pype
### Varios
> **/help** - Muestra un menú de ayuda en un embed.<br>
> **/info** - Muestra la info del servidor.<br>
> **/yt** - Busca un vídeo en YouTube.<br>
> **/say** - Manda un mensaje a través del bot.<br>
> **/platano** - Mira a ver cuánto mide tu plátano. 😳<br>
> **/dado** - Tira un dado de 6 caras.<br>
> **/moneda** - Tira una moneda al aire.<br>
> **/avatar** - Renderiza el avatar de un miembro del servidor.<br>
> **/spam** - Spammea a un miembro del servidor. 😈<br>
> **/oooh** - Oooohh! ✋🏼<br>
> **/spank** - Dale una nalgada a un miembro.<br>
> **/carey** - Feliz navidad :v<br>

### Interacción
> **/amb** - Llama a una ambulancia.<br>
> **/dance** - Ponte a bailar!<br>
> **/fbi** - Llama al FBI.<br>
> **/hug** - Abraza a alguien uwu.<br>
> **/kill** - Mata a alguien. D:<br>
> **/kiss** - Besa a alguien . >///<<br>
> **/pat** - Acaricia a alguien. nwn<br>
> **/run** - Corre!<br>
> **/sad** - Expresa tus tristes sentimientos. :(<br>
> **/slap** - Abofetea a alguien!<br>
> **/sleep** - A mimir.<br>
> **/fusilar** - Fusila a alguien como en los viejos tiempos.<br>
> **/hentai** - Manda una imagen hentai random. 😏<br>
> **/cum** - *Paso de explicar esto*<br>

### Operaciones matemáticas
> **/contar** - Cuenta desde a hasta b.<br>
> **/calc** - Calcula expresiones simples. (Ej.: +,-,/,*,**)<br>

### Gráficas
> **/sen** - Grafica una función seno.<br>
> **/cos** - Grafica una función coseno.<br>
> **/rect** - Grafica una función lineal.<br>
> **/pac** - Grafica una función cuadrática.<br>

### Música
> *Próximamente...*<br>

## Información adicional
Se pueden añadir comandos con la forma:

```
@bot.slash_command(name="", guild_ids="", description="")
async def command(ctx, *, optional_params):
    code
    return
```
⚠️ **IMPORTANTE: PARA AÑADIR IMÁGENES A SUS RESPECTIVOS DIRECTORIOS SERÁ NECESARIO RENOMBRAR LOS FICHEROS ÚNICAMENTE DE LA FORMA INDICADA EN DICHOS DIRECTORIOS O NO FUNCIONARÁ** ⚠️

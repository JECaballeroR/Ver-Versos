# Ver-Versos
_Imágenes poéticas por Inteligencia Artificial usando [CLIP](https://github.com/openai/CLIP) and [Unsplash](https://unsplash.com/)_

Disponible en:

http://3.20.221.95:8501/

[Proyecto Original de thoppe](https://github.com/thoppe/alph-the-sacred-river)

## Prepocesado de las nuevas imágenes

+ Descarga imágenes de Unsplash ([Mira aquí](https://github.com/unsplash/datasets))
+ Guarda cada imágnes cómo jpg en `data/source_images/`
+ Corre `python P0_encode_images.py` para computar los latents de la imágen

    
## Instrucciones para deploy en AWS


+ Crea una instancia de EC2, Ubuntu-Server, con al menos 12 GB de almacenamiento.

+ Clona el repositorio con:
```
git clone https://github.com/JECaballeroR/Ver-Versos.git
```
+ Corre en terminal:

```
sudo apt update 

sudo apt-get install python3-pip 

sudo su 

pip3 install streamlit

pip3 install plotly

exit 

cd Ver-Versos

sudo su 

pip3 install -r requirements.txt 

exit 

```
Lo anterior es para instalar todos los requisitos de la app cómo Super Usuario para poder correr los comandos posteriores correctamente.

+ Corre  (estando en la carpeta del repositorio clonado):
```
bash swap.sh
```
Esto agregará memoria Swap a la instancia de EC2 para permitirle correr la aplicación, dado que consume más recurso que el que ofrece gratuitamente Amazon (o cualquier proveedor de cloud computing).

+  Corre (estando en la carpeta del repositorio clonado):
```
tmux
uvicorn api:app --host 0.0.0.0 --port 9999 --reload
<Ctrl+B> <D>
```
Esto iniciará el proceso de la API de de los modelos en el puerto 9999, que es al que la aplicación enviará los Request, y lo deja corriendo aunque se cierre el terminal.

+  Corre (estando en la carpeta del repositorio clonado):
```
streamlit run streamlit_app.py
<Ctrl+B> <D>
```

Para iniciar la app, y dejarla corriendo aunque se cierre el terminal.

## Para correrlo local en Windows:

+ Es posible que haya que cambiar el host de 0.0.0.0 a 127.0.0.1

Además, dentro del código de streamlit_app.py, es posible que haya que cambiar elementos del código, en particular:

+ Que al abrir los archivos de texto, estos tengan encode utf-8 
+ El código para generar la lista de archivos .txt. Una opción puede ser usar glob y un replace:
```
import glob
files=glob.glob(known_poems_dest+'/*.txt')
txt_files=[x.replace('\\', '/') for x in files]
```

Es posible que se deba cambiar esta línea en los requirements.txt:

    pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    

## (Posible) To do

+ Los poemas no pueden tener dos versos iguales, o esto generá un problema con la API.
+ El refactoring del código para funcionar en AWS no ha sido propiamente documentado.
+ Arreglar el código para que no haya dos instancias de la API corriendo en la instancia (start_api.py).




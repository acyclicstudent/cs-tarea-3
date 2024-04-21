# cs-tarea-3
Tarea script python-nmap

En este repo se encuentra el script de la tarea 3, el cuál tiene el objetivo de utilizar nmap con python.

Requisitos previos:
- Tener Python 3 instalado.
- Tener pip y venv instalado. 

Para instalar el script (es necesario):
```
// Ingresar a la carpeta ráiz del repositorio
cd cs-tarea-3
// Instalar dependencias
python -m venv .env && source .env/bin/activate && pip install -r requirements.txt
```

Para ejecutar el script:
```
python main.py IP_HOST --port PORT --root --args ADDITIONAL_ARGS
```

El script recibe los siguientes argumentos:
- IP_HOST (Requerido): Dirección ip del host.
- PORT (Opcional): Puerto a escanear.
- ADDITIONAL_ARGS (Opcional): Argumentos adicionales que se pueden pasar a nmap.

Ademas se soportan las siguientes flags:
-r, --root (Opcional): Permite ejecutar el código como super usuario.
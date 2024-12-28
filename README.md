# Paintxel
Editor de imágenes para Pixel Art

## Requisitos
- Python 3.12.2
- Docker (opcional)

## Instalación

### Método 1: Instalación Local
1. Clonar el repositorio
2. Instalar las dependencias usando pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el programa con Python:
   ```bash
   python main.py
   ```

### Método 2: Usar Docker
1. Clonar el repositorio
2. Construir la imagen Docker:
   ```bash
   docker build -t paintxel .
   ```
3. Ejecutar el contenedor:
   ```bash
   docker run -it --rm \                                                                             01:32:10
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    paintxel
    ```
Para Linux:
1. Habilitar el acceso a X11 en el contenedor
```bash
xhost +local:docker
```
2. Ejecutar el contenedor
```bash
docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    paintxel
```
Nota: Si dice que no hay permisos, asegurarse de que el usuario este en el grupo docker


Para Windows:
1. Instalar VcXsrv Windows X Server
2. Configurar la variable DISPLAY apropiadamente
3. Ejecutar el contenedor con la configuración adecuada de DISPLAY

Para macOS:
1. Instalar XQuartz
2. Configurar la variable DISPLAY apropiadamente
3. Ejecutar el contenedor con la configuración adecuada de DISPLAY

## Notas sobre Docker
- La imagen usa Python 3.12.2 como base
- Incluye todas las dependencias necesarias para la interfaz gráfica (tkinter)
- El contenedor necesita acceso al sistema X11 para mostrar la interfaz gráfica
- Los archivos guardados persistirán solo mientras el contenedor esté en ejecución

## Licencia
MIT License - Ver archivo [LICENSE](LICENSE) para más detalles

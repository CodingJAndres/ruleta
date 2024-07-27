# Juego de Ruleta con Pistola

Este es un script en Python que simula un juego de ruleta con pistola. El juego presenta una representación ASCII de una pistola y te reta a elegir un número del 1 al 6. Si eliges el número que corresponde al "bala", se elimina un archivo de tu sistema. Si no eliges el número correcto después de varios intentos, se muestra un mensaje de victoria.

## Requisitos

- Python 3.x
- [colorama](https://pypi.org/project/colorama/) (para la gestión de colores en la consola)

## Instalación

1. **Clona o descarga el repositorio:**

    ```bash
    git clone https://github.com/CodingJAndres/ruleta.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd juego
    ```

3. **Instala las dependencias necesarias:**

    ```bash
    pip install colorama
    ```

## Uso

1. **Ejecuta el script:**

    ```bash
    python ruleta_rusa.py
    ```

2. **Introduce la ruta al archivo que deseas "poner en juego" cuando se te solicite.**

3. **Elige un número del 1 al 6 cuando se te pregunte.**

    - Si eliges el número que corresponde a la "bala", el archivo especificado será eliminado y perderás el juego.
    - Si no eliges el número correcto después de 4 intentos, ganarás el juego y se te proporcionará un enlace a una página web.

## Cómo Funciona

- **Arte ASCII:** Se muestra una imagen ASCII de una pistola al inicio del juego.
- **Entrada del Usuario:** Solicita al usuario que introduzca la ruta de un archivo y que elija un número del 1 al 6.
- **Juego:** Si el número elegido coincide con el número de la "bala", el archivo se elimina. Si no, el usuario tiene hasta 4 intentos para adivinar.
- **Mensajes:** Se muestran mensajes aleatorios para advertir al usuario antes de tomar cada decisión.

## Nota

- Asegúrate de introducir una ruta de archivo válida para evitar errores.
- Usa este script con precaución para evitar la eliminación accidental de archivos importantes.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

¡Diviértete jugando!

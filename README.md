# VLSM-Calculator-Calculadora-VLSM-
Este script Python utiliza Tkinter para una interfaz gráfica de usuario, implementando una Calculadora de Subredes VLSM. Permite planificar redes con máscaras de longitud de prefijo variable.

## Capturas de Pantalla:
[![Captura-de-pantalla-2024-01-21-132156.png](https://i.postimg.cc/7LPRV7F9/Captura-de-pantalla-2024-01-21-132156.png)](https://postimg.cc/Mn4tZcKf)

[![Captura-de-pantalla-2024-01-21-132216.png](https://i.postimg.cc/KzSMbrmr/Captura-de-pantalla-2024-01-21-132216.png)](https://postimg.cc/PLyxzDpP)

# Descripción:
## Lenguaje y Bibliotecas:
- Lenguaje: Python
- Bibliotecas: Tkinter (GUI), ipaddress (manipulación de IP).

# Estructura del Script
## Clase VLSMCalculator
- Configura la interfaz gráfica utilizando Tkinter.
- Divide la interfaz en tres secciones: Barra Superior, Menú Lateral y Cuerpo Principal.
- Proporciona controles para ingresar la dirección IP inicial, cantidad de subredes y número de hosts por subred.
- Permite calcular y visualizar los resultados de VLSM en una tabla.

## Métodos Principales
- `controles_barra_superior()`: Configura la barra superior de la interfaz.
- `controles_menu_lateral()`: Configura el menú lateral que incluye la entrada de dirección IP, la cantidad de subredes y la tabla de resultados.
- `controles_cuerpo()`: Configura el cuerpo principal de la interfaz que muestra la tabla de resultados.
- `actualizar_entries()`: Añade o elimina contenedores de entrada dinámicamente según la cantidad de subredes seleccionadas.
- `realizar_calculo()`: Calcula los resultados de VLSM según la información proporcionada.
- `calcular_vlsm()`: Realiza el cálculo de VLSM para obtener información detallada de las subredes.
- `calcular_mascara_hosts_utilizables()`: Calcula la máscara CIDR y la cantidad de hosts utilizables.

# Interfaz Gráfica
- Utiliza Tkinter para crear una interfaz gráfica intuitiva y fácil de usar.
- Permite ocultar/mostrar el menú lateral para proporcionar más espacio para la visualización de resultados.

# Ejecución del Script
- El script se ejecuta mediante la creación de una instancia de la clase VLSMCalculator.
- La interfaz gráfica se inicia con la función `run()`.

# Uso
1. Ingrese la dirección IP inicial y la cantidad de subredes requeridas.
2. Ingrese el nombre y el número de hosts para cada subred.
3. Haga clic en el botón "Calcular" para obtener los resultados de VLSM.
4. Los resultados se mostrarán en la tabla, incluyendo detalles como la dirección de red, máscara CIDR, hosts utilizables, etc.

# Notas Adicionales
- Se utiliza la fuente "Roboto" para la barra superior y la fuente "Terminal" para otras secciones de la interfaz.
- Se emplea FontAwesome para el ícono del botón del menú lateral.
- Se proporciona información del creador en la barra superior.

# Requisitos
- Python instalado (preferiblemente versión 3.x).

# Ejecución
```bash
python nombre_del_script_que_pongas.py

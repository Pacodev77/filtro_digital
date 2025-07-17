
# Trabajo Realizado Por Francisco Ruiz
# UCNL Señales y Sistémas

# Diseño e Implementación de Filtros Digitales en Python

Este proyecto tiene como objetivo crear señales de prueba (ruido blanco y señal compuesta), diseñar filtros digitales (FIR e IIR), aplicar dichos filtros y analizar los resultados mediante visualización.

##  Estructura del Código

### 1. Definición de la señal de entrada

- **Ruido blanco**: generado con distribución normal.
- **Señal compuesta**: suma de dos senoidales (50 Hz y 120 Hz).
- **Señal ruidosa**: combinación de la señal compuesta con ruido blanco.

### 2. Diseño de filtros digitales

Se diseñaron dos filtros pasa bajos:

#### a. Filtro IIR: Butterworth

- Orden: 5  
- Frecuencia de corte: 60 Hz  
- Método: `scipy.signal.butter`

#### b. Filtro FIR con ventana

- Número de coeficientes: 101  
- Ventana: Hamming  
- Método: `scipy.signal.firwin`

### 3. Aplicación de los filtros

Se utilizó `scipy.signal.lfilter` para aplicar los filtros a la señal ruidosa.

### 4. Visualización de los resultados

Se graficaron:

- La señal original y la señal con ruido.  
- Las señales filtradas por cada filtro.  
- La respuesta en frecuencia (magnitud) de cada filtro.

## Resultados Visuales

Se puede observar:

- La señal compuesta original (sin ruido).  
- La señal con ruido blanco añadido.  
- La señal filtrada por cada tipo de filtro.  
- Las curvas de atenuación de frecuencia de cada filtro.

## Requisitos

- Python 3.x  
- Numpy  
- Matplotlib  
- Scipy  # filtro_digital

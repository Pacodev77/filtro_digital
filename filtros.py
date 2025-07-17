import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 segundo

# Señal 1: Ruido blanco
np.random.seed(0)  # Para reproducibilidad
ruido_blanco = np.random.normal(0, 1, fs)

# Señal 2: Compuesta (50 Hz + 120 Hz)
f1, f2 = 50, 120
senal_compuesta = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Graficar señales
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, ruido_blanco)
plt.title("Señal de Ruido Blanco")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

plt.subplot(2, 1, 2)
plt.plot(t, senal_compuesta)
plt.title("Señal Compuesta (50 Hz + 120 Hz)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()

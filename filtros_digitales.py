
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, firwin, lfilter, freqz

# Parámetros de la señal
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 segundo

# Señal 1: Ruido blanco
np.random.seed(0)  # Para reproducibilidad
ruido_blanco = np.random.normal(0, 1, fs)

# Señal 2: Compuesta (50 Hz + 120 Hz)
f1, f2 = 50, 120
senal_compuesta = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Señal compuesta con ruido
senal_ruidosa = senal_compuesta + ruido_blanco * 0.3

# -----------------------------
# Filtro Butterworth Pasa bajos (IIR)
# -----------------------------
def butter_lowpass(cutoff, fs, order=5):
    nyq = fs / 2
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

cutoff = 60  # Frecuencia de corte
b_butter, a_butter = butter_lowpass(cutoff, fs)
senal_filtrada_butter = lfilter(b_butter, a_butter, senal_ruidosa)

# -----------------------------
# Filtro FIR Pasa bajos con ventana
# -----------------------------
def fir_lowpass(cutoff, fs, numtaps=101):
    nyq = fs / 2
    taps = firwin(numtaps, cutoff / nyq, window='hamming')
    return taps

taps_fir = fir_lowpass(cutoff, fs)
senal_filtrada_fir = lfilter(taps_fir, [1.0], senal_ruidosa)

# -----------------------------
# Respuesta en frecuencia de los filtros
# -----------------------------
w_b, h_b = freqz(b_butter, a_butter, worN=8000)
w_f, h_f = freqz(taps_fir, worN=8000)

# Graficar señales y respuestas de los filtros
fig, axs = plt.subplots(3, 2, figsize=(14, 10))

# Señales originales
axs[0, 0].plot(t, senal_ruidosa)
axs[0, 0].set_title("Señal compuesta + ruido blanco")
axs[0, 0].set_xlabel("Tiempo [s]")

axs[0, 1].plot(t, senal_compuesta)
axs[0, 1].set_title("Señal compuesta original")
axs[0, 1].set_xlabel("Tiempo [s]")

# Señales filtradas
axs[1, 0].plot(t, senal_filtrada_butter)
axs[1, 0].set_title("Filtrado con Butterworth (Pasa bajos)")
axs[1, 0].set_xlabel("Tiempo [s]")

axs[1, 1].plot(t, senal_filtrada_fir)
axs[1, 1].set_title("Filtrado con FIR (Pasa bajos, ventana Hamming)")
axs[1, 1].set_xlabel("Tiempo [s]")

# Respuestas en frecuencia
axs[2, 0].plot(w_b * fs / (2 * np.pi), 20 * np.log10(abs(h_b)))
axs[2, 0].set_title("Respuesta en Frecuencia - Butterworth")
axs[2, 0].set_xlabel("Frecuencia [Hz]")
axs[2, 0].set_ylabel("Magnitud [dB]")

axs[2, 1].plot(w_f * fs / (2 * np.pi), 20 * np.log10(abs(h_f)))
axs[2, 1].set_title("Respuesta en Frecuencia - FIR")
axs[2, 1].set_xlabel("Frecuencia [Hz]")
axs[2, 1].set_ylabel("Magnitud [dB]")

plt.tight_layout()
plt.show()

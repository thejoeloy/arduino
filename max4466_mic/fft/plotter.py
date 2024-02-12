import serial
import numpy as np
import matplotlib.pyplot as plt

# Initialize the serial port to read data from Metro Mini
ser = serial.Serial('/dev/ttyUSB0', 115200)

# Define the sample rate and the duration to capture data
fs = 1000  # Sample rate in Hz
duration = 2  # Capture for 2 seconds

n_samples = fs * duration
data = []

# Collect data from serial port
for _ in range(n_samples):
    line = ser.readline().strip()
    try:
        data.append(int(line))
    except ValueError:
        print(f"Skipping invalid data: {line}")

# Close the serial port
ser.close()

# Compute the FFT
freqs = np.fft.fftfreq(len(data), 1/fs)
fft_values = np.fft.fft(data)

# Only keep the positive frequencies
positive_freq_idxs = np.where(freqs > 0)
freqs = freqs[positive_freq_idxs]
fft_values = np.abs(fft_values[positive_freq_idxs])

# Plot the FFT
plt.figure()
plt.plot(freqs, fft_values)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT of MAX4466 Microphone Output")
plt.show()

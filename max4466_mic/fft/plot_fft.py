import serial
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def plot_fft_realtime(serial_port='/dev/ttyUSB1', baud_rate=115200):
    ser = serial.Serial(serial_port, baud_rate)
    fig, ax = plt.subplots()
    y_data = []

    N = 512  # Number of points for FFT
    fs = 1 / 0.001  # Sampling frequency based on the Arduino delay time

    def init():
        ax.set_xlim(0, fs // 2)  # Frequency range (Nyquist theorem)
        ax.set_ylim(0, 1000)  # FFT output range (change according to your needs)
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("FFT Magnitude")
        return

    def update(frame):
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                value = int(line)
                if len(y_data) >= N:
                    y_data.pop(0)
                y_data.append(value)
            except ValueError:
                print(f"Failed to parse: {line}")

        if len(y_data) == N:
            # Subtracting the mean from each data point to remove DC component
            y_data_zero_centered = np.array(y_data) - np.mean(y_data)
            
            fft_output = np.fft.fft(y_data_zero_centered)
            fft_magnitude = np.abs(fft_output)[:N // 2]
            fft_freq = np.fft.fftfreq(N, 1 / fs)[:N // 2]

            ax.clear()
            ax.plot(fft_freq, fft_magnitude)
            ax.set_xlabel("Frequency (Hz)")
            ax.set_ylabel("FFT Magnitude")

    ani = FuncAnimation(fig, update, init_func=init)
    plt.show()

if __name__ == "__main__":
    plot_fft_realtime()





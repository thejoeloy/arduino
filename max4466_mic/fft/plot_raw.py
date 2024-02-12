import serial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_sensor_output_realtime(serial_port='/dev/ttyUSB1', baud_rate=115200, sample_count=500):
    # Initialize the serial port to read data from Metro Mini
    ser = serial.Serial(serial_port, baud_rate)

    # Initialize the data array
    data = np.zeros(sample_count)

    # Initialize plot
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")
    ax.set_title("Real-Time Output of MAX4466 Microphone")
    plt.xlim(0, sample_count)
    plt.ylim(0, 1023)  # Assuming 10-bit ADC, change if different

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        nonlocal data
        line_serial = ser.readline().strip()
        try:
            value = int(line_serial)
            data = np.roll(data, -1)
            data[-1] = value
        except ValueError:
            print(f"Skipping invalid data: {line_serial}")

        x_data = np.arange(len(data))
        y_data = data

        line.set_data(x_data, y_data)
        return line,

    ani = FuncAnimation(fig, update, init_func=init, blit=False)

    plt.show()

    # Close the serial port
    ser.close()

# To start plotting in real-time, call the function like this:
plot_sensor_output_realtime()

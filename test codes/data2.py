import csv
import numpy as np
import serial
import time
from math import log2
from scipy.signal import hilbert
import matplotlib.pyplot as plt

# Establish serial connection with Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)  # Adjust serial port name and baud rate as needed

# Sampling frequency (adjust as needed)
sampling_freq = 1000  # Hz

# Open CSV file for writing
output_file = 'emg_parameters.csv'
csvfile = open(output_file, 'w', newline='')
fieldnames = ['Amplitude', 'Rise Time', 'Turns', 'Phase', 'Baseline Crossing', 'Duration']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

# Function to calculate baseline crossings
def calculate_baseline_crossings(amplitude, baseline_threshold=0.2):
    previous_amplitude = amplitude[0]
    crossings = []
    for i in range(1, len(amplitude)):
        if previous_amplitude < baseline_threshold and amplitude[i] >= baseline_threshold:
            crossings.append(i)  # Detect onset of muscle activity
        elif previous_amplitude > baseline_threshold and amplitude[i] <= baseline_threshold:
            crossings.append(i)  # Detect offset of muscle activity
        previous_amplitude = amplitude[i]  # Update the previous amplitude value
    num_crossings = len(crossings)
    return num_crossings, crossings

try:
    start_time = time.time()  # Start time for calculating signal duration

    while True:
        # Read EMG data from Arduino
        emg_data = float(ser.readline().decode().strip())

        # Calculate parameters
        amplitude = emg_data
        T10 = 0.1 * amplitude
        T90 = 0.9 * amplitude
        rise_time = (T90 - T10) / log2(10 / 90)

        # Calculate frequency from peak-to-peak amplitude and duration
        peak_to_peak_amplitude = ...  # Replace with the actual peak-to-peak amplitude
        duration = time.time() - start_time  # Calculate signal duration

        # Calculate the number of turns per phase
        turns_per_phase = sampling_freq / frequency

        # Calculate phase using Hilbert transform
        emg_signal = ...  # Load or generate EMG signal data
        analytic_signal = hilbert(emg_signal)
        phase = np.angle(analytic_signal)

        # Calculate baseline crossings
        num_crossings, crossings = calculate_baseline_crossings(amplitude)

        # Write parameters to CSV
        writer.writerow({'Amplitude': amplitude,
                         'Rise Time': rise_time,
                         'Turns': turns_per_phase,
                         'Phase': phase,
                         'Baseline Crossing': num_crossings,
                         'Duration': duration})

        # Print parameters (for debugging)
        print("Amplitude:", amplitude)
        print("Rise Time:", rise_time)
        print("Turns:", num_turns)
        print("Phase:", phase)
        print("Baseline Crossing:", num_crossings)
        print("Duration:", duration)
        print()

except KeyboardInterrupt:
    # Close serial connection and CSV file
    ser.close()
    csvfile.close()
    print("Output saved to:", output_file)

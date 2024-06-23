import csv
import numpy as np
import serial
import time
from math import log2

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

try:
    while True:
        # Read EMG data from Arduino
        emg_data = float(ser.readline().decode().strip())

        # Calculate amplitude
        amplitude = emg_data

        import numpy as np
        from scipy.signal import hilbert
        import matplotlib.pyplot as plt

        # Load or generate EMG signal data
        emg_signal = ...  # Load EMG signal data

        # Apply Hilbert transform to EMG signal
        analytic_signal = hilbert(emg_signal)
        phase = np.angle(analytic_signal)

        # Plot the original EMG signal and phase
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(emg_signal)
        plt.title('Original EMG Signal')

        plt.subplot(2, 1, 2)
        plt.plot(phase)
        plt.title('Phase of EMG Signal')

        plt.show()

        
        #rise_time
        T10 = 0.1 * amplitude
        T90 = 0.9 * amplitude
        rise_time = (T90 - T10) / log2(10 / 90)


        # Peak-to-Peak Amplitude of the EMG signal (in mV)
        # amplitude = 2.5  # Replace with the actual peak-to-peak amplitude

        # # Duration of the EMG signal (in seconds)
        # duration = 5  # Replace with the actual duration of the signal

        # # Calculate the period and frequency
        # period = duration / 1  # Assuming one cycle based on peak-to-peak amplitude
        # frequency = 1 / period

        # # Display the calculated frequency
        # print("Frequency of the EMG signal: {} Hz".format(frequency))



        # Sampling frequency of the EMG signal (in Hz)
        # sampling_frequency = 1000  # Replace with your actual sampling frequency

        # # Frequency of the EMG signal (in Hz)
        # emg_frequency = 50  # Replace with the actual frequency of the EMG signal

        # # Calculate the number of turns per phase
        # turns_per_phase = sampling_frequency / emg_frequency

        # # Display the result
        # print("Number of turns per phase:", turns_per_phase)


        import numpy as np

        # Define the baseline threshold (adjust this based on your signal characteristics)
        baseline_threshold = 0.2  # Replace with the actual baseline threshold value

        # Variable to store the previous amplitude value for comparison
        previous_amplitude = amplitude[0]  # Assuming amplitude is the variable storing real-time EMG signal data

        # Store the baseline crossing indices
        crossings = []

        # Iterate through the real-time amplitude data to detect crossings
        for i in range(1, len(amplitude)):
            if previous_amplitude < baseline_threshold and amplitude[i] >= baseline_threshold:
                crossings.append(i)  # Detect onset of muscle activity
            elif previous_amplitude > baseline_threshold and amplitude[i] <= baseline_threshold:
                crossings.append(i)  # Detect offset of muscle activity
            
            previous_amplitude = amplitude[i]  # Update the previous amplitude value

        # Count the number of crossings and display their indices
        num_crossings = len(crossings)
        print("Number of baseline crossings:", num_crossings)
        print("Crossing indices:", crossings)


        # Write parameters to CSV
        writer.writerow({'Amplitude': amplitude,
                         'Rise Time': rise_time,
                         'Turns': num_turns,
                         'Phase': phase,
                         'Baseline Crossing': baseline_crossing,
                         'Duration': duration})

        # Print parameters (for debugging)
        print("Amplitude:", amplitude)
        print("Rise Time:", rise_time)
        print("Turns:", num_turns)
        print("Phase:", phase)
        print("Baseline Crossing:", baseline_crossing)
        print("Duration:", duration)
        print()

except KeyboardInterrupt:
    # Close serial connection and CSV file
    ser.close()
    csvfile.close()
    print("Output saved to:", output_file)
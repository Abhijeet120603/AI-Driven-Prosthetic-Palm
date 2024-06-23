import csv
import numpy as np
import serial
import time

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

        # Calculate rise time
        threshold = 0.1 * amplitude  # 10% threshold
        rise_time = None
        if emg_data >= threshold:
            rise_time = time.time()  # Get current time

        # Find peaks
        peaks = []
        if emg_data >= threshold:
            peaks.append(time.time())  # Append current time as peak

        # Calculate turns (number of peaks)
        num_turns = len(peaks)

        # Calculate phase (for demonstration purposes, calculating the phase relative to the first peak)
        if num_turns > 0:
            first_peak_time = peaks[0]
            phase = first_peak_time - time.time()  # Phase relative to the current time
        else:
            phase = None

        # Calculate baseline crossing and duration
        baseline_crossing = None
        duration = None

        if emg_data >= threshold:
            baseline_crossing = time.time()  # Get current time

        if baseline_crossing is not None:
            duration = time.time() - baseline_crossing  # Calculate duration from baseline crossing to current time

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
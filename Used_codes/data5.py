import csv
import numpy as np
import serial
import time
from math import log2
from scipy.signal import hilbert
import matplotlib.pyplot as plt


ser = serial.Serial('/dev/ttyACM0', 9600)  


sampling_freq = 1000  


output_file = 'emg_parameters.csv'
csvfile = open(output_file, 'w', newline='')
fieldnames = ['Amplitude', 'Rise Time', 'Turns', 'Phase', 'Baseline Crossing', 'Duration']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


def calculate_baseline_crossings(amplitude, baseline_threshold=0.2):
    previous_amplitude = amplitude[0]
    crossings = []
    for i in range(1, len(amplitude)):
        if previous_amplitude < baseline_threshold and amplitude[i] >= baseline_threshold:
            crossings.append(i)  
        elif previous_amplitude > baseline_threshold and amplitude[i] <= baseline_threshold:
            crossings.append(i)  
        previous_amplitude = amplitude[i]  
    num_crossings = len(crossings)
    return num_crossings, crossings

try:
    while True:
        
        emg_data = float(ser.readline().decode().strip())

       
        amplitude = emg_data
        T10 = 0.1 * amplitude
        T90 = 0.9 * amplitude
        rise_time = (T90 - T10) / log2(10 / 90)

        peak_to_peak_amplitude = ... 
        duration = ...  
        period = duration / 1  
        frequency = 1 / period

        turns_per_phase = sampling_freq / frequency

        emg_signal = ...  
        analytic_signal = hilbert(emg_signal)
        phase = np.angle(analytic_signal)

       
        num_turns = 0 
        duration = 0  

 
        num_crossings, crossings = calculate_baseline_crossings(amplitude)

        writer.writerow({'Amplitude': amplitude,
                         'Rise Time': rise_time,
                         'Turns': turns_per_phase,
                         'Phase': phase,
                         'Baseline Crossing': num_crossings,
                         'Duration': duration})

        
        print("Amplitude:", amplitude)
        print("Rise Time:", rise_time)
        print("Turns:", turns_per_phase)
        print("Phase:", phase)
        print("Baseline Crossing:", num_crossings)
        print("Duration:", duration)
        print()
except KeyboardInterrupt:
    
    ser.close()
    csvfile.close()
    print("Output saved to:", output_file)

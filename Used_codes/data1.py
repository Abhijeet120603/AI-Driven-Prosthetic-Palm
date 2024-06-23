import csv
import numpy as np
import serial
import time
from math import log2


ser = serial.Serial('/dev/ttyACM0', 9600)  

sampling_freq = 1000 


output_file = 'emg_parameters.csv'
csvfile = open(output_file, 'w', newline='')
fieldnames = ['Amplitude', 'Rise Time', 'Turns', 'Phase', 'Baseline Crossing', 'Duration']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

try:
    while True:
        
        emg_data = float(ser.readline().decode().strip())

        amplitude = emg_data

        import numpy as np
        from scipy.signal import hilbert
        import matplotlib.pyplot as plt

        
        emg_signal = ...  

        
        analytic_signal = hilbert(emg_signal)
        phase = np.angle(analytic_signal)

        
        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(emg_signal)
        plt.title('Original EMG Signal')

        plt.subplot(2, 1, 2)
        plt.plot(phase)
        plt.title('Phase of EMG Signal')

        plt.show()

        
        T10 = 0.1 * amplitude
        T90 = 0.9 * amplitude
        rise_time = (T90 - T10) / log2(10 / 90)

        import numpy as np

       
        baseline_threshold = 0.2 

        
        previous_amplitude = amplitude[0]  

        
        crossings = []

        
        for i in range(1, len(amplitude)):
            if previous_amplitude < baseline_threshold and amplitude[i] >= baseline_threshold:
                crossings.append(i)  
            elif previous_amplitude > baseline_threshold and amplitude[i] <= baseline_threshold:
                crossings.append(i) 
            
            previous_amplitude = amplitude[i]  

        
        num_crossings = len(crossings)
        print("Number of baseline crossings:", num_crossings)
        print("Crossing indices:", crossings)


        
        writer.writerow({'Amplitude': amplitude,
                         'Rise Time': rise_time,
                         'Turns': num_turns,
                         'Phase': phase,
                         'Baseline Crossing': baseline_crossing,
                         'Duration': duration})

        
        print("Amplitude:", amplitude)
        print("Rise Time:", rise_time)
        print("Turns:", num_turns)
        print("Phase:", phase)
        print("Baseline Crossing:", baseline_crossing)
        print("Duration:", duration)
        print()

except KeyboardInterrupt:
    
    ser.close()
    csvfile.close()
    print("Output saved to:", output_file)
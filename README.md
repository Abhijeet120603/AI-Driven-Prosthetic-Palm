# AI-Driven-Prosthetic-Palm
In this project i had created an palm which will work like an normal human hand. It is been trained using machine learning. It can currenty perform some specified gestures. 


In this project, I used an EMG Muscle Sensor V3. Connections are made according to the user manual of the EMG Muscle Sensor V3. For easy access, I have uploaded the user manual of this sensor. The components used in this project are Raspberry Pi 3, Arduino, and the Muscle Sensor.

To verify the data from the sensor, we can check it on the Arduino IDE using the serial plotter. It should generate a waveform corresponding to finger movements. The Arduino code is provided in the file named "main_code/emg_code_arduino.ino." Upload the code to the Arduino.

After that, connect it with the Raspberry Pi. Change the serial port name in the file "main_code/emg_data_extraction_code_rpi.py." After changing it, run the code. It will create a file named "emg_parameters.csv." This way, you can generate your own datasets.

I have applied a machine learning algorithm for the actuation of fingers. The ML code will be uploaded shortly.

The hand used in this project is 3D printed and I had uploaded the file of individual component.

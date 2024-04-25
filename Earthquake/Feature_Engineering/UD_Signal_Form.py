import matplotlib.pyplot as plt
import numpy as np

sampling_freq = 100
duration = 119
num_samples = len(memo_array)
time_values = np.linspace(0, duration, num_samples)
plt.plot(time_values, memo_array)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Waveform Visualization')
plt.grid(True)
plt.show()

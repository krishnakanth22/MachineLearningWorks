import numpy as np
import matplotlib.pyplot as plt

sampling_freq = 100  
duration_time = 59   
scale_factor = 2000 / 8388608

num_samples = len(memo_array)
time = np.linspace(0, duration_time, num_samples)
last_clicked_point = None  
start_listening = False  
def onclick(event):
    global last_clicked_point, start_listening
    if start_listening:
        last_clicked_point = (event.xdata, event.ydata)
        print(f'Clicked point: ({last_clicked_point[0]:.2f}, {last_clicked_point[1]:.2f})')
        plt.close()
    else:
        print("Press Enter to start selecting points.")
def on_key(event):
    global start_listening
    if event.key == 'enter':
        start_listening = True

%matplotlib qt

plt.figure()
plt.plot(np.array(memo_array) * scale_factor) 
plt.title('Acceleration Data')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (gal)')
plt.grid(True)

plt.gcf().canvas.mpl_connect('key_press_event', on_key)
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.show()
if last_clicked_point:
    print("Last clicked point:", last_clicked_point)
else:
    print("No point has been clicked yet.")

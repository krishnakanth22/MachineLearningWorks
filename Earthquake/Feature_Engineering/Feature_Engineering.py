#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install mplcursors')


# In[1]:


# Using a raw string (prefixing with 'r')
file_path = r'E:\1996\19960724214700.knt\SZO0039607242147.UD'

with open(file_path, 'r') as file:
    contents = file.read()
print(contents)


# In[8]:


lines = contents.split("\n")
memo_data = []
in_memo_section = False

for line in lines:
    if "Memo." in line:
        in_memo_section = True
        continue
    if in_memo_section and line.strip():
        memo_data.extend(line.strip().split())
memo_array = [int(value) for value in memo_data]
print(memo_array)


# In[21]:


import numpy as np
import matplotlib.pyplot as plt

# Provided data
sampling_freq = 100  # Hz
duration_time = 59   # seconds
scale_factor = 2000 / 8388608

# Assuming you have already defined memo_array and time
num_samples = len(memo_array)
time = np.linspace(0, duration_time, num_samples)

# Plot the data
plt.figure()
plt.plot(time, np.array(memo_array) * scale_factor)  # Convert memo_array to numpy array before multiplication
plt.title('Acceleration Data')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (gal)')
plt.grid(True)
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

# Set the backend to qt explicitly
get_ipython().run_line_magic('matplotlib', 'qt')
plt.show()


# In[29]:


import numpy as np
import matplotlib.pyplot as plt
sampling_freq = 100  # Hz
duration_time = 59   # seconds
scale_factor = 2000 / 8388608

num_samples = len(memo_array)
time = np.linspace(0, duration_time, num_samples)
last_clicked_point = None  # Initialize variable to store last clicked point

def onclick(event):
    global last_clicked_point
    last_clicked_point = (event.xdata, event.ydata)
    print(f'Clicked point: ({last_clicked_point[0]:.2f}, {last_clicked_point[1]:.2f})')

get_ipython().run_line_magic('matplotlib', 'qt')

plt.figure()
plt.plot(time, np.array(memo_array) * scale_factor) 
plt.title('Acceleration Data')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (gal)')
plt.grid(True)
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

plt.show()
if last_clicked_point:
    print("Last clicked point:", last_clicked_point)
else:
    print("No point has been clicked yet.")


# In[30]:


print(last_clicked_point)


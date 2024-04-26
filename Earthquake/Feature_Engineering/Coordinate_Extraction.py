import matplotlib.pyplot as plt
import mplcursors

# Define a callback function to handle the click event
def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        print(f'Clicked point: ({event.xdata:.2f}, {event.ydata:.2f})')
        # Save the coordinates to a variable or perform any other action

# Generate sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y)
plt.title('Interactive Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Attach the onclick event handler to the figure
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

# Display the plot
mplcursors.cursor()

plt.show()

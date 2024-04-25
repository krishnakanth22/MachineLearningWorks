import plotly.graph_objects as go

sampling_freq = 100  # Hz
duration = 59  # seconds
num_points = len(memo_array)
time = [i / sampling_freq for i in range(num_points)]

# Create the interactive plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=memo_array, mode='lines', name='Seismic Data'))
fig.update_layout(title='Seismic Data Plot',
                  xaxis_title='Time (s)',
                  yaxis_title='Acceleration (gal)',
                  template='plotly_dark')
fig.show()

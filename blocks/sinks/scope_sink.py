# blocks/sinks/scope_sink.py

import matplotlib.pyplot as plt
from blocks.sinks.base_sink_block import BaseSinkBlock

class ScopeSinkBlock(BaseSinkBlock):
    def __init__(self, name):
        super().__init__(name)
        # We'll use the base sink functionality for input ports.
        # Additionally, create buffers and plotting objects for each input.
        self.times = {}
        self.values = {}
        self.lines = {}
        # Create the figure and axis in the main thread.
        plt.ion()
        self.figure, self.ax = plt.subplots()
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Signal Value")
        self.ax.grid(True)
        # Do not call legend() yet (we'll update it later when data exists)
        self.figure.canvas.draw()
        self.background = self.figure.canvas.copy_from_bbox(self.ax.bbox)

    def add_input_port(self, port_name, default_value=None, expected_type=None):
        super().add_input_port(port_name, default_value, expected_type)
        # Initialize buffers for this port.
        self.times[port_name] = []
        self.values[port_name] = []
        # Create a line for this port with a proper label.
        (line,) = self.ax.plot([], [], label=f"{self.name}-{port_name}")
        self.lines[port_name] = line
        # Update legend.
        self.ax.legend()

    def update(self, t, dt):
        # For each input port, record the current value.
        for port_name, port in self.input_ports.items():
            value = port.get()
            if value is not None:
                self.times[port_name].append(t)
                self.values[port_name].append(value)

    def update_plot(self):
        # Update the data for each line.
        for port_name in self.input_ports.keys():
            if self.times[port_name]:
                self.lines[port_name].set_xdata(self.times[port_name])
                self.lines[port_name].set_ydata(self.values[port_name])
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.legend()
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def get_output(self):
        return {}

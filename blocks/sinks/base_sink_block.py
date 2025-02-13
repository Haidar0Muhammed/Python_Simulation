# blocks/sinks/base_sink_block.py

from simulation.block import BaseBlock
from simulation.port import Port

class BaseSinkBlock(BaseBlock):
    def __init__(self, name):
        super().__init__(name)
        # Sink blocks have input ports but produce no outputs.
        self.input_ports = {}
        self.data = {}  # Optional: dictionary to store data per port.
    
    def add_input_port(self, port_name, default_value=None, expected_type=None):
        self.input_ports[port_name] = Port(port_name, direction="input", default_value=default_value, expected_type=expected_type)
        self.data[port_name] = []
    
    def update(self, t, dt):
        raise NotImplementedError("Subclasses of BaseSinkBlock must implement update(t, dt)")
    
    def get_output(self):
        return {}

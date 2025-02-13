# simulation/block.py

from simulation.port import Port

class BaseBlock:
    def __init__(self, name):
        self.name = name
        # Ports are stored as dictionaries mapping port names to Port objects.
        self.input_ports = {}
        self.output_ports = {}
        # Optional internal state.
        self.state = None

    def add_input_port(self, port_name, default_value=None, expected_type=None):
        self.input_ports[port_name] = Port(port_name, direction="input", default_value=default_value, expected_type=expected_type)

    def add_output_port(self, port_name, default_value=None, expected_type=None):
        self.output_ports[port_name] = Port(port_name, direction="output", default_value=default_value, expected_type=expected_type)

    def update(self, t, dt):
        """
        Update the block's internal state and compute outputs based on its inputs.
        This method must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement update(t, dt)")

    def get_output(self):
        """
        Returns a dictionary mapping output port names to their current values.
        """
        return {name: port.get() for name, port in self.output_ports.items()}

    def __repr__(self):
        return f"BaseBlock({self.name})"

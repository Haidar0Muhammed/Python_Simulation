# simulation/port.py

from simulation.signal import Signal

class Port:
    def __init__(self, name, direction="bidirectional", default_value=None, expected_type=None):
        """
        A port holds a Signal along with metadata.
        
        Parameters:
          - name: the port's name.
          - direction: "input", "output", or "bidirectional".
          - default_value: initial value.
          - expected_type: optional type that the port's value is expected to be.
        """
        allowed = {"input", "output", "bidirectional"}
        if direction not in allowed:
            raise ValueError(f"Direction must be one of {allowed}")
        self.name = name
        self.direction = direction
        self.expected_type = expected_type
        self.signal = Signal(default_value)

    def set(self, value):
        if self.expected_type is not None and not isinstance(value, self.expected_type):
            raise TypeError(f"Port '{self.name}' expects type {self.expected_type.__name__}, got {type(value).__name__}")
        self.signal.set(value)

    def get(self):
        return self.signal.get()

    def __repr__(self):
        return f"Port({self.name}, direction={self.direction}, value={self.signal.get()}, expected_type={self.expected_type})"

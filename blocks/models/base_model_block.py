from simulation.block import BaseBlock
import numpy as np

class BaseModelBlock(BaseBlock):
    def __init__(self, name, initial_state=None):
        super().__init__(name)
        # Initialize internal state as a numpy array (or zeros if not provided).
        if initial_state is not None:
            self.state = np.array(initial_state, dtype=float)
        else:
            # Default to a zero state of length 1 (you may adjust this as needed).
            self.state = np.zeros(1)
        # Create aliases for compatibility.
        self.inputs = self.input_ports   # so that self.inputs works the same as self.input_ports
        self.outputs = self.output_ports # same for outputs

    def update(self, t, dt):
        """
        Update the model's state and outputs.
        This method must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses of BaseModelBlock must implement update(t, dt)")

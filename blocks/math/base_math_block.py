# blocks/math/base_math_block.py

from simulation.block import BaseBlock

class BaseMathBlock(BaseBlock):
    def __init__(self, name):
        super().__init__(name)
        # Typically, math blocks have two inputs and one output.
        self.add_input_port("in1", default_value=0)
        self.add_input_port("in2", default_value=0)
        self.add_output_port("out", default_value=0)
    
    def update(self, t, dt):
        raise NotImplementedError("Subclasses of BaseMathBlock must implement update(t, dt)")

# blocks/math/subtraction.py

from blocks.math.base_math_block import BaseMathBlock

class SubtractionBlock(BaseMathBlock):
    def __init__(self, name):
        super().__init__(name)
    
    def update(self, t, dt):
        a = self.input_ports["in1"].get()
        b = self.input_ports["in2"].get()
        self.output_ports["out"].set(a - b)

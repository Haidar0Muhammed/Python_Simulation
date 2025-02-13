# blocks/sources/constant_source.py

from simulation.block import BaseBlock
from simulation.signal import Signal

class ConstantSourceBlock(BaseBlock):
    def __init__(self, name, constant_value):
        super().__init__(name)
        self.constant_value = constant_value
        self.add_output_port("out", default_value=constant_value)

    def update(self, t, dt):
        # Always output the constant value.
        self.output_ports["out"].set(self.constant_value)

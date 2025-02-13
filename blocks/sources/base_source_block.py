# blocks/sources/base_source_block.py

from simulation.block import BaseBlock

class BaseSourceBlock(BaseBlock):
    def __init__(self, name):
        super().__init__(name)
        # Source blocks produce outputs and typically have no inputs.
    
    def update(self, t, dt):
        raise NotImplementedError("Subclasses of BaseSourceBlock must implement update(t, dt)")

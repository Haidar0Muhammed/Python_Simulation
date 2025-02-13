# blocks/sources/step_source.py

from blocks.sources.base_source_block import BaseSourceBlock

class StepSourceBlock(BaseSourceBlock):
    def __init__(self, name, initial_value, final_value, step_time):
        super().__init__(name)
        self.initial_value = initial_value
        self.final_value = final_value
        self.step_time = step_time
        self.add_output_port("out", default_value=initial_value)
    
    def update(self, t, dt):
        if t < self.step_time:
            self.output_ports["out"].set(self.initial_value)
        else:
            self.output_ports["out"].set(self.final_value)

# blocks/models/pid_controller.py

from blocks.models.base_model_block import BaseModelBlock
import numpy as np

class PIDControllerBlock(BaseModelBlock):
    def __init__(self, name, Kp, Ki, Kd, dt, initial_state=None):
        # State: [integral, prev_error]
        super().__init__(name, initial_state if initial_state is not None else [0.0, 0.0])
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        # Create input port "in" (for error)
        self.add_input_port("in", default_value=0.0, expected_type=float)
        # Create output port "out" (for control voltage)
        self.add_output_port("out", default_value=0.0, expected_type=float)
    
    def update(self, t, dt):
        error = self.input_ports["in"].get()
        integral, prev_error = self.state
        integral += error * dt
        derivative = (error - prev_error) / dt
        self.state = np.array([integral, error])
        u = self.Kp * error + self.Ki * integral + self.Kd * derivative
        self.output_ports["out"].set(u)

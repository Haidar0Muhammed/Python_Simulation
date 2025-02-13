# blocks/models/dc_motor_model_block.py

import numpy as np
from blocks.models.base_model_block import BaseModelBlock

class DCMotorModelBlock(BaseModelBlock):
    def __init__(self, name, initial_state=None, L=0.5, R=1.0, Ke=0.01, Kt=0.05, J=0.02, b=0.1):
        # State: [i, ω, θ]
        super().__init__(name, initial_state if initial_state is not None else [0, 0, 0])
        self.L = L
        self.R = R
        self.Ke = Ke
        self.Kt = Kt
        self.J = J
        self.b = b
        # Create input ports: "voltage" and "T_load"
        self.add_input_port("voltage", default_value=0.0, expected_type=float)
        self.add_input_port("T_load", default_value=0.0, expected_type=float)
        # Create output ports: "omega" (angular speed) and "theta" (position)
        self.add_output_port("omega", default_value=0.0, expected_type=float)
        self.add_output_port("theta", default_value=0.0, expected_type=float)
    
    def update(self, t, dt):
        voltage = self.input_ports["voltage"].get()
        T_load = self.input_ports["T_load"].get()
        i, omega, theta = self.state
        di_dt = (voltage - self.R * i - self.Ke * omega) / self.L
        domega_dt = (self.Kt * i - self.b * omega - T_load) / self.J
        dtheta_dt = omega
        self.state += np.array([di_dt, domega_dt, dtheta_dt]) * dt
        self.output_ports["omega"].set(self.state[1])
        self.output_ports["theta"].set(self.state[2])

#!/usr/bin/env python3
# main.py

import threading
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from simulation.network_simulator import NetworkSimulator
from blocks.sources.step_source import StepSourceBlock
from blocks.models.dc_motor_model_block import DCMotorModelBlock
from blocks.models.pid_controller import PIDControllerBlock
from blocks.math.subtraction import SubtractionBlock
from blocks.sinks.scope_sink import ScopeSinkBlock

def simulation_thread(sim, blocks):
    sim.run(blocks)

def main():
    dt_sim = 0.001
    T_total = 20.0

    # Create blocks.
    # DesiredSpeed: constant 10 rad/s.
    desired_speed_source = StepSourceBlock("DesiredSpeed", initial_value=10.0, final_value=20.0, step_time=10)
    
    # Subtraction block: error = desired speed - real speed.
    error_block = SubtractionBlock("ErrorCalc")
    
    # PID controller.
    pid_block = PIDControllerBlock("PID", Kp=75.0, Ki=30.0, Kd=20.0, dt=dt_sim)
    
    # DC Motor model.
    motor_block = DCMotorModelBlock("Motor", initial_state=[0, 0, 0],
                                    L=0.5, R=1.0, Ke=0.01, Kt=0.05, J=0.01, b=0.1)
    
    # Sinks:
    motor_speed_sink = ScopeSinkBlock("MotorSpeedSink")
    motor_speed_sink.add_input_port("desired", default_value=0, expected_type=float)
    motor_speed_sink.add_input_port("real", default_value=0, expected_type=float)
    
    motor_theta_sink = ScopeSinkBlock("MotorThetaSink")
    motor_theta_sink.add_input_port("theta", default_value=0, expected_type=float)
    
    error_sink = ScopeSinkBlock("ErrorSink")
    error_sink.add_input_port("error", default_value=0, expected_type=float)
    
    # Connect blocks by sharing Port objects:
    desired_port = desired_speed_source.output_ports["out"]
    error_block.input_ports["in1"] = desired_port
    motor_speed_sink.input_ports["desired"] = desired_port

    real_speed_port = motor_block.output_ports["omega"]
    error_block.input_ports["in2"] = real_speed_port
    motor_speed_sink.input_ports["real"] = real_speed_port

    error_port = error_block.output_ports["out"]
    pid_block.inputs["in"] = error_port  # note: PIDControllerBlock (inherits from BaseModelBlock) must have alias "inputs"
    error_sink.input_ports["error"] = error_port

    motor_block.input_ports["voltage"] = pid_block.output_ports["out"]

    motor_theta_sink.input_ports["theta"] = motor_block.output_ports["theta"]

    blocks = {
        "DesiredSpeed": desired_speed_source,
        "ErrorCalc": error_block,
        "PID": pid_block,
        "Motor": motor_block,
        "MotorSpeedSink": motor_speed_sink,
        "MotorThetaSink": motor_theta_sink,
        "ErrorSink": error_sink
    }

    sim = NetworkSimulator(dt=dt_sim, T_total=T_total)

    # Run simulation in separate thread.
    sim_thread = threading.Thread(target=simulation_thread, args=(sim, blocks))
    sim_thread.start()

    # Use FuncAnimation in main thread to update all sink plots.
    def update_plots(frame):
        motor_speed_sink.update_plot()
        motor_theta_sink.update_plot()
        error_sink.update_plot()
    ani = FuncAnimation(motor_speed_sink.figure, update_plots, interval=100)
    
    plt.show(block=True)
    sim_thread.join()

if __name__ == '__main__':
    main()
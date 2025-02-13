# Python Simulation Platform

This project is a MATLAB/Simulink–like simulation environment built in Python. It implements a block–port–signal architecture for modeling and simulating dynamic systems. The project features modular components including sources, models (dynamic systems), math operations, and sinks (output blocks), all connected via dedicated Port objects that encapsulate signals. The simulation platform is demonstrated with a closed-loop control system for a DC motor using PID control.

## Features

- **Modular Block-Based Architecture**  
  Each block (source, model, math, sink) inherits from a common base class (`BaseBlock`) and manages its inputs and outputs using dedicated Port objects.

- **Dynamic Models**  
  The project includes a DC motor model block (`DCMotorModelBlock`) and a PID controller block (`PIDControllerBlock`), both inheriting from `BaseModelBlock`.

- **Math Operations**  
  A math block (`SubtractionBlock`) computes the difference between two signals, used to determine the error between a desired setpoint and the actual motor speed.

- **Sources and Sinks**  
  A step source block (`StepSourceBlock`) generates a step input signal (for example, a voltage setpoint). Several sink blocks (`ScopeSinkBlock`) display simulation data in real time. In our closed-loop test, separate scopes display:
  - Motor speed (both desired and real speed),
  - Motor position (theta),
  - Control error.

- **Real-Time and Accelerated Simulation**  
  The simulation engine (`NetworkSimulator`) is designed to run as fast as possible (with optional real-time synchronization) and decouples simulation computation from plotting by using a separate thread for simulation and `FuncAnimation` for real-time updates in the main thread.

## Folder Structure

```
project/
├── main.py                     # Main file to run the simulation.
├── README.md                   # This file.
├── simulation/                 # Core simulation engine and base classes.
│   ├── __init__.py             # (empty)
│   ├── base_block.py           # Contains the BaseBlock class.
│   ├── signal.py               # Contains the generic Signal class.
│   ├── port.py                 # Contains the Port class.
│   └── network_simulator.py    # Contains the NetworkSimulator class.
├── blocks/                     # Definitions of simulation blocks.
│   ├── __init__.py             # (empty)
│   ├── sources/                # Source blocks (that generate signals).
│   │   ├── __init__.py         # (empty)
│   │   └── step_source.py      # Contains StepSourceBlock.
│   ├── models/                 # Dynamic system blocks.
│   │   ├── __init__.py         # (empty)
│   │   ├── base_model_block.py # Base class for model blocks.
│   │   ├── dc_motor_model_block.py  # Contains DCMotorModelBlock.
│   │   └── pid_controller.py   # Contains PIDControllerBlock.
│   ├── math/                   # Math operation blocks.
│   │   ├── __init__.py         # (empty)
│   │   └── subtraction.py      # Contains SubtractionBlock.
│   └── sinks/                  # Sink (output) blocks.
│       ├── __init__.py         # (empty)
│       ├── base_sink_block.py  # Base class for sink blocks.
│       └── scope_sink.py       # Contains ScopeSinkBlock.
└── signals/                    # (Optional) Additional signal classes.
    ├── __init__.py             # (empty)
    └── base_signal.py          # Base signal class (if different from simulation/signal.py).
```

## How It Works

1. **Block Architecture:**  
   - **BaseBlock:** The common parent for all blocks. It handles port creation and provides an interface for updates.  
   - **BaseModelBlock:** Inherits from BaseBlock for dynamic systems (e.g., DC motor, PID controller).  
   - **BaseMathBlock:** Inherits from BaseBlock for math operations (e.g., subtraction).  
   - **BaseSinkBlock:** Inherits from BaseBlock for output-only blocks (e.g., scopes).  
   - **BaseSourceBlock:** Inherits from BaseBlock for blocks that generate signals (e.g., step source).

2. **Ports and Signals:**  
   Each block’s inputs and outputs are managed using `Port` objects (defined in `simulation/port.py`). A port encapsulates a `Signal`, which carries data (of any type) along with its data type.

3. **Simulation Engine:**  
   The `NetworkSimulator` class (in `simulation/network_simulator.py`) steps through time, calling each block’s `update(t, dt)` method. Blocks update their internal state and outputs accordingly.  
   Plotting is decoupled from the simulation thread: the simulation runs in a separate thread while the main thread uses `FuncAnimation` to update the display.

4. **Closed-Loop Example:**  
   The main file demonstrates a closed-loop control system:
   - A step source sets the desired voltage (or desired speed).
   - A subtraction block computes the error between desired speed and motor speed.
   - A PID controller block processes the error to produce a control voltage.
   - A DC motor model block uses that voltage to update its state (producing outputs "omega" and "theta").
   - Multiple sink blocks display the signals (motor speed, motor position, error).

## How to Run

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/Haidar0Muhammed/Python_Simulation.git
   cd Python_Simulation
   ```

2. **Install Dependencies:**  
   Ensure you have Python 3 installed and the required libraries. For example, you need:
   - NumPy
   - Matplotlib
   You can install these using pip:
   ```bash
   pip install numpy matplotlib
   ```

3. **Run the Simulation:**  
   In the terminal, execute:
   ```bash
   python main.py
   ```
   This will run the simulation. Sink blocks will open plotting windows updated in real time.

4. **Interacting with the Simulation:**  
   The simulation runs in a background thread while the main thread displays the plots. Close the plot windows to finish.

## Contributing

Feel free to fork this repository and submit pull requests with improvements, bug fixes, or new features (such as additional block types, signal converters, or enhanced plotting).

## License

This project is open source.
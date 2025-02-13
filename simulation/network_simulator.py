import time

class NetworkSimulator:
    def __init__(self, dt=0.001, T_total=10.0):
        self.dt = dt
        self.T_total = T_total
        self.steps = int(T_total / dt)
        self.time_list = []

    def run(self, blocks):
        start_time = time.time()
        for step in range(self.steps):
            t = step * self.dt
            self.time_list.append(t)
            for block in blocks.values():
                block.update(t, self.dt)

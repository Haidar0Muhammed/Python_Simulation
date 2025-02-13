# simulation/signal.py

class Signal:
    """
    A generic Signal class that carries data from block to block.
    It stores a value of any type and records its data type.
    """
    def __init__(self, value=None):
        self.value = value
        self.dtype = type(value)

    def set(self, value):
        self.value = value
        self.dtype = type(value)

    def get(self):
        return self.value

    def get_dtype(self):
        return self.dtype

    def __repr__(self):
        return f"Signal({repr(self.value)}, dtype={self.dtype.__name__})"

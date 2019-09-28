import numpy as np

def emitter(gain, omega, t):
    while True:
        v = gain*np.sin(omega*t)
        return v

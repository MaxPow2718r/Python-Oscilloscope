import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def emitter(gain, omega, t):
    while True:
        v = gain*np.sin(omega*t)
        return v


import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
import numpy as np
import probe
from scope import *

t = np.linspace(0, 10, 100)
gain = 2
omega = 2

fig, ax = plt.subplots()
scope = Scope(ax)

# pass a generator in "emitter" to produce data for the update func
ani = animation.FuncAnimation(fig, scope.update, probe.emitter(gain, omega, t), interval=10,
                              blit=True)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack import fft


# %matplotlib inline

N = 40

# time vector
time_vector = np.linspace(0, 1, N, endpoint=True)

x = np.sin(np.pi * t) * np.sin(2* np.pi * t) + np.sin(3 * np.pi * t) + np.sin(5 * np.pi * t)

def plt_sel(s, *args, **kwargs):
    if s == 0: return plt.plot(*args)
    if s == 0: return plt.stem(*args, **kwargs)
    if s == 0: return plt.step(*args)
import numpy as np

def moving_average(x, n=5):
    x=np.asarray(x,float)
    if n<=1:return x
    return np.convolve(x,np.ones(n)/n,mode="same")

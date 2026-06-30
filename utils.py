import numpy as np

def normalize(x):
    x=np.asarray(x,float)
    mn,mx=x.min(),x.max()
    if mx==mn:return np.zeros_like(x)
    return (x-mn)/(mx-mn)

def rms(x):
    x=np.asarray(x,float)
    return float(np.sqrt(np.mean(x*x)))

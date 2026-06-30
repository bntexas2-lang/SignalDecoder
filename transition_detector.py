import numpy as np

def detect_transitions(signal):
    s=np.asarray(signal)
    return np.where(np.diff(np.sign(s))!=0)[0]+1

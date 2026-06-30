import numpy as np

def detect_frames(signal, threshold=0.5):
    s=np.asarray(signal)
    above=s>threshold
    frames=[]
    start=None
    for i,v in enumerate(above):
        if v and start is None:start=i
        if not v and start is not None:
            frames.append((start,i)); start=None
    if start is not None: frames.append((start,len(s)))
    return frames

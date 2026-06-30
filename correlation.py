import numpy as np

def normalized_correlation(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    if len(a)!=len(b): raise ValueError("Lengths differ")
    na=np.linalg.norm(a); nb=np.linalg.norm(b)
    if na==0 or nb==0:return 0.0
    return float(np.dot(a,b)/(na*nb))

import numpy as np
from scipy.stats import norm
def call_price(s, k, vol, r, t):
    d1 = (np.log(s/k) + (r + (vol**2)/2) * t) / (vol * np.sqrt(t))
    d2 = d1 - vol * np.sqrt(t)
    return s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
def put_price(s, k, vol, r, t):
    d1 = (np.log(s/k) + (r + (vol**2)/2) * t) / (vol * np.sqrt(t))
    d2 = d1 - vol * np.sqrt(t)
    return k * np.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)
c=call_price(1427.65,1390,0.3,0.06,46/365)
p=put_price(1427.65,1390,0.3,0.06,46/365)
print("The Call price is: ",round(c,4))
print("The Put price is: ",round(p,4))

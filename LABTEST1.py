#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt

np.random.seed(0)
aqi = np.random.normal(loc=50,scale=100,size=1440)

def apply_low_pass_filter(data, cutoff=0.1,fs=1.0,order=2):
    nyquist = 0.5*fs
    normal_cutoff = cutoff/nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

smoothed_aqi = apply_low_pass_filter(aqi)
hourly_averages = np.mean(smoothed_aqi.reshape(-1, 60), axis=1)
hourly_aqi = np.repeat(hourly_averages, 60)

plt.figure(figsize=(14, 7))
plt.plot(aqi,label="Original Noisy AQI",color="blue")

plt.plot(smoothed_aqi,label="Smoothed AQI",linewidth=2,color="orange")
plt.plot(hourly_aqi,label="Hourly AQI",linestyle="--",linewidth=2,color="green")

thershold = 100
exceed_indices = np.where(smoothed_aqi>thershold)[0]

for i in range(len(exceed_indices)-15):
    if exceed_indices[i+15]-exceed_indices[i]==15:
        plt.plot(exceed_indices[i],exceed_indices[i+15],color="red",alpha=0.5)
plt.xlabel("TIme(minutes)")
plt.ylabel("AQI")
plt.title("Air Quality Index Analysis")
plt.show()


    


# In[ ]:





# In[ ]:





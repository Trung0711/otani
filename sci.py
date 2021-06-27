
import numpy as np
from matplotlib import pyplot as pl

# tao ham trong n=mien thowi gian 
# tan so theo son vij hz
fre=10
#ti le mau
fre_samp=100
#thoi gian
t=np.linspace(0,2,2*fre_samp,endpoint=False)
#ham sin theo thoi gian
f=np.sin(fre*2*np.pi*t)+np.cos(2*fre*np.pi*t)
#ve ham 
# pl.figure(1)
# figure=pl.subplot()
pl.figure(0)
pl.subplot(122)
pl.plot(t,f)
# axis.set_xlabel('thời gian (s)')
# axis.set_ylabel('cường độ tín hiệu')

#sử dụng biến đổi furie
from scipy import fft

s=fft.fft(f)
# frequency=fft.fftfreq(len(s))*fre_samp
#vẽ hàm trong miền tấn số

# axis.stem(frequency,abs(s),use_line_collection=True)
m=np.linspace(-50,50,200)
pl.subplot(121)
pl.plot(m,s)
# axis.set_xlabel('tần số hz')
# axis.set_ylabel('độ lớn phổ tần số')
# axis.set_xlim(-fre_samp/2,fre_samp/2)
# axis.set_ylim(0,100)
pl.show()

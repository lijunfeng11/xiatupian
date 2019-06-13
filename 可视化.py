# 颜色rbgc
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(10)
y=np.arange(10)
plt.plot(x,y,'--co')
plt.plot(x,x**2,'--go')
plt.legend(['y=x','y=x^2'],loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.title('第一幅图')
plt.rcParams['font.sans-serif']=['SimHei']
# xytext=(5,15)箭头
plt.annotate('备注',xy=(5,5),xytext=(5,15),arrowprops={'facecolor':'black'})
# plt.annotate('备注',xy=(5,5),xytext=(5,15),arrowprops=dict(facecolor='black'))
# print(dict(facecolor='black'))
plt.show()
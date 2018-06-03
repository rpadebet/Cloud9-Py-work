import numpy as np

a = np.arange(1, 10, 0.5)
a.shape
len(a)

a.shape
y = np.zeros((2, 3, 4))
print y

c = np.linspace(1,5,100)
print(c)

d = np.diag(np.array([1,2,3,4]))

print d

r=np.random.randn()
print(r)

np.empty((2,3),dtype=float)

import matplotlib.pyplot as plt

x=np.random.randn(20)
y=np.random.rand(20)
plt.plot(x,y)

plt.show()
plt.plot(x,y,'*')

plt.show()

# 2-d plots

image = np.random.randn(10, 10)
plt.imshow(image, cmap = plt.cm.gray)
plt.colorbar()
plt.show()

# indexing

data = np.random.randint(low=1,high=100,size =10)
mask = (data % 3 == 0)
new_data = data[mask]
print(new_data)

test=np.array(new_data,np.arange(3))

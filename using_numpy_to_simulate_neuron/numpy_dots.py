import numpy as np
import time

st=time.time()

#vector times vector dot. (Neurons)
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.dot(a,b)
end=time.time()

print("result: ", c)
print("Time taken: {:}".format(end-st))

#Vector times matrix (layer)

a=np.array([1,2,3])
b=np.array([[4,5,6],[3,5,6],[1,6,8]])
c=np.dot(a,b)
end=time.time()

print("result: ", c)
print("Time taken: {:}".format(end-st))



#matrix times vector (layer)

a=np.array([1,2,3])
b=np.array([[4,5,6],[3,5,6],[1,6,8]])
c=np.dot(b,a)
end=time.time()

print("result: ", c)
print("Time taken: {:}".format(end-st))


#Matrix times matrix (batch)

a=np.array([[j*i for j in range(10,15)] for i in range(15,20)])
b=np.array([[j * i for j in range(10,15)] for i in range(15,20)])


c=np.dot(b,a)
end=time.time()

print("result: ", c)
print("Time taken: {:}".format(end-st))
import numpy as np
a = np.random.randint(1,20,15)
print("array:")
print(a)
a.resize((3,5))
print(a)
print(a.shape)
for i in a:
    i[np.where(i==i.max())] = 0
print("maximum value replaced by 0:")
print(a)

OUTPUT: 
array:
[ 1 16 12  3 10  1  1 10 15 10 13 10  9 19 10]
[[ 1 16 12  3 10]
 [ 1  1 10 15 10]
 [13 10  9 19 10]]
(3, 5)
maximum value replaced by 0:
[[ 1  0 12  3 10]
 [ 1  1 10  0 10]
 [13 10  9  0 10]]    

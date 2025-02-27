import numpy as np # terminálba: pip install numpy
import matplotlib.pyplot as plt #pip install matplotlib

# Numpy tömbök (array)

tomb = np.array([5,7,2,3,5])
print(tomb)
print(type(tomb))
print(tomb.shape)
print(tomb.dtype)

tomb = np.array([3.14, 2.0, 5.2, 6.6])
print(tomb)
print(type(tomb))
print(tomb.shape)
print(tomb.dtype)

tomb = np.array([i for i in range(100)])
print(tomb)
tomb = tomb.reshape(10,10)
print(tomb)
tomb = tomb.reshape(5,5,4)
print(tomb)
print(tomb.shape)
tomb = tomb.reshape(2,2,5,5)
print(tomb.shape)

print(tomb[1,0,3,2])

tomb = np.array([i for i in range(128)])
print(tomb)
print(tomb[13])
print(tomb[10:20])
tomb = tomb.reshape(16,8)
print(tomb[5,4])
print(tomb[:5,3:6])

osszeg = 0
for i in range(tomb.shape[0]):
    for j in range(tomb.shape[1]):
        osszeg += tomb[i][j]
print(osszeg)

osszeg = 0
tomb = tomb.reshape(2,2,2,2,2,2,2)
for i in range(tomb.shape[0]):
    for j in range(tomb.shape[1]):
        for k in range(tomb.shape[2]):
            for l in range(tomb.shape[3]):
                for m in range(tomb.shape[4]):
                    for n in range(tomb.shape[5]):
                        for o in range(tomb.shape[6]):
                            osszeg += tomb[i,j,k,l,m,n,o]                    
print(osszeg)
osszeg = 0
for item in np.nditer(tomb):
    osszeg += item
print(osszeg)
tens = tomb[tomb % 10 == 0]
print(tens)

tomb = np.random.randint(1, 101, size = 100)
print(tomb)
tomb.sort()
print(tomb)

tomb = np.random.normal(size = 20)
print(tomb)

#tetejére: import matplotlib.pyplot as plt #pip install matplotlib
tomb = np.random.choice(["alma", "banán", "citrom"], size = 50, p = [0.7, 0.2, 0.1])
print(tomb)

uniques, counts = np.unique(tomb, return_counts=True)
print(uniques)
print(counts)

plt.bar(uniques, counts)
plt.show()

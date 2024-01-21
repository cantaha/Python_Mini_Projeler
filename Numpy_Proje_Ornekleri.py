import numpy as np

numpylist1 = np.array([10,15,30,45,60])

numpylist2 = np.arange(5,15)

numpylist3 = np.arange(50,100,5)

numpylist4 = np.zeros(10)

numpylist5 = np.ones(10)

numpylist6 = np.linspace(0,100,5)

numpylist7 = np.random.randint(10,30,5)

numpylist8 = np.random.randn(5)

numpylist9 = numpylist2.reshape(2,5)

numpylist10 = numpylist9.sum(axis=1)

numpylist11 = numpylist9.sum(axis=0)

numpylist12 = numpylist9.argmax()
numpylist12 = numpylist9.argmin()

numpylist13 = np.arange(10,20)
numpylist13_result = numpylist13[0:3]
numpylist13_result = numpylist13[::-1]

numpylist14 = numpylist9[:1]

numpylist15 = numpylist9[1,2]

numpylist16 = numpylist9[:,0]

numpylist17 = np.sqrt(numpylist9)

numpylist18 = numpylist9 %2 == 0
print(numpylist9[numpylist18])
print(numpylist9)


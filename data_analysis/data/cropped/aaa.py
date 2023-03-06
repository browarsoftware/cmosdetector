import numpy as np
v01 = np.loadtxt('data01.csv', delimiter=',')
v02 = np.loadtxt('data02.csv', delimiter=',')
x = v01 + v02
np.savetxt('rp1.3.csv', x, delimiter=',')

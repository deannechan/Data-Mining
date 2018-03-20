import numpy as np
from scipy.sparse import linalg

L = np.asarray([
    [2,-1,-1,0,0,0,0,0],
    [-1,2,0,-1,0,0,0,0],
    [-1,0,2,-1,0,0,0,0],
    [0,-1,-1,3,-1,0,0,0],
    [0,0,0,-1,3,-1,-1,0],
    [0,0,0,0,-1,2,0,-1],
    [0,0,0,0,-1,0,2,-1],
    [0,0,0,0,0,-1,-1,2]
], dtype=np.float32)
# print L

[D, X] = linalg.eigs(L, 2)
s = X[:, 0] # this is the 2nd eigenvecotr
print "D - ", D
print "------"
print "X - ", X
print "------"
print "S - ", s
print "------"
w, v = linalg.eigs(L)
# seen = {}
# unique_eigenvalues = []
# for (x, y) in zip(w, v):
#     if x in seen:
#         continue
#     seen[x] = 1
#     unique_eigenvalues.append((x, y))
# fiedler = sorted(unique_eigenvalues)[1][1]
print w
print "------"
print v
# print "fiedler - ", fiedler


evals,evec = np.linalg.eigh(L) 
ind = np.argsort(evals) 
evals = evals[ind] 
evec = evec[:,ind]
np.set_printoptions(precision=3, suppress=True)
print "-------"
print "-------"
print ind
print evals
print evec

fiedler = evec[:,1] 
connectivity = evals[1]
print "-------"
print "Fiedler"
print fiedler
print connectivity
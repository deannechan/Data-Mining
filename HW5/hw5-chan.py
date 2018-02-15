import numpy as np

m = np.asarray([[0.5, 0.5, 0],[0.5, 0, 1],[0, 0.5, 0]])
v = np.asarray([[0.33],[0.33], [0.33]])
print "[0]: \n", v
for k in range(1,51):
    prev = v
    v = np.dot(m,v)
    print "[", k, "]: \n", np.matrix.round(v,4)
    if np.array_equal(np.matrix.round(prev,4), np.matrix.round(v,4)):
        r = k
        print "stable value of r is found at", r
        break

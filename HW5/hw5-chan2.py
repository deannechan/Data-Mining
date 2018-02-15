import numpy as np

b=0.85
m = np.asarray([[0,0,1],[0.5,0,0],[0.5,1,0]])
v = np.asarray([[0.33],[0.33], [0.33]])
e = np.asarray([[1],[1],[1]])
print "[0]: \n", v
for k in range(1,50):
    v = np.dot(b * m, v) + np.dot((1-b),e)/3
    print "[", k, "]: \n", np.matrix.round(v,4)

a = v[0]
b = v[1]
c = v[2]

print round((.95 * a),6) == round((.9 * c) + (.05 * b),6)
print round((.85 * c),6) == round(b + (.575 * a), 6)
print round((.85 * a),6) == round(c + (.15 * b),6)
print round(a,6) == round(c + (.15 * b),6)
print round((0.95 * b),6) == round((0.475 * a) + (0.05 * c),6)
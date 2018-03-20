for_u = [-1,-2,-3,1,2,3]
for_v = [-4,-2,-4,1,1,1]
for_b = [-1,-1,-1,1,1,1]
c=0.1
n=0.2

# first iteration u,v,b
u = 0.000
v = 1.000
b = -2.000
#for each iteration
for x in range(1, 76):
    pattern=[0,0,0,0,0,0]
    pattern[0] = 0 if u+(4*v)+b >= 1 else 1
    pattern[1] = 0 if (2*u)+(2*v)+b >=1 else 1
    pattern[2] = 0 if (3*u)+(4*v)+b >= 1 else 1
    pattern[3] = 0 if u+v+b <= -1 else 1
    pattern[4] = 0 if (2*u)+v+b <= -1 else 1
    pattern[5] = 0 if (3*u)+v+b <= -1 else 1

    temp_u = 0
    temp_v = 0
    temp_b = 0
    for i in range(len(pattern)):
        if pattern[i] == 1:
            temp_u += for_u[i]

    for i in range(len(pattern)):
        if pattern[i] == 1:
            temp_v += for_v[i]

    for i in range(len(pattern)):
        if pattern[i] == 1:
            temp_b += for_b[i]

    du = u + c * temp_u
    dv = v + c * temp_v
    db = b + c * temp_b

    new_u = u - (n * du)
    new_v = v - (n * dv)
    new_b = b - (n * db)

    print "\nITERATION ", x
    print "u: ", round(u,3)
    print "v: ", round(v,3) 
    print "b: ", round(b,3)
    print "d/du: ", round(du,3)
    print "d/dv: ", round(dv,3)
    print "d/db: ", round(db,3)

    u = round(new_u,3)
    v = round(new_v,3)
    b = round(new_b,3)

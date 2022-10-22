#Problem 1

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {2, 4}
B = {1, 2, 8}
C = {1, 2, 5, 6, 10}

print (f"Intersection of sets A and C = {A.intersection(C)}")
print (f"Union of sets A and B = {A.union(B)}")
print (f"The compliment of C = {U - C}")
print (f"B - C = {B - C}")
print (f"The intersection of the compliment of B = {C.intersection(U - B)}")

#Problem 2
i = 10
A = {4*x for x in range (1, i)}
B = {2*y for y in range (1, i)}
C = {z**2 for z in range(1, i)}

print (A.intersection(B.union(C)))

for i in range(0, 6):
    print(f"i: {i} = {3 - 2*i + i**2}")
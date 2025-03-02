# Define sets A, B, and C
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# (a) Number of elements in A and B
print("\n(a) Elements in A or B:", sorted(A | B), "\nCount:", len(A | B))

# (b) Number of elements in B that are not in A or C
B_not_AC = B - (A | C)
print("\n(b) Elements in B not in A or C:", sorted(B_not_AC), "\nCount:", len(B_not_AC))

# (c) Set operations with sorting for better readability

# (i) Elements in C but not in A or B
print("\n(c.i) C not in A or B:", sorted(C - (A | B)))

# (ii) Elements common to all three sets
print("\n(c.ii) Common in A, B, and C:", sorted(A & B & C))

# (iii) Elements in A ∩ B or B ∩ C
print("\n(c.iii) A ∩ B or B ∩ C:", sorted((A & B) | (B & C)))

# (iv) Elements in A ∩ C but not in B
print("\n(c.iv) A ∩ C not in B:", sorted((A & C) - B))

# (v) Elements present in all three sets
print("\n(c.v) Present in A, B, and C:", sorted(A & B & C))

# (vi) Unique elements in B (not in A or C)
print("\n(c.vi) Unique to B:", sorted(B - (A | C)))
#Q3
def reverse_rec(L):
    if len(L) == 0:
        return []
    if len(L) == 1:
        return [L[0]]
    
    return reverse_rec(L[1:]) + [L[0]]

#Q1
def power(x, n):
    #if n == 1:
    #    return x
    if n == 0:
        return 1
    return power(x, n-1)*x

print(power(2, 3))


#Q2
def interleave(L1, L2):
    if len(L1) != len(L2):
        return False
    if len(L1) == 0 or len(L2) ==0:
        return []
    if len(L1) == 1:
        return [[L1[0]], [L2[0]]]
    mid = len(L1)//2
    return interleave(L1[:mid], L2[:mid]) + interleave(L1[mid:], L2[mid:])


def interleave2(L1,L2):
    if len(L1) == 0:
        return []
    return [L1[0],L2[0]] + interleave2(L1[1:],L2[1:])
L1 = [1, 2, 3]
L2 = [4, 5, 6]

print(interleave(L1, L2))

#Q4
def zigzag1(L):
    if len(L) == 0:
        return []
    elif len(L) == 1:
        return [L[0]]
    return zigzag1(L[1:-1]) + [L[0]] + [L[-1]]

    
L = [2, 3, 4, 5, 6]
print(zigzag1(L))
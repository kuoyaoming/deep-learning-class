from and_gate import AND
from or_gate import OR
from xor_gate import XOR

def FA(a, b, ci):
    s1 = XOR(a,b)
    S = XOR(s1,ci)
    s2 = AND(s1,ci)
    s3 = AND(a,b)
    C = OR(s2,s3)
    return S,C

if __name__ == '__main__':
    for xs in [(0, 0, 0),(1, 0, 0),(0, 1, 0),(1, 1, 0),(0, 0, 1),(1, 0, 1),(0, 1, 1),(1, 1, 1),]:
        y = full_adder(xs[0], xs[1], xs[2])
        print(str(xs) + " -> " + " C_out:" + str(y[1])+ " S:" + str(y[0]))
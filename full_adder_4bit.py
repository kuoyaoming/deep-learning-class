from full_adder import FA

def FA_4b(a,b,c0):
    s1 = FA(a[0],b[0],c0)
    s2 = FA(a[1],b[1],s1[1])
    s3 = FA(a[2],b[2],s2[1])
    s4 = FA(a[3],b[3],s3[1])
    S = (s1[0],s2[0],s3[0],s4[0])
    return s4[1], S

if __name__ == '__main__':
    a = (1,0,1,0)
    b = (0,1,0,1)
    c0 = (1) 
    y = FA_4b(a, b, c0)
    print(str(xs) + " -> " + " C4:" + str(y[0]) + " S:" + str(y[1]))
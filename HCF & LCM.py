a = int(input('FIRST NUMBER : '))
b = int(input('SECOND NUMBER : '))
def compute_hcf(x,y):
    while(y):
        x,y = y,x%y
    return x
hcf = compute_hcf(a,b)
print(f'The H.C.F. of {a} and {b} is : ',hcf)
lcm = int((a*b)/hcf)
print(f'The L.C.M. of {a} and {b} is : ',lcm)

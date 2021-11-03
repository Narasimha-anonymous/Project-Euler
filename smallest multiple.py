smallest_multiple=False
n=2*3*5*7*11*13*17*19
check=[20,18,16,15,14,12]
while not smallest_multiple:
    for i in check:
        if n%i==0:
            smallest_multiple=True
        else:
            smallest_multiple=False
            n+=2*3*5*7*11*13*17*19
            #print(n)
            break
print(n)

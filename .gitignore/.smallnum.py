try:
    l,r = [int(x) for x in input().split(' ')]
    z=max(l,r)
    x=z
    y = min(l,r)
    while(x%y!=0):
        x+=z
    print(x)    
except:
    print ("Invalid Input")
    print(n)

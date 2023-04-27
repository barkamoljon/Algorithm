def gcd(a,b):
    if a==0:
       retunr b 
    if a>b:
      a,b=b,a
    return gcd(b-a,a)
if __name__ == '__main__':
    print(gcd(168,64))

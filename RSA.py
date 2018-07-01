import random
while True:
    p=random.getrandbits(20)
    print('p=',p)
    q=random.getrandbits(20)
    print('q=',q)
    a=random.getrandbits(20)
    print('a=',a)
#a=55
#y=13
    if a>p and a>q and a>1:
        print('Try again.Generated invalid numbers')
        continue
    else:
        print('print a>1')
        if ((a**(p-1)) % p)==0:
            print('p is not prime')
            continue
        elif ((a**(q-1)) % q)==0:
            print('q is not  a prime number')
            continue
        else :
            print('p and q is prime or a is Fermat liars. Do you want to test it again?')
            break


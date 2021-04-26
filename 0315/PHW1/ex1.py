# Ex-1. Check Prime Number
# Divide n by all integer i in [2,n] and check if the remainder is zero.
# if zero -> not prime, not zero -> prime 

def isPrime(n):   # check prime number function
    check = 1
    for i in range(2,n):
        if n % i == 0:
            check = 0
            break
        else: 
            continue
    if check == 1:
        return True
    else:
        return False


n = int(input("Type the integer: "))   # receive n from user
if n < 2 or n > 32767:
    print("Wrong Value! n should be [2,32767]")
else:
    print("Is it Prime Number? " + str(isPrime(n)))
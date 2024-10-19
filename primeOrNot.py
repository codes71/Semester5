def prime(num):
    if num==0:
        return
    if num>1:
        for i in range (2,num):
            if(num%i) == 0:
                return 1
            else:
                return 0

num = 3
if prime(num) == 1:
    print("Not Prime")
else: 
    print("Prime")
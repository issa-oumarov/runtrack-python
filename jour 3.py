for i in range(21):
        print(i)
#--------------------------------------------------------

for i in range(0, 21, 2):
        print(i)
#--------------------------------------------------------

for i in range(101):
    if i not in [26,37,88]:
        print(i)
#--------------------------------------------------------

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#---------------------------------------------------------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, 1001):
    if is_prime(i):
        print(i)
        
#--------------------------------------------------------

string = "abcdefghijklmnopqrstuvwxyz" * 10
n = 1
while n*(n+1)//2 <= len(string):
    start = (n-1)*n//2
    end = n*(n+1)//2
    print(string[start:end].center(0))
    n += 1
#--------------------------------------------------------

chaine = "nikana"
chaine_inverse = chaine[::-1]
print(chaine_inverse)

# Time Complexity

n = int(input("Enter your number: "))

# F(n) = n + 3
a = 5
for i in range(n):
    print(a + i)
b = 6
print(b + i)

# F(n) = 4(n^2) + 2n - 2
for i in range(n):
    for j in range(n):
        print(i)
        print(j)
        k = i + j
        t = k - 6
for i in range(n - 1):
    k = t
    t = 6
    
# F(n) = 1.3(n^2) + 2n
for i in range(n):
    for j in range(0,n,3):
        a = b
        b = c
        c = d
        d = e 
    e = k
    k = n 
    
# F(n) = 0.3(n^2) - 5.16n + 19.83
for i in range(10,n + 3,4):
    for j in range(20,2 * n,3):
        a = c
        b = d
    k = p 
    p = n 
    
# F(n) = 0.5(n^2) +1.5n
for i in range(n):
    for j in range(i,n,1):
        t += 5
    k -= 6
    
# F(n) = log(n)
while n > 1:
    n //= 2
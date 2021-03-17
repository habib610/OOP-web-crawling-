fib_x = 1
fib_next = 1

n = int(input()) # 4

if n <= 2:
    fib_n = 1
else:
    i = 3
    while i <= n:
        i+= 1
        fib_temp = fib_next + fib_x # 1 + 1 = 2
        fib_x = fib_next # 1
        fib_next = fib_temp
    fib_n = fib_next

print(fib_n)
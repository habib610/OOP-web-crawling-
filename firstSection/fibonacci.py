def find_fib_n_list(n):
    li = []
    if n <= 2:
        return li.append(1)
    fib_x, fib_next = 1, 1
    li.append(fib_next)
    li.append(fib_x)
    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
        # li.append(fib_x)
        li.append(fib_next)
    return li

# n = int(input())
# print(find_fib_n_list(n))

# for i in range(1, 11):
#     print(find_fin(i))
def div(a, b):
    try:
     return  a / b
    except ZeroDivisionError:
        return "Cannot divided by zero"
    except TypeError:
        return "Unsupported Type. Did You use String?"

print(div(10, 2))
print(div(10, 0))
print(div("9", 3))
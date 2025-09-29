def add():
    global a, b
    print(a+b)
    a, b = 3, 5

a, b = 2, 5
add()
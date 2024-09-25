def croix(x):
    for i in range(x):
        print (" " * i + "*" + (2*(x-i) -1) * " " + "*")
    print(" " * x + "*")
    for i in range(x):
        print(" " * (x-i-1) + "*" + (2*(i)+1 ) * " "+ "*")
croix(4)

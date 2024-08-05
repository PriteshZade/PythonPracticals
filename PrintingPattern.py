def prints(n):
    for i in range(1, n + 2):
        x = 1
        while x <= n + 2 - i:
            print(" ", end="")
            x = x + 1
        print("*", end="")
        y = 1
        while y <= 2 * (i - 1) - 1:
            if(i == n + 1 and y == n):
                print(n, end="")
            else:
                print(" ", end="")
            y = y + 1
        if i != 1:
            print("*")
        else:
            print("")

    for j in range(1, n):
        m = 1
        while m <= j + 1:
            print(" ", end="")
            m = m + 1
        print("*", end="")
        c = 1
        while c <= 2 * (n - j) - 1:
            print(" ", end="")
            c = c + 1
        print("*")

    for k in range(0, n):
        z = 1
        while z <= 5 + (n - 1) * 2:
            print("*", end="")
            z = z + 1
        print("")


def print_pattern(l):
    if(l < 1):
        return "Enter number greater than 0"
    if(type(l) == int):
        prints(l)
        quit()
    if(type(l) == float):
        x = int(l)
        y = l - x
        if(y == 0.0):
            prints(x)
            quit()
        else:
            return "Enter positive integer value"
    else:
        return "Invalid input"


print(print_pattern(3.000))

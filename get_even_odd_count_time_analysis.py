import time

def get_even_odd_count(L):
    c1 = 0 
    c2 = 0  
    for elem in L:
        if elem % 2 == 0:
            c1 += 1
        else:
            c2 += 1
    return (c1, c2)

def get_even_odd_count2(L):
    even_count = 0
    odd_count = 0
    for elem in L:
        t = elem % 2
        even_count += 1 - t
        odd_count += t
    return (even_count, odd_count)


a = time.perf_counter()
get_even_odd_count((2, 8, 6, 9))
b = time.perf_counter()
c = time.perf_counter()
get_even_odd_count2((2, 8, 6, 9))
d = time.perf_counter()

trad = b - a
met1 = d - c
print(trad)
print(met1)

if trad > met1:
    p = ((trad - met1) / trad) * 100
    print("Method 2 is " + str(p) + " percent faster than traditional Method")
else:
    p = ((met1 - trad) / trad) * 100
    print("Method 2 is " + str(p) + " percent slower than traditional Method")


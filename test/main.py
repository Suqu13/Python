def fib(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        print(a)
        a, b = b, a + b
        i += 1


fib(11)

for i in range(1,8,2):
    print(i)

words = ['mamy','duzego','czarnego','kota']

for w in words[:]:
    if(len(w) < 5):
        words.insert(3, w)
        print(w)


print(words[1])
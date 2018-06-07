reps = int(input())
for i in range(0, reps):
    
    read = input()
    odd = ""
    even = ""
    for i in range(0, len(read)):
        if i % 2 == 0:
            odd += read[i]
        else:
            even += read[i]
    print("{} {}".format(odd, even))
    
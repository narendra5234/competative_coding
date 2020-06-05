for t in range(int(input())):
    new = "0000000000"
    for i in range(int(input())):
        s = input()
        new = bin(int(new, 2) ^ int(s, 2))[2:]
    print(new.count('1'))


def read():
    i = input()
    if i == "ACCESS GRANTED":
        return True
    prefix = "ACCESS DENIED ("
    suffix = " ms)"
    return int(i[len(prefix) : len(i) - len(suffix)])


length = 1
while True:
    print("A" * length)
    res = read()
    if res is True:
        exit(0)
    if res > 5:
        break
    length += 1

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
password = "B" * length
overhead = 23

for i in range(length):
    for char in characters:
        password = password[:i] + char + password[i + 1 :]
        print(password)
        res = read()
        if res is True:
            exit(0)
        if res >= overhead:
            break
    else:
        exit(0)
    overhead += 9

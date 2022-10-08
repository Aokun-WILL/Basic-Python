while True:
    str_x = input()
    if str_x == "0":
        break

    count = 0
    for n in str_x:
        count += int(n)
    print(count)

num_A = []
numbers = 0

while True:
    numbers = int(input())
    if numbers == 0:
        break
num_A.append(numbers)

for i in range(len(num_A)):
    print("Case {}: {}".format(i + 1, num_A[i]))

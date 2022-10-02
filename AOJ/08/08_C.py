import sys
texts = sys.stdin.read()
texts = sys.lower()
letters = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
for i in texts:
    if ord(i) in range(ord('a'), ord('z') + 1):
        letters[i] += 1
[print(f'{k} : {v}') for k, v in letters.item()]

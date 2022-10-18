class Dice:
    def __init__(self, ary):
        self.__top = ary[0]
        self.__fro = ary[1]
        self.__rit = ary[2]
        self.__lft = ary[3]
        self.__bak = ary[4]
        self.__btm = ary[5]

    def turn_e(self):
        self.__top, self.__lft, self.__btm, self.__rit = self.__lft, self.__btm, self.__rit, self.__top

    def turn_s(self):
        self.__top, self.__fro, self.__btm, self.__bak = self.__bak, self.__top, self.__fro, self.__btm

    def turn_w(self):
        self.__top, self.__lft, self.__btm, self.__rit = self.__rit, self.__top, self.__lft, self.__btm

    def turn_n(self):
        self.__top, self.__fro, self.__btm, self.__bak = self.__fro, self.__btm, self.__bak, self.__top

    def is_same_setting(self, ary):
        if self.__top == ary[0] and self.__fro == ary[1] and self.__rit == ary[2] and self.__lft == ary[3] and self.__bak == ary[4] and self.__btm == ary[5]:
            return True

    def is_same_dice(self, ary):
        is_same = False
        for _ in range(2):
            for _ in range(3):
                for _ in range(4):
                    if self.is_same_setting(ary):
                        is_same = True
                    self.turn_w()
                self.turn_n()
            self.turn_e()
            self.turn_s()
        return is_same


n = int(input())
surfaces_stack = [None] * n
for i in range(n):
    surfaces_stack[i] = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        dice = Dice(surfaces_stack[i])
        if dice.is_same_dice(surfaces_stack[j]):
            print('No')
            break
    else:
        continue
    break
else:
    print('Yes')

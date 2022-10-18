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

    def show_top(self):
        return self.__top


surfaces = list(map(int, input().split()))
instructions = list(input())

dice = Dice(surfaces)

for inst in instructions:
    if inst == "E":
        dice.turn_e()
    if inst == "N":
        dice.turn_n()
    if inst == "S":
        dice.turn_s()
    if inst == "W":
        dice.turn_w()

print(dice.show_top())

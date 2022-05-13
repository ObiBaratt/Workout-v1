# from calc1rm import Calc1rm
#
# calc = Calc1rm()
#
# max_dict_from_calc1rm = calc.max_reps


class SquatOverload:
    def __init__(self, one_rm, max_dict):
        self.one_rm = one_rm
        self.max_dict = max_dict

        self.rep_hi = int(self.max_dict[3] * self.one_rm)
        self.rep_mid = int(self.max_dict[9] * self.one_rm)
        self.rep_low = int(self.max_dict[12] * self.one_rm)

        self.rep_4 = int(self.max_dict[4] * self.one_rm)
        self.rep_6 = int(self.max_dict[6] * self.one_rm)
        self.rep_20 = int(self.max_dict[18] * self.one_rm)

    def day1(self):
        return f'{self.rep_hi}x3, 2, 1\n/ {self.rep_mid}x8\n/ {self.rep_low}x10'

    def day2(self):
        return f'{self.rep_hi}x5, 3, 1\n/ {self.rep_mid}x8\n/ {self.rep_low}x8'

    def day3(self):
        return f'{self.rep_mid}x5\n/ {self.rep_6}x3\n/ {self.rep_4}x1\n/ {self.rep_hi}x1\n/ {self.rep_20}x20'


# squat = SquatWorkout(410, max_dict_from_calc1rm)
#
# print(squat.day1())
# print()
# print(squat.day2())
# print()
# print(squat.day3())



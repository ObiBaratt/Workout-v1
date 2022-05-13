# from calc1rm import Calc1rm
#
# calc = Calc1rm()
#
# max_dict_from_calc1rm = calc.max_reps


def squat_overload_func(one_rm, max_dict):
    squat = SquatOverload(one_rm=one_rm, max_dict=max_dict)
    return squat.day1(), squat.day2(), squat.day3()


class SquatOverload:
    def __init__(self, one_rm, max_dict):
        self.one_rm = one_rm
        self.max_dict = max_dict

        self.rep_hi = int(self.max_dict[3] * self.one_rm)
        self.rep_mid = int(self.max_dict[9] * self.one_rm)
        self.rep_low = int(self.max_dict[12] * self.one_rm)
        self.rep_5 = int(self.max_dict[5] * self.one_rm)
        self.rep_20 = int(self.max_dict[18] * self.one_rm)

        self.rep_next = int((self.rep_hi / self.max_dict[5]) * self.max_dict[3])

    def day1(self):
        return [(self.rep_hi, 3), (self.rep_hi, 2), (self.rep_hi, 1), (self.rep_mid, 8), (self.rep_low, 10)]

    def day2(self):
        return [(self.rep_hi, 5), (self.rep_hi, 3), (self.rep_hi, 1), (self.rep_mid, 8), (self.rep_low, 8)]

    def day3(self):
        return [(self.rep_mid, 5), (self.rep_5, 3), (self.rep_hi, 1), (self.rep_next, 1), (self.rep_20, 20)]

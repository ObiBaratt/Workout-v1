def round_nearest_five(x):
    return 5 * round(x / 5)


def percent1rm(one_rm, percent):
    return one_rm * percent


def set_calc(one_rm, percent):
    return round_nearest_five(percent1rm(one_rm, percent))


class NuckolsPress:
    def __init__(self, one_rm):
        self.one_rm = one_rm
        self.percent80 = set_calc(self.one_rm, 0.80)
        self.percent85 = set_calc(self.one_rm, 0.85)
        self.percent90 = set_calc(self.one_rm, 0.90)

    def day1(self):
        return [(self.percent80, 5), (self.percent80, 5), (self.percent80, 5), (self.percent80, 5),
                (self.percent85, 3), (self.percent85, 'AMAP')]

    def day2(self):
        return [(self.percent80, 5), (self.percent80, 5), (self.percent85, 3), (self.percent85, 3),
                (self.percent85, 3), (self.percent85, 'AMAP')]

    def day3(self):
        return [(self.percent85, 3), (self.percent85, 3), (self.percent85, 3), (self.percent90, 1),
                (self.percent90, 1), (self.percent90, 'AMAP')]


class NuckolsSquat:
    def __init__(self, one_rm):
        self.one_rm = one_rm
        self.percent80 = set_calc(self.one_rm, 0.80)
        self.percent84 = set_calc(self.one_rm, 0.84)
        self.percent90 = set_calc(self.one_rm, 0.90)
        self.percent92 = set_calc(self.one_rm, 0.92)
        self.percent95 = set_calc(self.one_rm, 0.95)

    def day1(self):
        return [(self.percent80, 'AMAPx3. Goal: 8'), (self.percent84, 'AMAP if > goal')]

    def day2(self):
        return [(self.percent90, 'AMAPx3. Goal: 5'), (self.percent92, 'AMAP if > goal')]

    def day3(self):
        return [(self.percent95, 'AMAPx3. Goal: 3')]


class NuckolsDeadlift:
    def __init__(self, one_rm):
        self.one_rm = one_rm
        self.percent60 = set_calc(self.one_rm, 0.60)
        self.percent65 = set_calc(self.one_rm, 0.65)
        self.percent70 = set_calc(self.one_rm, 0.70)
        self.percent80 = set_calc(self.one_rm, 0.80)
        self.percent92 = set_calc(self.one_rm, 0.92)
        self.percent95 = set_calc(self.one_rm, 0.95)

#         print(rfive(0.80 * tmax), '4x5'), print(rfive(0.60 * tmax), '6x3 EMOM'), print('Rows 3x10'), print(
#             'Shrugs 3x10'), print('Hip Thrusts 3x10')
#     elif '2' in level:
#         print(rfive(0.90 * tmax), '2x1'), print(rfive(0.85 * tmax), '3x3'), print(rfive(0.65 * tmax),
#                                                                                   '6x3 EMOM'), print(
#             'Rows 4x10'), print('Shrugs 4x10'), print('Hip Thrusts + 4x10')
#     elif '3' in level:
#         print(rfive(0.70 * tmax), '6x3 EMOM'), print('Rows 3x8'), print('Shrugs 3x8'), print('Hip Thrusts ++ 3x8')
#     else:
#         print('Time to max. Warmup and get to it!')
#     print()
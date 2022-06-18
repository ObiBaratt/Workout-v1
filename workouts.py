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
                (self.percent85, 3), (self.percent85, 'AMAP, 5+')]

    def day2(self):
        return [(self.percent80, 5), (self.percent80, 5), (self.percent85, 3), (self.percent85, 3),
                (self.percent85, 3), (self.percent85, 'AMAP, 5+')]

    def day3(self):
        return [(self.percent85, 3), (self.percent85, 3), (self.percent85, 3), (self.percent90, 1),
                (self.percent90, 1), (self.percent90, 'AMAP, 3+')]

    def return_workouts(self):
        return self.day1(), self.day2(), self.day3()


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

    def return_workouts(self):
        return self.day1(), self.day2(), self.day3()


class NuckolsDeadlift:
    def __init__(self, one_rm):
        self.one_rm = one_rm
        self.percent60 = set_calc(self.one_rm, 0.60)
        self.percent65 = set_calc(self.one_rm, 0.65)
        self.percent70 = set_calc(self.one_rm, 0.70)
        self.percent80 = set_calc(self.one_rm, 0.80)
        self.percent85 = set_calc(self.one_rm, 0.85)
        self.percent90 = set_calc(self.one_rm, 0.90)

    def day1(self):
        return [(self.percent80, 5), (self.percent80, 5), (self.percent80, 5), (self.percent80, 5),
                (self.percent60, '6x3 EMOM')]

    def day2(self):
        return [(self.percent90, 1), (self.percent90, 1), (self.percent85, 3), (self.percent85, 3), (self.percent85, 3),
                (self.percent65, '6x3 EMOM')]

    def day3(self):
        return [(self.percent70, '6x3 EMOM')]

    def return_workouts(self):
        return self.day1(), self.day2(), self.day3()


class SquatOverload:
    def __init__(self, one_rm):
        self.one_rm = one_rm

        self.rep_hi = round_nearest_five(self.one_rm * 0.94)
        self.rep_mid = round_nearest_five(self.one_rm * 0.78)
        self.rep_low = round_nearest_five(self.one_rm * 0.71)
        self.rep_5 = round_nearest_five(self.one_rm * 0.89)
        self.rep_20 = round_nearest_five(self.one_rm * 0.63)
        self.rep_next = int((self.rep_hi / 0.89) * 0.94)

    def day1(self):
        return [(self.rep_hi, 3), (self.rep_hi, 2), (self.rep_hi, 1), (self.rep_mid, 8), (self.rep_low, 10)]

    def day2(self):
        return [(self.rep_hi, 5), (self.rep_hi, 3), (self.rep_hi, 1), (self.rep_mid, 8), (self.rep_low, 8)]

    def day3(self):
        return [(self.rep_mid, 5), (self.rep_5, 3), (self.rep_hi, 1), (self.rep_next, 1), (self.rep_20, 20)]

    def return_workouts(self):
        return self.day1(), self.day2(), self.day3()


# TODO: Make this work on app.py main route
# squat = NuckolsSquat(365)
# deadlift = NuckolsDeadlift(405)
#
# workout = {}
#
# workout['nuckolsSquat'] = squat.return_workouts()
# print(workout)
#
# workout['nuckolsDeadlift'] = deadlift.return_workouts()
# print(workout)
#
# print(workout['nuckolsSquat'])
#
# print(workout['nuckolsDeadlift'])
#
# print('for loop')
#
# for i in range(len(workout['nuckolsDeadlift'])):
#     print(workout['nuckolsDeadlift'][i])
# print('end')
#
# if workout['nuckolsDeadlift']:
#     print(workout['nuckolsDeadlift'])
# try:
#      print(workout['overload'])
# except KeyError:
#     print('does not exist')
#

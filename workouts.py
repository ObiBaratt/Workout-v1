def round_nearest_five(x):
    return 5 * round(x / 5)


class NuckolsPress:
    def __init__(self, one_rm):
        self.one_rm = one_rm

        self.percent80 = round_nearest_five(0.80 * self.one_rm)
        self.percent85 = round_nearest_five(0.85 * self.one_rm)
        self.percent90 = round_nearest_five(0.90 * self.one_rm)

    def day1(self):
        return [(self.percent80, 5), (self.percent80, 5), (self.percent80, 5), (self.percent80, 5),
                (self.percent85, 3), (self.percent85, 'AMAP')]

    def day2(self):
        return [(self.percent80, 5), (self.percent80, 5), (self.percent85, 3), (self.percent85, 3),
                (self.percent85, 3), (self.percent85, 'AMAP')]

    def day3(self):
        return [(self.percent85, 3), (self.percent85, 3), (self.percent85, 3), (self.percent90, 1),
                (self.percent90, 1), (self.percent90, 'AMAP')]

# def squat(tmax, level):
#     '''
#     Creates a Squat workout plan when tmax is int or float and level is str.
#     '''
#
#     print()
#     print('Squat Level', level, 'Selected.')
#     if '1' in level:
#         print(rfive(0.80 * tmax), '3xAMAP, Goal: 8 ', 'If >10 reps then: ', rfive(0.84 * tmax)), print(
#             'One Handed Rows 3x12'), print('Leg Presses 3x12'), print('Deficit Deadlifts 3x12'), print(
#             'Plank + L/R Side Planks')
#     elif '2' in level:
#         print(rfive(0.90 * tmax), '3xAMAP, Goal: 5 ', 'If >6 reps then: ', rfive(0.92 * tmax)), print(
#             'One Handed Rows 3x10 +'), print('Leg Presses 3x10 +'), print('Deficit Deadlifts 3x10 +'), print(
#             'Plank + L/R Side Planks')
#     elif '3' in level:
#         print(rfive(0.95 * tmax), '3xAMAP, Goal: 3'), print('One Handed Rows ++ 3x8'), print(
#             'Leg Presses 3x8 ++'), print('Deficit Deadlifts 3x8 ++'), print('Plank + L/R Side Planks')
#     else:
#         print('Time to max. Warmup and get to it!'), print('Cooldown with:'), print(rfive(0.70 * tmax), '3x10'), print(
#             'Leg Presses 1-2x15-20'), print('Deficit Deadlifts 1-2x15-20')
#     print()
#
#
# def deadlift(tmax, level):
#     '''Creates a Deadlift workout plan when tmax is int or float and level is str'''
#
#     print()
#     print('Deadlift Level', level, 'Selected.')
#     if '1' in level:
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
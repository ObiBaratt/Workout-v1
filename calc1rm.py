class Calc1rm:
    def __init__(self):
        self.max_reps = {1: 1, 2: 0.97, 3: 0.94, 4: 0.92, 5: 0.89,
                         6: 0.86, 7: 0.83, 8: 0.81, 9: 0.78, 10: 0.75,
                         11: 0.73, 12: 0.71, 13: 0.70, 14: 0.68, 15: 0.67,
                         16: 0.65, 17: 0.64, 18: 0.63, 19: 0.61, 20: 0.60}

        self.one_rm = 0

    def calc_one_rm(self, weight, reps):
        max_percent = self.max_reps[reps]
        self.one_rm = int(weight / max_percent)
        return self.one_rm

from pandas import read_csv


class DataManager:
    def __init__(self, filename, columns, target):
        self.filename, self.columns, self.target = filename, columns, target
        self.df, self.X, self.y = None, None, None

    def make_design(self):
        self.df = read_csv(self.filename)
        self.X = self.df[self.columns].values
        self.y = self.df[self.target].values

    def get_matrix(self):
        return self.X

    def get_target(self):
        return self.y
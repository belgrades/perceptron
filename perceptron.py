import numpy as np

# TODO: Add different constructors to simulate entry https://docs.python.org/3/tutorial/classes.html
# TODO: Add plots


class SimplePerceptron:
    def __init__(self, X, y, g):
        self.X = X
        self.y = y
        self.g = g
        self.l, self.p = X.shape
        self.w = None
        self.b = None

    def fit(self):
        self.w, self.b, cc = np.zeros(self.p), 0, 0

        while cc < self.l:
            for i in range(self.l):
                if self.y[i] * self.g(np.inner(self.w, self.X[i, :]) + self.b) <= 0:
                    self.w = self.w + self.y[i] * self.X[i, :]
                    self.b = self.b + self.y[i]
                else:
                    cc = cc + 1
            if cc < self.l:
                cc = 0

    def get_model(self):
        return self.w, self.b

    def evaluate(self, x):
        return self.g(np.inner(self.w, x)+self.b)


def perceptron_vector(X, y, g):
    l, p = X.shape
    w, b, cc = np.zeros(p), 0, 0

    while cc < l:
        for i in range(l):
            if y[i]*g(np.inner(w, X[i, :])+b) <= 0:
                w = w + y[i]*X[i, :]
                b = b + y[i]
            else:
                cc = cc + 1
        if cc < l:
            cc = 0

    return w, b


def perceptron(X, y):
    l, p = X.shape

    # Define matrix of w of shape (l, 1)
    w, b = np.matrix(np.zeros((p, 1))), np.matrix(np.zeros((1,1)))
    k, cc = 0, 0

    while cc < l:
        for i in range(l):
            print
            print(" Response "+str(i))
            print(b[0, k])
            print(w[:, k])
            print(w)
            print(y[i]*(np.inner(w[:, k].T, X[i, :])[0, 0]+b[0, k]), y[i])
            print(b)

            print(y[i]*(np.inner(w[:, k].T, X[i, :])[0, 0]+b[0, k]), y[i]*(np.inner(w[:, k].T, X[i, :])[0, 0]+b[0, k])<=0)

            if y[i]*(np.inner(w[:, k].T, X[i, :])[0, 0]+b[0, k]) <= 0:
                w = np.c_[w, w[:, k] + y[i]*X[i, :].reshape(2,1)]
                b = np.c_[b, b[0, k] + y[i]]
                k = k + 1
            else:
                cc = cc + 1

        if cc < l:
            print("cc" + str(cc))
            print(w[:, k])
            print(b[0, k])

            w, b = w[:, k], np.matrix(b[0, k])
            k = 0
            print(w)
            print(b)
            cc = 0

    return w, b
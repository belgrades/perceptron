import sys
from pandas import read_csv
import numpy as np
from perceptron import perceptron

# TODO: Send X as df[size - 1]


def main():
    filename = sys.argv[1]
    df = read_csv(filename)

    a, b = perceptron(X=df[['x1', 'x2']].values,
                      y=df['y'].values)

    print("final")
    print(a, b)

if __name__ == "__main__":
    main()

import sys
from pandas import read_csv
from perceptron import perceptron, perceptron_vector, SimplePerceptron
from activation import sgn

# TODO: Send X as df[size - 1]


def main():

    filename = sys.argv[1]
    df = read_csv(filename)

    a, b = perceptron(X=df[['x1', 'x2']].values,
                      y=df['y'].values)

    print("final")
    print(a, b)

    p = SimplePerceptron(X=df[['x1', 'x2']].values,
                         y=df['y'].values,
                         g=sgn)
    p.fit()
    print(p.get_model())

if __name__ == "__main__":
    main()

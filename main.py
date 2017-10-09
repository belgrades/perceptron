import sys
import numpy as np
from perceptron import perceptron, perceptron_vector, SimplePerceptron
from activation import sgn
from data import DataManager
# TODO: Send X as df[size - 1]


def main():
    filename = sys.argv[1]
    dm = DataManager(filename=filename,
                     columns=['x1', 'x2'],
                     target='y')

    dm.make_design()

    model = SimplePerceptron(X=dm.get_matrix(),
                             y=dm.get_target(),
                             g=sgn)
    model.fit()

    print(model.get_model())
    print(model.evaluate(np.array([0.25, 1.5])))

if __name__ == "__main__":
    main()

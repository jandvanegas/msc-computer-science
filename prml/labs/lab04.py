import math
import os

import matplotlib.pyplot as plt
import numpy as np

from prml import prml


def main():
    data_path = os.environ["DATA_PATH"]
    plt.figure()
    XPlot = np.linspace(-8, 12, 1000)
    m = np.ones((1, 1)) * 1.0
    C = np.ones((1, 1)) * 2.0
    result = prml.logpdf_GAU_ND(prml.vrow(XPlot), m, C)
    plt.plot(XPlot.ravel(), np.exp(result))
    plt.show()

    XND1 = np.load(os.path.join(data_path, './lab04/X1D.npy'))
    m = prml.mean(XND1)
    C = prml.covariance(XND1)

    plt.figure()
    plt.hist(XND1.ravel(), bins=50, density=True)
    XPlot = np.linspace(-8, 12, 1000)
    plt.plot(XPlot.ravel(), np.exp(prml.logpdf_GAU_ND(prml.vrow(XPlot), m, C)))
    plt.show()


if __name__ == '__main__':
    main()

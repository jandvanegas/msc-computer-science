import numpy as np
import prml
import matplotlib.pyplot as plt


def test_logpdf_GAU_ND():
    XND = np.load('./XND.npy')
    mu = np.load('./muND.npy')
    C = np.load('./CND.npy')
    pdfSol = np.load('./llND.npy')
    pdfGau = prml.logpdf_GAU_ND(XND, mu, C)
    assert np.abs(pdfSol - pdfGau).max() == 0.0

    XPlot = np.linspace(-8, 12, 1000)
    m = np.ones((1, 1)) * 1.0
    C = np.ones((1, 1)) * 2.0
    pdfSol = np.load('./llGAU.npy')
    pdfGau = prml.logpdf_GAU_ND(prml.vrow(XPlot), m, C)
    assert np.abs(pdfSol - pdfGau).max() == 0.0


def test_mean_x_input():
    expected_mean = np.array([[-0.07187197], [0.05989594]])
    expected_empirical_covariance = np.array(
        [
            [0.94590166, 0.09313534],
            [0.09313534, 0.8229693]
        ])
    XND = np.load('./XND.npy')

    mean = prml.mean(XND)
    empirical_covariance = prml.covariance(XND)
    assert np.abs(mean - expected_mean).sum() < 0.001
    assert np.abs(
        expected_empirical_covariance - empirical_covariance).sum() < 0.001

    ll = prml.loglikelihood(XND, mean, empirical_covariance)
    assert abs(-270.70478023795044 - ll) < 0.00001

    XND1 = np.load('./X1D.npy')
    m = prml.mean(XND1)
    assert (m - np.array([1.9539157])) < 0.000001
    C = prml.covariance(XND1)
    assert (C - np.array([6.0954228])) < np.array([[0.00001]])

    plt.figure()
    plt.hist(XND1.ravel(), bins=50, density=True)
    XPlot = np.linspace(-8, 12, 1000)
    plt.plot(XPlot.ravel(), np.exp(prml.logpdf_GAU_ND(prml.vrow(XPlot), m, C)))

import numpy as np
import scipy.special

import src.prml.prml as prml
import matplotlib.pyplot as plt


def main_multiclass():
    prior = prml.vcol(np.array([1.0 / 3, 1.0 / 3, 1.0 / 3]))
    C = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    L = np.load('lab08/commedia_labels.npy')
    llCond = np.load('lab08/commedia_ll.npy')
    DCF = multiclass_evaluate(L, llCond, C, prior)
    print(f"DCF for epsilon 0.001 {DCF}")

    L = np.load('lab08/commedia_labels_eps1.npy')
    llCond = np.load('lab08/commedia_ll_eps1.npy')
    DCF = multiclass_evaluate(L, llCond, C, prior)
    print(f"DCF for epsilon 1 {DCF}")


def main_binary_analysis():
    ll_ratio_0_001 = np.load(
        'lab08/commedia_llr_infpar.npy')
    L_0_001 = np.load('lab08/commedia_labels_infpar.npy')
    ll_ratio_1 = np.load(
        'lab08/commedia_llr_infpar_eps1.npy')
    L_1 = np.load('lab08/commedia_labels_infpar_eps1.npy')
    prior = 0.8
    Cfn = 1
    Cfp = 10
    binary_evaluation(ll_ratio_0_001, L_0_001, prior, Cfn, Cfp)
    binary_min_detection_cost(ll_ratio_0_001, L_0_001, prior, Cfn, Cfp)
    binary_plot_roc(ll_ratio_0_001, L_0_001)
    binary_plot_error(ll_ratio_0_001, L_0_001)
    binary_plot_error(ll_ratio_1, L_1, colors=('y', 'b'))
    plt.show()


def binary_evaluation(ll_ratio, L, prior, Cfn, Cfp, t=None):
    _, FPR, FNR, _ = prml.optimal_bayes(ll_ratio, L, prior, Cfn, Cfp, t)
    DCFu = prior * Cfn * FNR + (1 - prior) * Cfp * FPR
    B_dummy = min(prior * Cfn, (1 - prior) * Cfp)
    return DCFu / B_dummy


def binary_min_detection_cost(ll_ratio, L, prior, Cfn, Cfp):
    thresholds = np.array(ll_ratio)
    thresholds.sort()
    thresholds = np.concatenate(
        [np.array([-np.inf]), thresholds, np.array([np.inf])])
    thresholds_size = thresholds.shape[0]
    DCFs = np.zeros(thresholds_size)
    for i, t in enumerate(thresholds):
        DCFs[i] = binary_evaluation(ll_ratio, L, prior, Cfn, Cfp, t)
    return np.min(DCFs)


def binary_plot_roc(ll_ratio, L):
    thresholds = np.array(ll_ratio)
    thresholds.sort()
    thresholds = np.concatenate(
        [np.array([-np.inf]), thresholds, np.array([np.inf])])
    thresholds_size = thresholds.shape[0]
    FPR_vector = np.zeros(thresholds_size)
    FNR_vector = np.zeros(thresholds_size)
    for i, t in enumerate(thresholds):
        _, FPR, FNR, _ = prml.optimal_bayes(ll_ratio, L, 0, 1, 1, t)
        FPR_vector[i] = FPR
        FNR_vector[i] = FNR
    plt.plot(FPR_vector, 1 - FNR_vector)
    plt.show()


def binary_plot_error(ll_ratio, L, colors=('r', 'b')):
    Cfn = 1
    Cfp = 1
    effPriorLogOdds = np.linspace(-3, 3, 21)
    effPriorLogOddsSize = effPriorLogOdds.shape[0]
    effectivePrior = 1 / (1 + np.exp(-effPriorLogOdds))
    DCF = np.zeros(effPriorLogOddsSize)
    minDCF = np.zeros(effPriorLogOddsSize)
    for i, prior in enumerate(effectivePrior):
        DCF[i] = binary_evaluation(ll_ratio, L, prior, Cfn, Cfp)
        minDCF[i] = binary_min_detection_cost(ll_ratio, L, prior,
                                              Cfn, Cfp)
    plt.plot(effPriorLogOdds, DCF, label='DCF', color=colors[0])
    plt.plot(effPriorLogOdds, minDCF, label='minDCF', color=colors[1])
    plt.ylim([0, 1.1])
    plt.xlim([-3, 3])


def multiclass_evaluate(L, llCond, C, prior):
    llJoint = llCond + np.log(prior)
    llMarginal = scipy.special.logsumexp(llJoint, axis=0)
    Post = np.exp(llJoint - llMarginal)
    B_dummy = np.min(np.dot(C, prior))
    Weighted_Post = C @ Post
    prediction = np.argmin(Weighted_Post, axis=0)
    confusion = prml.compute_confusion_matrix(np.unique(L), L, prediction)
    mis_classification_ratio = confusion / confusion.sum(axis=0)
    DCFu = np.sum(
        prml.vrow(prior) * np.sum(mis_classification_ratio * C, axis=0))
    DCF = DCFu / B_dummy
    return DCF


if __name__ == '__main__':
    main_binary_analysis()

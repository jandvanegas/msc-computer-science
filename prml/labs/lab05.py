import numpy as np
import scipy.special
import sklearn.datasets

import prml


def main():
    D, L = load_iris()
    classifier = 'tied_naive'
    samples = D.shape[1]
    errors = []
    for i in range(samples):
        DTR = np.delete(D, i, axis=1)
        LTR = np.delete(L, i)
        mean, covariance = compute_classifier(DTR, LTR, classifier=classifier)
        DTE = D[:, i:i+1]
        LTE = L[i:i+1]
        evaluation = evaluate(DTE, LTE, mean, covariance,
                              logarithmically=False)
        errors.append(evaluation['err'])
    return np.average(errors)


def training_50_50(classifier):
    D, L = load_iris()
    (DTR, LTR), (DTE, LTE) = prml.split_data(D, L, 2.0 / 3.0)
    mean, covariance = compute_classifier(DTR, LTR, classifier=classifier)
    return evaluate(DTE, LTE, mean, covariance, logarithmically=False)


def compute_classifier(DTR, LTR, classifier):
    data_by_classes = split_by_classes(DTR, LTR)
    mean_by_class, covariance_by_class = get_mean_and_covariance(
        data_by_classes)
    classifier_covariance = compute_classifier_covariance(covariance_by_class,
                                                          classifier, DTR, LTR)
    return mean_by_class, classifier_covariance


def compute_classifier_covariance(covariance, classifier, D, L):
    if classifier == 'mvg':
        return covariance
    elif classifier == 'naive':
        return diagonalize_covariance(covariance)
    elif classifier == 'tied_gaussian':
        covariance = prml.covariance_within(D, L)
        return [covariance for _ in range(3)]
    elif classifier == 'tied_naive':
        covariance = prml.covariance_within(D, L)
        return diagonalize_covariance([covariance for _ in range(3)])


def evaluate(DTE, LTE, mean, covariance, logarithmically):
    S = get_score_matrix(DTE, mean, covariance,
                         logarithmically=logarithmically)
    prior = np.array([[1.0 / 3], [1.0 / 3], [1.0 / 3]])
    SJoint = compute_join(S, prior, logarithmically=logarithmically)
    SMarginal = compute_marginal(SJoint, logarithmically=logarithmically)
    posterior = compute_posterior(SJoint, SMarginal,
                                  logarithmically=logarithmically)
    SPost = np.argmax(posterior, axis=0, keepdims=False)
    accuracy = np.sum(SPost == LTE) / DTE.shape[1]
    err = 1.0 - accuracy
    return {
        'Sjoint': SJoint,
        'SMarginal': SMarginal,
        'posterior': posterior,
        'SPost': SPost,
        'acc': accuracy,
        'err': err
    }


def diagonalize_covariance(covariance_by_class):
    diagonalized_covariances = []
    for covariance in covariance_by_class:
        size = covariance.shape[0]
        diagonalized_covariances.append(covariance * np.identity(size))
    return diagonalized_covariances


def compute_posterior(SJoint, SMarginal, logarithmically=False):
    if logarithmically:
        return np.exp(SJoint - SMarginal)
    return SJoint / SMarginal


def compute_marginal(SJoint, logarithmically=False):
    if logarithmically:
        return prml.vrow(scipy.special.logsumexp(SJoint, axis=0))
    return prml.vrow(SJoint.sum(0))


def get_score_matrix(samples, mean_by_class, covariance_by_class,
                     logarithmically: False):
    samples_number = samples.shape[1]
    score = np.empty((0, samples_number))
    for mean, covariance in zip(mean_by_class, covariance_by_class):
        class_score = prml.logpdf_GAU_ND(samples, mean, covariance)
        if not logarithmically:
            class_score = np.exp(class_score)
        score = np.vstack([score, class_score])
    return score


def compute_join(score, class_probability, logarithmically=False):
    if logarithmically:
        return score + np.log(class_probability)
    return class_probability * score


def load_iris():
    iris = sklearn.datasets.load_iris()
    D, L = iris['data'].T, iris['target']
    return D, L


def get_mean_and_covariance(data_by_classes):
    mean = []
    covariance = []
    for class_data in data_by_classes:
        mean.append(prml.mean(class_data))
        covariance.append(prml.covariance(class_data))
    return mean, covariance


def split_by_classes(data, labels):
    classes = []
    for _class in set(labels):
        classes.append(data[:, labels == _class])
    return classes



if __name__ == '__main__':
    main()

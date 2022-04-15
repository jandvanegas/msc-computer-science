# Lab 2
The lab consists on loading and plotting iris.csv file.
Solution was implemented using spyder for the interation and pycharm
for the software development.
Some learning about spyder are:
* Spyder allow you to set up PYTHONPATH.
* Create a module, so that you can import it from spyder.

```python
import numpy as np
import matplotlib.pyplot as plt


def load_iris():
    values, targets = load('iris.csv')
    centered_values = center_values(values)
    plot(centered_values, targets,
         ['Sepal length', 'Sepal width', 'Petal length',
          'Petal width'])
    plot(values, targets, ['Sepal length', 'Sepal width', 'Petal length',
                           'Petal width'])


def load(file_name: str):
    array = []
    targets = []
    with open(file_name, 'r') as file:
        for raw_line in file:
            if raw_line:
                line = raw_line.split(',')
                raw_values, target = line[:-1], line[-1]
                values = [float(value) for value in raw_values]
                array.append(values)
                targets.append(target.strip())
    return np.array(array).T, np.array(targets)


def simple_plot(values: np.ndarray, classes: list, feature_names: list = None):
    unique_classes = set(classes)
    fig = plt.figure()
    for feature in range(values.shape[0]):
        feature_data = values[feature]
        fig1 = fig.add_subplot(1, values.shape[0], feature + 1)
        for specific_class in unique_classes:
            class_rows = classes == specific_class
            class_values = feature_data[class_rows]
            fig1.hist(class_values, label=specific_class, density=True)
            if feature_names:
                fig1.set_title(feature_names[feature])
            fig1.legend(loc='best')
    plt.show()


def plot(values: np.ndarray, classes: np.ndarray,
         feature_names: list = None):
    unique_classes = set(classes)
    fig = plt.figure()
    feature_number = values.shape[0]
    for feature in range(feature_number):
        feature_data = values[feature]
        for second_feature in range(feature_number):
            second_feature_data = values[second_feature]
            fig1 = fig.add_subplot(feature_number, feature_number,
                                   feature * feature_number + second_feature + 1)
            for specific_class in unique_classes:
                class_rows = classes == specific_class
                if feature == second_feature:
                    class_values = feature_data[class_rows]
                    fig1.hist(class_values, label=specific_class, density=True)
                    if feature_names:
                        fig1.set_title(feature_names[feature])
                else:
                    feature_class_values = feature_data[class_rows]
                    second_class_values = second_feature_data[class_rows]
                    fig1.scatter(feature_class_values, second_class_values,
                                 label=specific_class)
                    if feature_names:
                        fig1.set_xlabel(feature_names[feature])
                        fig1.set_ylabel(feature_names[second_feature])
                fig1.legend(loc='best')
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.6,
                        hspace=0.6)
    plt.show()


def center_values(values: np.ndarray):
    return values - mcol(values.mean(1))


def mcol(vector: np.ndarray):
    return vector.reshape((vector.shape[0], 1))


def mrow(vector: np.ndarray):
    return vector.reshape((1, vector.shape[0]))


if __name__ == '__main__':
    load_iris()
```



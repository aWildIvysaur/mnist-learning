"""
Docstring for model
"""

from typing import Any
import numpy
import keras.datasets.mnist as mnist
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from numpy.typing import NDArray


def flatten_data(data: Any) -> NDArray[Any]:
    """
    Flattens 3D tuple into 2D numpy array

    :param data: list of 2d arrays of grayscale pixel values
    :type data: list[list[list[int]]]
    :return: Flattened data for ML
    :rtype: NDArray
    """
    data_array = numpy.asarray(data)
    samples, x, y = data_array.shape
    new_data = data_array.reshape((samples, x * y))

    return new_data


def train(
    data: NDArray[Any], awns: tuple[int], test_data: NDArray[Any], test_awns: tuple[int]
) -> RandomForestClassifier:
    """
    Trains and tests a model using random forest classification with 500 estimators

    :param data: Flattened training data
    :type data: NDArray
    :param awns: Awnsers for training data
    :type awns: tuple[int]
    :param test_data: Flattened testing data
    :type test_data: NDArray
    :param test_awns: Awnsers for testing data
    :type test_awns: tuple[int]
    :return: Trained model
    :rtype: RandomForestClassifier
    """
    # 500 Forest (~0.9712)
    forest_model = RandomForestClassifier(n_estimators=500, n_jobs=6, verbose=False)
    forest_model = forest_model.fit(data, awns)
    forest_output = forest_model.predict(test_data)
    print("Random Forest with n_estimators:500")
    print(accuracy_score(test_awns, forest_output))
    return forest_model


def train_mnist() -> RandomForestClassifier:
    """
    Trains and tests a model using random forest classification with 500 estimators
    Uses keras mnist data

    :return: Trained model
    :rtype: RandomForestClassifier
    """
    (train_data, train_awns), (test_data, test_awns) = mnist.load_data(path="mnist.npz")
    trained_model = train(
        flatten_data(train_data), train_awns, flatten_data(test_data), test_awns
    )
    return trained_model

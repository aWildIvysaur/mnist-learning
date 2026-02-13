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
    """flattens 3D tuple into 2D numpy array"""
    data_array = numpy.asarray(data)
    samples, x, y = data_array.shape
    new_data = data_array.reshape((samples, x * y))

    return new_data


def train(
    data: NDArray[Any], awns: tuple[int], test_data: NDArray[Any], test_awns: tuple[int]
) -> RandomForestClassifier:
    """
    Trains and tests a model using random forest classification with 500 estimators
    """
    # 500 Forest (~0.9712)
    forest_model = RandomForestClassifier(n_estimators=500, n_jobs=6, verbose=False)
    forest_model = forest_model.fit(data, awns)
    forest_output = forest_model.predict(test_data)
    print("Random Forest with n_estimators:500")
    print(accuracy_score(test_awns, forest_output))
    return forest_model


def train_mnist() -> RandomForestClassifier:
    (train_data, train_awns), (test_data, test_awns) = mnist.load_data(path="mnist.npz")
    trained_model = train(
        flatten_data(train_data), train_awns, flatten_data(test_data), test_awns
    )
    return trained_model

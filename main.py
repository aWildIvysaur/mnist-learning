"""
Docstring for main
"""

import numpy
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import keras.datasets
from typing import Any
from numpy.typing import NDArray

(train_data, train_awns), (test_data, test_awns) = keras.datasets.mnist.load_data(
    path="mnist.npz"
)


def flatten_dataset(data: tuple[int, int]) -> NDArray[Any]:
    """flattens 3D tuple into 2D numpy array"""
    data_array = numpy.asarray(data)
    samples, x, y = data_array.shape
    new_data = data_array.reshape((samples, x * y))

    return new_data


def test_mlp(
    data: NDArray[Any], awns: tuple[int], test_data: NDArray[Any], test_awns: tuple[int]
):
    mlp = MLPClassifier(solver="sgd", hidden_layer_sizes=(10,), random_state=1)
    mlp.fit(data, awns)
    mlp_output = mlp.predict(test_data)
    print("sgd")
    print(accuracy_score(test_awns, mlp_output))

    mlp = MLPClassifier(solver="lbfgs", hidden_layer_sizes=(10,), random_state=1)
    mlp.fit(data, awns)
    neural_output = mlp.predict(test_data)
    print("lbfgs")
    print(accuracy_score(test_awns, neural_output))


def test_forest(
    data: NDArray[Any], awns: tuple[int], test_data: NDArray[Any], test_awns: tuple[int]
):
    forest = RandomForestClassifier(n_estimators=500)
    forest = forest.fit(data, awns)
    forest_output = forest.predict(test_data)
    print("Random Forest with n_estimators:500")
    print(accuracy_score(test_awns, forest_output))

    forest = RandomForestClassifier(n_estimators=5000)
    forest = forest.fit(data, awns)
    forest_output = forest.predict(test_data)
    print("Random Forest with n_estimators:5000")
    print(accuracy_score(test_awns, forest_output))


# test_mlp(flatten_dataset(train_data), train_awns, flatten_dataset(test_data), test_awns)
test_forest(
    flatten_dataset(train_data), train_awns, flatten_dataset(test_data), test_awns
)

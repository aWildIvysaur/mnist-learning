"""
Docstring for model_tests
"""

from typing import Any
import numpy
import keras
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from numpy.typing import NDArray

(train_data, train_awns), (test_data, test_awns) = keras.datasets.mnist.load_data(
    path="mnist.npz"
)
print(test_awns)


def flatten_data(data: tuple[int, int]) -> NDArray[Any]:
    """flattens 3D tuple into 2D numpy array"""
    data_array = numpy.asarray(data)
    samples, x, y = data_array.shape
    new_data = data_array.reshape((samples, x * y))

    return new_data


def test_mlp(
    data: NDArray[Any], awns: tuple[int], test_data: NDArray[Any], test_awns: tuple[int]
):
    """
    Trains and tests 2 models using MLP classification with SGD and LBFGS solvers
    """
    # SGD MLP (0.3376)
    mlp = MLPClassifier(
        solver="sgd", hidden_layer_sizes=(10,), random_state=1, verbose=True
    )
    mlp.fit(data, awns)
    mlp_output = mlp.predict(test_data)
    print("sgd")
    print(accuracy_score(test_awns, mlp_output))

    # LBFGS MLP
    mlp = MLPClassifier(
        solver="lbfgs", hidden_layer_sizes=(10,), random_state=1, verbose=True
    )
    mlp.fit(data, awns)
    neural_output = mlp.predict(test_data)
    print("lbfgs")
    print(accuracy_score(test_awns, neural_output))


def test_forest(
    data: NDArray[Any], awns: tuple[int], test_data: NDArray[Any], test_awns: tuple[int]
):
    """
    Trains and tests 2 models using random forest classification with 500 and 5000 estimators
    """
    # 500 Forest (0.9712)
    forest = RandomForestClassifier(n_estimators=500, n_jobs=6, verbose=True)
    forest = forest.fit(data, awns)
    forest_output = forest.predict(test_data)
    print("Random Forest with n_estimators:500")
    print(accuracy_score(test_awns, forest_output))

    # 5000 Forest (0.972)
    forest = RandomForestClassifier(n_estimators=5000, n_jobs=6, verbose=True)
    forest = forest.fit(data, awns)
    forest_output = forest.predict(test_data)
    print("Random Forest with n_estimators:5000")
    print(accuracy_score(test_awns, forest_output))


# test_mlp(flatten_data(train_data), train_awns, flatten_data(test_data), test_awns)
# test_forest(flatten_data(train_data), train_awns, flatten_data(test_data), test_awns)

import json
import numpy as np
import os


def load_in_data():
    """
    load data from "A_group.json" and "B_group.json"
    :return: X: numpy.array [n x 2], y: numpy.array [n x 1]
    """
    # load data from json
    script_path = os.path.realpath(__file__)
    script_path = os.path.realpath(
        os.path.join(*os.path.split(script_path)[:-1]))
    os.chdir(script_path)
    A_group_path = os.path.join("..", "data", "A_group.json")
    B_group_path = os.path.join("..", "data", "B_group.json")
    with open(A_group_path) as f:
        GroupA = json.load(f)

    with open(B_group_path) as f:
        GroupB = json.load(f)

    # reformat into sklearn format
    num_GroupA = len(GroupA['x'])
    num_GroupB = len(GroupB['x'])

    X = []
    y = []

    for i in range(num_GroupA):
        X.append([GroupA['x'][i], GroupA['y'][i]])
        y.append(-1)

    for i in range(num_GroupB):
        X.append([GroupB['x'][i], GroupB['y'][i]])
        y.append(1)

    X = np.array(X, dtype=np.float)
    y = np.array(y, dtype=np.float)

    return X, y

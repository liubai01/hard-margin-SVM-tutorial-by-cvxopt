#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : visualization.py
# @Author: Yin-tao Xu
# @Date  : 18-9-10
# @Desc  : visualization section
from matplotlib.colors import ListedColormap
import numpy as np


def plot_example_1(plt):
    """
        visualize the optimization problem in example 01
    :param plt: handle for pyplot in matplotlib
    :return:
    """
    x = np.linspace(-4, 8, 1000)
    x_ = np.linspace(1.25, 8, 1000)
    y_1 = x * x * -0.5 + 3

    y_1_ = x_ * x_ * -0.5 + 3
    y_2_ = np.ones(x_.shape) * -4

    plt.figure(figsize=(5, 6), dpi=96)
    plt.xlim([-3, 4])
    plt.ylim([-3, 4])

    plt.plot(x, y_1, label=r"$-\frac{1}{2}x^2+3$")
    plt.axvline(1.25, color='orange')
    plt.legend(loc='best')

    x_opt = 1.25
    y_opt = x_opt * x_opt * -0.5 + 3
    plt.scatter([x_opt], [y_opt], c="r")
    plt.axhline(y_opt, linestyle=":", linewidth=0.8, color="grey")
    plt.fill_between(x_, y_1_, y_2_, color='blue', alpha=0.25)
    plt.grid()
    plt.show()


def plot_Xy(X, y, plt):
    # hyperparameter for boardry
    x_min = 0
    x_max = 10
    y_min = 0
    y_max = 10
    step = 0.05

    # Create color maps
    cmap_bold = ListedColormap(['#FF0000', '#003300'])

    plt.figure(figsize=(8, 5), dpi=96)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.xlim([x_min, x_max])
    plt.ylim([y_min, y_max])
    plt.show()


def plot_classifer(model, X, y, plt):
    """
    visualize the descision boundary of the hard-margin SVM classfier
    :param model: SVM object defined in Jupyter notebook
    :param X: 2-d numpy array with shape (n, dim), a designed matrix
    :param y: 1-d numpy array with shape (n,), label matrix with notation +1,-1
    :param plt: handle for pyplot in matplotlib
    :return: None
    """
    # hyperparameter for boardry
    x_min = 0
    x_max = 10
    y_min = 0
    y_max = 10
    step = 0.05

    xx, yy = np.meshgrid(np.arange(x_min, x_max, step),
                         np.arange(y_min, y_max, step)
                         )
    z = model.predict(np.c_[xx.ravel(), yy.ravel()])

    # Create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
    cmap_bold = ListedColormap(['#FF0000', '#003300'])

    z = z.reshape(xx.shape)

    # derieve support vectors
    X_sv = X[model.sp_v_i]

    plt.figure(figsize=(8, 5), dpi=96)
    plt.pcolormesh(xx, yy, z, cmap=cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.scatter(X_sv[:, 0], X_sv[:, 1], s=200,
                c="", edgecolors="b", marker="o", label="support vector")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_problem_1(plt)

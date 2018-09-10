# hard-margin-SVM-tutorial-by-cvxopt
Author: Yin-tao Xu | Date: 2018/9/10
## Introduction

This repository is a Jupyter notebook interactive guidance for setting up a hard-margin SVM binary classifer by cvxopt. The very beginning idea sources from offering a case study for my blog: [author's CSDN blog(Chinese)](https://blog.csdn.net/liubai01/article/details/82017964).

![screenshot of the jupyter notebook](https://github.com/liubai01/hard-margin-SVM-tutorial-by-cvxopt/blob/master/imgs/svm-hard.png)

 [Hard-Margin SVM](https://en.wikipedia.org/wiki/Support_vector_machine#Hard-margin) can be transformed into a standard [QP problem](https://en.wikipedia.org/wiki/Quadratic_programming). For beginners or researchers focusing on application, it is challenging to implement very detailed numerical optimization method. Rely on magic boxes in cvxopt package, you are able to derive the solution with only one command! 

## Feature

- Well-designed visualization of the decision boundary!
- A quick start to get familiar with cvxopt.

## Prerequisite

1. Get familiar with the basic modeling of the hard-margin SVM.
2. Get familiar with the idea of how to transforming into a QP-Problem
3. Have cvxopt installed. [Install insturction](http://cvxopt.org/install/)

4. Python 3(Basic Concept of function, import, OOP, etc.)

6. [Numpy](http://www.numpy.org/),[Jupyter Notebook](http://jupyter.org/), matplotlib, etc,  [Anaconda](https://www.anaconda.com/download/) is a one-stage solution instead of manually installing these frequently used 3-rd party package.

Here are two tutorials in English ([Note from standformd CS229](http://cs229.stanford.edu/notes/cs229-notes3.pdf)) and Chinese([author's CSDN blog](https://blog.csdn.net/liubai01/article/details/82017964)).

**Note**: For notes in standford, first 7 pages will provide you with enough background knowledge about SVM(before lagrange duality). 

## Quick start

1. Open terminal at target directory(anywhere you want to start this interactive tutorial)
2. follow these steps:

```shell
git clone https://github.com/liubai01/hard-margin-SVM-tutorial-by-cvxopt.git
cd hard-margin-SVM-tutorial-by-cvxopt/
jupyter notebook
```

Finally, open your browser to connect your Jupyter session. Open `case_study_01.ipynb` directly.


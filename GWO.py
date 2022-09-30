#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 12:26
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : GWO.py
# @Statement : The grey wolf optimizer
# @Reference : Mirjalili S, Mirjalili S M, Lewis A. Grey wolf optimizer[J]. Advances in Engineering Software, 2014, 69: 46-61.
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of reservoir
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def boundary_check(x, lb, ub, dim):
    """
    Check the boundary
    :param x: a candidate solution
    :param lb: lower bound
    :param ub: upper bound
    :param dim: dimension
    :return:
    """
    for i in range(dim):
        if x[i] < lb[i]:
            x[i] = lb[i]
        elif x[i] > ub[i]:
            x[i] = ub[i]
    return x


def main(pop, lb, ub, iter):
    # Step 1. Initialization
    dim = len(ub)  # dimension
    pos = []
    score = []
    iter_best = []  # the best ever value of each iteration
    for _ in range(pop):
        temp_pos = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        temp_score = obj(temp_pos)
        pos.append(temp_pos)
        score.append(temp_score)
    sorted_score = sorted(score)
    alpha_score = sorted_score[0]
    alpha_pos = pos[score.index(alpha_score)]
    beta_score = sorted_score[1]
    beta_pos = pos[score.index(beta_score)]
    delta_score = sorted_score[2]
    delta_pos = pos[score.index(delta_score)]
    iter_best.append(alpha_score)

    # Step 2. The main loop
    for t in range(iter):
        a = 2 - 2 * t / (iter + 1)
        for i in range(pop):
            for j in range(dim):
                # Calculate the distance between alpha
                r1 = random.random()
                r2 = random.random()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * alpha_pos[j] - pos[i][j])
                X1 = alpha_pos[j] - A1 * D_alpha

                # Calculate the distance between beta
                r1 = random.random()
                r2 = random.random()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_alpha = abs(C2 * beta_pos[j] - pos[i][j])
                X2 = beta_pos[j] - A2 * D_alpha

                # Calculate the distance between delta
                r1 = random.random()
                r2 = random.random()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_alpha = abs(C3 * delta_pos[j] - pos[i][j])
                X3 = delta_pos[j] - A3 * D_alpha

                pos[i][j] = (X1 + X2 + X3) / 3

            # Check the boundary
            pos[i] = boundary_check(pos[i], lb, ub, dim)

        # Calculate the score
        for i in range(pop):
            score[i] = obj(pos[i])
            if score[i] < alpha_score:
                alpha_score = score[i]
                alpha_pos = pos[i]
            elif score[i] < beta_score:
                beta_score = score[i]
                beta_pos = pos[i]
            elif score[i] < delta_score:
                delta_score = score[i]
                delta_pos = pos[i]

        iter_best.append(alpha_score)

    # Step 3. Sort the results
    x = [i for i in range(iter + 1)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.ticklabel_format(style='sci', scilimits=(0, 0))
    plt.xlabel('Iteration number')
    plt.ylabel('So-far best value')
    plt.show()

    return {'best solution': alpha_pos, 'best score': alpha_score}


if __name__ == '__main__':
    pop = 200
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    iter = 100
    print(main(pop, lb, ub, iter))

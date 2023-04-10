import math


def main(vec_x, vec_z, vec_y):
    res = 0
    for i in range(len(vec_x)):
        res += math.fabs(7 * vec_y[i] ** 3
                         - vec_x[len(vec_x) - i - 1]
                         - vec_z[len(vec_x) - i - 1] ** 2)
    return 54 * res


if __name__ == "__main__":
    print("{:,.2f}".format(main([-0.7, -0.63, -0.89, 0.42, 0.67, 0.97],
                                [0.25, -0.14, -0.86, -0.41, 0.27, 0.25],
                                [-0.67, -0.07, 0.77, 0.23, 0.31, 1.0])))

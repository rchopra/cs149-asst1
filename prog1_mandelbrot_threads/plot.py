import matplotlib.pyplot as plt

if __name__ == "__main__":
    threads = list(range(2,9))
    view1 = [1.93, 1.61, 2.35, 2.38, 3.09, 3.19, 3.63]
    view2 = [1.63, 2.05, 2.39, 2.64, 2.94, 3.32, 3.62]
    interleaved1 = [1.93, 2.80, 3.72, 4.31, 4.85, 5.41, 5.86]
    interleaved2 = [1.93, 2.79, 3.72, 4.08, 4.61, 5.17, 5.82]


    plt.plot(threads, view1, label="View 1")
    plt.plot(threads, view2, label="View 2")
    plt.legend()
    plt.title("Speedup with Spatial Decomposition")
    plt.show()

    plt.clf()

    plt.plot(threads, interleaved1, label="View 1")
    plt.plot(threads, interleaved2, label="View 2")
    plt.legend()
    plt.title("Speedup with Interleaved Decomposition")
    plt.show()

import time
import numpy as np
import ray


num_cpus = 7

def f1():
    time.sleep(1)


@ray.remote
def f2():
    time.sleep(1)


def test_multiprocessing():
    # ray initialize
    ray.init()

    # The following takes {num_cpus} seconds.
    start = time.time()
    [f1() for _ in range(num_cpus)]
    end = time.time()
    print(f"f1: {end - start}")

    # The following takes one second (assuming the system has {num_cpus} CPUs).
    start = time.time()
    ray.get([f2.remote() for _ in range(num_cpus)])
    end = time.time()
    print(f"f2: {end - start}")


if __name__ == "__main__":
    values_put = np.random.normal(size=1000)

    test_multiprocessing()

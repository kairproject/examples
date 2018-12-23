"""
Ray tutorial example.
https://ray.readthedocs.io/en/latest/tutorial.html
"""

import time
import ray


def f1():
    time.sleep(1)


@ray.remote
def f2():
    time.sleep(1)


def test_multiprocessing(num_cpus, ip_port):
    # ray initialize
    ray.init(ip_port)

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
    num_cpus = 20
    ip_port = "192.168.0.104:8787"

    test_multiprocessing(num_cpus, ip_port)

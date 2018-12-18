import time

import numpy as np
import ray
import gym


@ray.remote
class RayWorker(object):

    def __init__(self):
        self.w_policy = np.zeros([100, 100])
        self.env = gym.make('SpaceInvaders-v0')

    def rollout(self):
        obs = self.env.reset()
        steps = 0
        total_reward = 0

        while True:
            obs, reward, done, _ = self.env.step(self.env.action_space.sample())
            steps += 1
            total_reward += reward
            if done:
                break
        return total_reward, steps

    def do_rollout(self, w_policy, num_rollouts):
        rollout_rewards, rollout_weights=  [], []

        for i in range(num_rollouts):
            reward, r_steps = self.rollout()
            rollout_rewards.append(reward)

            # weight update step
            delta = np.random.rand(w_policy.shape[0], w_policy.shape[1])
            self.w_policy += delta

            rollout_rewards.append(reward)
            rollout_weights.append(self.w_policy)
        return rollout_rewards, rollout_weights

    def get_weights(self):
        return self.w_policy


class NonRayWorker(object):

    def __init__(self):
        self.w_policy = np.zeros([100, 100])
        self.env = gym.make('SpaceInvaders-v0')

    def rollout(self):
        obs = self.env.reset()
        steps = 0
        total_reward = 0

        while True:
            obs, reward, done, _ = self.env.step(self.env.action_space.sample())
            steps += 1
            total_reward += reward
            if done:
                break
        return total_reward, steps

    def do_rollout(self, w_policy, num_rollouts):
        rollout_rewards, rollout_weights = [], []

        for i in range(num_rollouts):
            reward, r_steps = self.rollout()
            rollout_rewards.append(reward)

            # weight update step
            delta = np.random.rand(w_policy.shape[0], w_policy.shape[1])
            self.w_policy += delta

            rollout_rewards.append(reward)
            rollout_weights.append(self.w_policy)
        return rollout_rewards, rollout_weights

    def get_weights(self):
        return self.w_policy


def test_multi_workers():
    # https://github.com/ray-project/ray/blob/master/doc/source/plasma-object-store.rst
    ray.init(huge_pages=True, plasma_directory="/mnt/hugepages")

    num_cpus = 7
    num_workers = num_cpus
    num_rollouts = 20
    init_w_policy = np.zeros([100, 100])

    # 1. parallel workers
    workers = [RayWorker.remote() for i in range(num_workers)]
    start = time.time()
    rollouts = [worker.do_rollout.remote(init_w_policy, num_rollouts) for
        worker in workers]
    results = ray.get(rollouts)
    end = time.time()
    print(f"Parallel workers took {end - start}s")

    # 2. non-parallel workers
    workers = [NonRayWorker() for i in range(num_workers)]
    start = time.time()
    rollouts = [worker.do_rollout(init_w_policy, num_rollouts) for
        worker in workers]
    end = time.time()
    print(f"Non-parallel workers took {end - start}s")


if __name__ == "__main__":
    test_multi_workers()

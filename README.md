# Tutorial examples

## [Ray](https://github.com/ray-project/ray)
- Install requirements

```
pip install ray 
git clone https://github.com/openai/gym.git
cd gym
pip install -e '.[atari]'
```

- Example 1: Easy multiprocessing test.
```
python ray_example_npy.py
```

- Example 2: RL worker-like multiprocessing test.
```
python ray_example_worker.py
```

## [Ray](https://github.com/ray-project/ray)
- Install requirements

```
pip install ray 
git clone https://github.com/openai/gym.git
cd gym
pip install -e '.[atari]'
```

- Setup cluster using ray
```
# PC1 setting (master)
ssh kair@192.168.0.25
>> Enter password
cd examples/
ray start --head --redis-port=6379

# PC2 setting 
ssh [pc2]@[pc2_ip_address]
>> Enter password
cd examples/
ray start --redis-address="192.168.0.25:6379"
```

- Example 1: Easy multiprocessing test
```
python ray_example_time.py
```

- Example 2: RL worker-like multiprocessing test
```
python ray_example_worker.py
```

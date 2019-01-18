# Mujoco Installation 

## Get License - Get license from [here](https://www.roboti.us/license.html)
- Download `mjkey.txt` from email.
- `cd ./mjkey.txt ~/.mujoco/mjkey.txt`

## Gym Installation
- `git clone https://github.com/openai/gym`
- `cd gym`
- `sudo apt-get install -y python-pyglet python3-opengl zlib1g-dev libjpeg-dev patchelf \
        cmake swig libboost-all-dev libsdl2-dev libosmesa6-dev xvfb ffmpeg`
- `pip install -e .`

## Python2
- Download [`mjpro131_linux.zip`](https://www.roboti.us/download/mjpro131_linux.zip) and extract
- `mv ./mjpro131 ~/.mujoco/`
- `pip install mujoco-py==0.5`

## Python3
- Download [`mjpro150_linux.zip`](https://www.roboti.us/download/mjpro150_linux.zip) and extract
- `mv ./mjpro150 ~/.mujoco/`
- `pip install mujoco-py`

## Issues
- Python3 [`GLEW initialization error`](https://github.com/openai/mujoco-py/pull/145) 
- Python2 [`module 'mujoco_py' has no attribute 'load_model_from_path'`](https://github.com/openai/mujoco-py/issues/261)
- [Compiler Error](https://github.com/openai/mujoco-py/issues/180)

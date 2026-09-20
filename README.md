# LunarLanderTools

Because we are running LunarLander-v2, we need to be careful about the versions of libraries that we are installing. I think we logged most of the installs

> $ conda create --name LunarLanderv2 python=3.8
> $ conda activate LunarLanderv2
> $ conda install -c conda-forge swig -y
> $ numpy==1.24.4
> $ matplotlib==3.1.2
> $ pip install Pillow==9.5.0
> $ pip install opencv-python
> $ pip install imageio[ffmpeg]


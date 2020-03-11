# Prepare lib to working with kinnect

In ubuntu 18.04 LTS :

Add in the sources repository:

```
deb http://cz.archive.ubuntu.com/ubuntu bionic main universe
apt update
```

Install the next packages

```

apt-get install build-essential
apt-get install git-core cmake freeglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev

```
Dowload the libfreebect_0.5.3 from: 

1. http://archive.ubuntu.com/ubuntu/pool/universe/libf/libfreenect/libfreenect_0.5.3.orig.tar.gz
2. This repository

Compile and install:

```
mkdir build
cd build
cmake ..
make -j4
sudo make install
```

Compile to wrapers in python
install cython

```
sudo python -m pip install cython
```

Compile

```
mkdir build
cd build
cmake .. -DBUILD_PYTHON=ON
make -j4
sudo make install
```
update path
```
sudo ldconfig
```



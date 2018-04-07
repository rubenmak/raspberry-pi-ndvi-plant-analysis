# raspberry-pi-ndvi-plant-analysis
Python code for analysis plants using ndvi with Raspberry Pi NoIR camera

This code is a modification of https://github.com/robintw/RPiNDVI.
It's modified such that it doesn't show black parts where NDVI is highest in the image.
Also, the visualisation is modified to my taste and added camera rotation as optional argument.

##Hardware
Raspberry Pi attached to a screen or VNC (I used 3B and Raspbian with desktop)
Raspberry Pi NoIR camera with the filter attached in some way
(more info: https://www.raspberrypi.org/blog/whats-that-blue-thing-doing-here/)

## install dependencies
Assuming you already have pip and picamera preinstalled (like with Raspboan with desktop). If not:
```
sudo apt-get update
sudo apt-get install python-picamera python-pip
```

Install opencv using:

```
sudo apt-get install build-essential gfortran libatlas-base-dev python-pip python-dev
sudo pip install --upgrade pip
sudo pip install numpy
sudo pip install scipy
sudo apt-get install python-opencv
```

Pip was throwing me TypeErrors on Raspian, so I had to reinstall it:

```
apt-get remove python-pip python3-pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py
```

## running
`python ndvi.py`

You might need to set the camera rotation based on how you camera is positioned, e.g.:

`python ndvi.py 90`


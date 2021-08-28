# Hand Tracking Demo

[![Hand Tracking Thumbnail](https://img.youtube.com/vi/LAQ-O3kCK8c/0.jpg)](https://www.youtube.com/watch?v=LAQ-O3kCK8c)

## Setup
* Use a virtual environment, python3.
  https://docs.python.org/3/library/venv.html

``` bash
# Run the demo, type in command line
python MyNewGameHandTraking.py
```

#### Hand Gesture as a Control

Use hand gestures to control the volume of your
computer in this case, this demo could be
easily modified to control other settings in
your computer.

###### Setup
* Activate your virtual environment for python3.

* Install [pyalsaaudio](https://github.com/larsimmisch/pyalsaaudio)

``` bash
# Run the demo, type in command line
python VolumeHandControl.py
```

* Note: This specific demo currently has only been
tested on ubuntu, porting this demo to windows
should be really straightforward instead of using
[pyalsaaudio](https://github.com/larsimmisch/pyalsaaudio) use [pycaw](https://github.com/AndreMiras/pycaw).

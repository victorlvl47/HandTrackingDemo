# Hand Tracking Demo

Note: Click the images to go to the video.

#### Hand Tracking

[![Hand Tracking Thumbnail](https://img.youtube.com/vi/LAQ-O3kCK8c/0.jpg)](https://www.youtube.com/watch?v=LAQ-O3kCK8c)

###### Setup
* Use a virtual environment, python3.
  https://docs.python.org/3/library/venv.html

``` bash
# Run the demo, type in command line
python MyNewGameHandTraking.py
```

#### Hand Gesture as a Control

[![Hand Gesture Thumbnail](https://img.youtube.com/vi/P3x2iqfM-tU/0.jpg)](https://www.youtube.com/watch?v=P3x2iqfM-tU)

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

#### CV Paint Demo

A MS Paint like application but you use your hand
as the cursor to paint and select colors and tools.

###### Setup
* Activate your [virtual environment](https://docs.python.org/3/library/venv.html) for python3.

``` bash
# Run the demo, type in command line
python CV_Paint.py
```

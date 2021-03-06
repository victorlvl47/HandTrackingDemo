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

[![Hand Tracking Thumbnail](https://img.youtube.com/vi/0-b7QuKvly4/0.jpg)](https://www.youtube.com/watch?v=0-b7QuKvly4)

A MS Paint like application but you use your hand
as the cursor to paint and select colors and tools.

###### Instructions
* Open your hand to select colors and tools, close
your hand except for the index finger to draw.

###### Setup
* Activate your [virtual environment](https://docs.python.org/3/library/venv.html) for python3.


``` bash
# Run the demo, type in command line
python CV_Paint.py
```

#### Finger Counting Demo

[![Finger Counting Thumbnail](https://img.youtube.com/vi/XuXzFIjtXOI/0.jpg)](https://www.youtube.com/watch?v=XuXzFIjtXOI)

A hand tracking demo that displays how many fingers are up in the image.

###### Setup
* Activate your [virtual environment](https://docs.python.org/3/library/venv.html) for python3.


``` bash
# Run the demo, type in command line
python FingerCounting.py
```

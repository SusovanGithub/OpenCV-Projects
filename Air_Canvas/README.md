#
**<H1 align = "center">Air Canvas</H1>**

## Description

<img align='right' height=100% width=38% src='https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/air_canvas.gif'/>

**Author** : Susovan Das

**Language** : Python  

**External Module** : [OpenCV][opencv], [MediaPipe][mediapipe]

It is a Computer Vision based project where we frist detacting the hand and it's landmarks, after that by using the landmarks we are defining some gesture and using them to draw into the Live Footage. all the [gestures](#gesture) are writen down.

## How to Download

To download this project Click this --> &nbsp; &nbsp; [<img src="https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/.download_icon.png" width="20" height="20"/>][DownGit]

## Requirements

This project requir some external modules.
* OpenCV
* MideaPipe

So use the package manager [pip](https://pypi.org/project/pip/) to install this packages.

```bash
pip install opencv-python
pip install mediapipe
```

## How to Use

You can run this by simply double clicking the _air_canvas.py_.  
Or you can use the Command Prompt/Terminal and go to the location of the _object_tracking.py_ and type `python air_canvas.py`.  

For exit press _ESC_ button.

### Gesture

There are total 4 Gestures,-

|**Selction Mode**|**Draw Mode**|**Hover Mode**|**Clear Mode**|
|---|---|---|---|
|![Selection Mode][selectionmode]|![Draw Mode][drawmode]|![Hover Mode][hovermode]|![Clear Mode][clearmode]|

<!--Inner Links-->
[opencv]: https://opencv.org/

[mediapipe]: https://mediapipe.dev/

[DownGit]: https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/SusovanGithub/OpenCV-Projects/tree/master/Air_Canvas

[selectionmode]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/Air_Canvas-selctionmode.png

[drawmode]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/Air_Canvas-drawmode.png

[hovermode]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/Air_Canvas-hovermode.png

[clearmode]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/Air_Canvas-clearmode.png

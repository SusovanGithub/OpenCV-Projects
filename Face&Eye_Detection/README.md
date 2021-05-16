#
**<H1 align = "center">Face & Eye Detection using Haar Classifier</H1>**

## Description

**Author** : Susovan Das

**Language** : Python  

**External Module** : [OpenCV][opencv]

|_face_detection.py_|_eye_detection.py_|
|---|---|
|![Face Detection][fdGif]|![Eye Detection][edGif]|

This Project helps to detect the faces and eyes from frame. We are using _OpenCV's_ built in class [_CascadeClassifier_][cascadeclassifier] where we loading a pretrained _.xml_ **Haar** classifier file which is provided by the _OpenCV_ itself. _OpenCV_ provides many other pretrained Haar classifiers as -  
* haarcascade_frontalface_default.xml
* haarcascade_smile.xml
* haarcascade_eye.xml
* haarcascade_upperbody.xml  
etc, to check all search the location using 'cv2.haarcascades' into the python shell.

## How to Download

To download this project Click this --> &nbsp; &nbsp; [<img src="https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/.download_icon.png" width="20" height="20"/>][DownGit]

## Requirements

This project requir a external module called _opencv-python_. So use the package manager [pip](https://pypi.org/project/pip/) to install the _OpenCV_ package. 

```bash
pip install opencv-python
```

## How to Use

You can run this by simply double clicking the _.py_ files.  
Or you can use the Command Prompt/Terminal and `python 'Files Name.py'`.  
To exit press _ESC_ button.

<!--Inner Links-->
[opencv]: https://opencv.org/

[cascadeclassifier]: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

[fdGif]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/face_detection.gif

[edGif]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/eye_detection.gif

[DownGit]: https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/SusovanGithub/OpenCV-Projects/tree/master/Face_Detection

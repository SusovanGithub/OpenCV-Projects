#
**<H1 align = "center">Object Detection</H1>**

## Description

**Author** : Susovan Das

**Language** : Python  

**External Module** : OpenCV

|_face_detection.py_|_eye_detection.py_|
|---|---|
|![Face Detection][fdGif]|![Eye Detection][edGif]|

This Project helps to detect some object from a frame or images. Here we are detecting the faces and eyes. we are using _OpenCV's_ built in class [_CascadeClassifier_](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) where we loading a pretrained _.xml_ **Haar** classifier file which is provided by the _OpenCV_ itself. _OpenCV_ provides many other pretrained classifiers as -  
* haarcascade_frontalface_default.xml
* haarcascade_smile.xml
* haarcascade_eye.xml
* haarcascade_upperbody.xml  
etc, to check all search the location using 'cv2.haarcascades'.

## How to Download

To download this project Click this --> &nbsp; &nbsp; [<img src="https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/.download_icon.png" width="20" height="20"/>][DownGit]

## Requirements

This project requir a external module called opencv-contrib-python. So use the package manager [pip](https://pypi.org/project/pip/) to install the OpenCV package. 

```bash
pip install opencv-python
```

## Usage

You can run this by simply double clicking the _.py_ files.  
Or you can use the Command Prompt/Terminal and `python 'Files Name.py'`.  
To exit press _ESC_ button.

<!--Inner Links-->
[fdGif]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/face_detection.gif
[edGif]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/eye_detection.gif
[DownGit]: https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/SusovanGithub/OpenCV-Projects/tree/master/Face_Detection

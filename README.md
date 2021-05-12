#
**<H1 align = "center">Color Detection</H1>**

## Description

**Author** : Susovan Das

**Language** : Python  

**External Module** : OpenCV, Numpy, Pandas

### **Color Detection**

This is a basic and small project of Computer Vision. In this we are detecting the color for a pecific location of the frame and finding that color name in the real world. To get the colors name there was a _.csv_ file named '_color_name.csv_' which content the name of the colors with ther R,G,B valus.  

|_color_detection_image.py_|_color_detection_webcam.py_|
|---|---|
|![Color Detection from a Image][imgGif]|![Color Detection using WebCam][webcamGif]|

### **Color Detection in HSV Color Scale**

![Color Detection in HSV Color Scale][imgHSVGif]

_detectColorHSV.py_ helps to detect the color in HSV scale, for that we are using some track pad to change the value for the HSV components and see how does this thing detect the colors.

## How to Download

To download this project Click this --> &nbsp; &nbsp; [<img src="https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/.download_icon.png" width="20" height="20"/>][DownGit]

## Requirements

This project requir some external modules.
* OpenCV
* Numpy
* Pandas

So use the package manager [pip](https://pypi.org/project/pip/) to install those package.

```bash
pip install opencv-python
pip install numpy
pip install pandas
```

## Usage

You can run this by simply double clicking the _.py_ files.  
Or you can use the Command Prompt/Terminal and `python 'Files Name.py'`.  

* After that a window will be popped up named **Color Detection** now using mouse select the point for which you want to know the color name. for _color_detection_image.py_ at first you have to enter the image 'path'.
* In _detectColorHSV.py_ window name is **Color Detection in HSV Space** and you have to use the Track Pad to change the HSV scale values.

To exit press _ESC_ button.

<!--Inner Links-->
[imgGif]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/color_detection_image.gif
[webcamGif]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/color_detection_webcam.gif
[imgHSVGif]: https://github.com/SusovanGithub/OpenCV-Projects/blob/master/Assets/detectColorHSV.gif
[DownGit]: https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/SusovanGithub/OpenCV-Projects/tree/master/Color_Detection

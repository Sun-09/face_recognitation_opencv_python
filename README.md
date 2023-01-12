# SIMPLE FACE-RECOGNITION CODE BY OPENCV & CONNECTION TO MQTT

![maxresdefault](https://user-images.githubusercontent.com/104966547/211987319-6a3f63c3-b098-458e-8d0c-b54bb9f28c20.jpg)


Hello all Coders Welcome to my Project. Here I make a Project where we run a opencv python code. The Code takes the video from your device's camera
and it compares the faces of the video and a image(which we have to given previously.This image will be Admin's Image). If the both faces are match,then the
1 value will publish to the mqtt broker with the help of **client.publish(.....)** commands in the opencv topic. The ESP32 is coded( you can see it in the
https://github.com/Sun-09/face_recognitation_opencv_python/blob/master/opencv-via-MQTT-data-transfer/opencv-via-MQTT-data-transfer.ino)  so that it subscribed 
to same topic and same mqtt client. So when the python will publish 1 value it will go to the ESP32 and whenever ESP32 will get 1 value it will turn LED..



Languages used by - Python, C/C++

# IDLE Used :- 

vsCode(Download at - https://code.visualstudio.com/Download)

Ardiuno IDLE(Download at - https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE)


# Libraries used -


a.opencv-Python(pip install opencv-python)

b.dlib(pip install dlib==19.18.00)


c.cmake(pip install cmake)

d.mqtt.client(pip install mqtt.client)

e. PubSubClient.h

f. Wifi.h


# N.B:- 

**If you find any problem installing dlib library follow the steps-**

 1. Go to the Link :- https://github.com/datamagic2020/Install-dlib 
 
 
 
 2. Download your Required .whl file according to Python Version
 
 3. Go To VsCode Terminal
 
 4. Enter the command - pip install "dlib-19.22.99-cp39-cp39-win_amd64.whl" in the terminal and press Enter.
 
 5. dlib library will be successfully installed


# TIP:-


you can copy the code of mqtt.py and paste it inside the if statement of main.py and do some **Internet of Things** projects


# ACKNOWLEDGEMENT:-

YouTube

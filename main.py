import cv2
import numpy as np
import face_recognition
import paho.mqtt.client as mqtt





capture = cv2.VideoCapture(0)




imgElon = face_recognition.load_image_file('images/OIP.jpeg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('images/test.jpeg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

imgbill = face_recognition.load_image_file('images/bill_gates_test.jpeg')
imgbill = cv2.cvtColor(imgbill,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]

cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,255,255),2)

faceLoctest = face_recognition.face_locations(imgTest)[0]
encodetest = face_recognition.face_encodings(imgTest)[0]

cv2.rectangle(imgTest,(faceLoctest[3],faceLoctest[0]),(faceLoctest[1],faceLoctest[2]),(0,255,0),2)

faceLocbill = face_recognition.face_locations(imgbill)[0]
encodeBill = face_recognition.face_encodings(imgbill)[0]

cv2.rectangle(imgbill,(faceLocbill[3],faceLocbill[0]),(faceLocbill[1],faceLocbill[2]),(255,255,0),2)
while True:
    _ , frame = capture.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    

    frameencoding = face_recognition.face_encodings(frame)[0]

    results = face_recognition.compare_faces([encodeElon],frameencoding)
    print(results)
    if results==[True]:
        
        import paho.mqtt.client as mqtt
        import json

        # This is the Subscriber
        def on_connect(client, userdata, flags, rc):
           print("Connected with result code " + str(rc))
           client.publish("opencv", 1)




        client = mqtt.Client()



        client.connect("test.mosquitto.org", 1883, 60)

        client.on_connect = on_connect
        client.loop_forever()
        
        
        
            
    else:
            print(0)

    
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()
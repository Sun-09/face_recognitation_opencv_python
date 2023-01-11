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
exit()
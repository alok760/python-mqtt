import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    temperature = 1
    (rc, mid) = client.publish("test760/key1", str(temperature), qos=1)
    (rc, mid) = client.publish("test760/key2", str(temperature), qos=1)
    time.sleep(2)

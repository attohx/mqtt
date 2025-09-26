import paho.mqtt.client as mqtt

from gpiozero import LED
from time import sleep



def on_connect(client, userdata, flags, rc):
    print ("Connected with result code"+str(rc))

    client.subscribe("glblcd/group5")


def on_message(client, userdata, msg):
    print(msg.topic+"\n" + msg.payload.decode("utf-8") + "\n")
    
    led = LED(17)


    if msg.payload.decode("utf-8") == "ON":
        led.on()
        print("LED ON")
    elif msg.payload.decode("utf-8") == "OFF":
        led.off()
        print("LED OFF")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("197.255.72.230", 1883, 60)

client.loop_forever()



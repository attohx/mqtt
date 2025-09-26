import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print ("Connected to broker")
        global Connected # Use global variable
        Connected = True # Signal connection

    else:
        print("Connection failed")

Connected = False # global variable for the state of the connection

client = mqtt.Client() # create new instance
client.on_connect = on_connect # attach function to callback
client.connect("197.255.72.230", 1883, 60) # set username and password
client.loop_start() # start the loop

while Connected != True: # Wait for connection
    time.sleep(0.1)

try:
    while True:
        message = input("ON") # Publish message to "glblcd/chat" topic
        client.publish("glblcd/group5", message) # wait
    
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()


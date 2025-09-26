import paho.mqtt.client as mqtt
from gpiozero import Button
from signal import pause
import time

button = Button(3)

Connected = False  # Global flag

def on_connect(client, userdata, flags, rc):
    global Connected
    if rc == 0:
        print("Connected to broker")
        Connected = True
    else:
        print(f"Connection failed with code {rc}")

def send_message():
    print("Button pressed, sending MQTT message...")
    client.publish("glblcd/group5", "ON")

client = mqtt.Client()
client.on_connect = on_connect

try:
    client.connect("197.255.72.230", 1883, 60)
except Exception as e:
    print(f"Could not connect to broker: {e}")
    exit(1)

client.loop_start()

# Wait for connection
start_time = time.time()
while not Connected and time.time() - start_time < 5:
    time.sleep(0.1)

if not Connected:
    print("MQTT connection timed out.")
    client.loop_stop()
    exit(1)

button.when_pressed = send_message

print("Waiting for button press. Press Ctrl+C to exit.")
try:
    pause()  
except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()
    client.loop_stop()

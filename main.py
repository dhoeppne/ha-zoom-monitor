from dotenv import load_dotenv
import os
import subprocess
import paho.mqtt.client as mqtt

load_dotenv()

mqttBroker = os.getenv("MQTT_BROKER")
username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")
topic = os.getenv("TOPIC")

client = mqtt.Client("Zoom_Meetings")
client.username_pw_set(username, password)
try:
  client.connect(mqttBroker, 1883, 60)
except:
  print("Could not connect to MQTT broker")
  exit()


p1 = subprocess.Popen(['ps', '-x'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "-E", "\-key [0-9]{9,10}"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()

output = p2.communicate()[0]

if output:
    code = output.split()[-1].decode()
    print("Meeting ID:", str(code))
    client.publish(topic, "ON")
else:
    print("Avail.")
    client.publish(topic, "OFF")
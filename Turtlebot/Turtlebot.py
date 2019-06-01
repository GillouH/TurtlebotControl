#!/usr/bin/env python3
# -*-coding:utf-8 -*

import paho.mqtt.client as mqtt_client
from sense_hat import SenseHat
import rospy
from geometry_msgs.msg import Twist


IP = "192.168.0.63" # Il faut mettre l'adresse IP du serveur MQTT
PORT = 1883
ALIVE = 45
TOPIC_MQTT = "Turtlebot1"
TOPIC_ROS = "/cmd_vel"


def map(x, lastXmin, lastXmax, newXmin, newXmax):
	if x > lastXmax:
		return newXmax
	if x < lastXmin:
		return newXmin
	return newXmin + (((x - lastXmin) * (newXmax - newXmin)) / (lastXmax - lastXmin))


def traitement(donnees):
	x = map(donnees[0], -100, 100, -0.22, 0.22)
	y = map(donnees[1], -100, 100, 2.84, -2.84)

	messageROS = Twist()
	messageROS.linear.x = x
	messageROS.angular.z = y

	clientROS.publish(messageROS)


def reception(client, userdata, message):
	msg = message.payload.decode()
	donnees = msg.split(",")

	x = float(donnees[0])
	y = float(donnees[1])
	print(str(x)+","+str(y))

	traitement((x, y))


if __name__ == "__main__":
	clientMQTT = mqtt_client.Client(client_id=TOPIC_MQTT+"Sub")
	try:
		rospy.init_node("Pub", anonymous=False)
		clientROS = rospy.Publisher(TOPIC_ROS, Twist, queue_size = 1)

		clientMQTT.on_message = reception
		clientMQTT.connect(host=IP, port=PORT, keepalive=ALIVE)
		clientMQTT.subscribe(TOPIC_MQTT)

		clientMQTT.loop_forever()
	except KeyboardInterrupt:
		pass

#!/usr/bin/env python3
# -*-coding:utf-8 -*


import paho.mqtt.client as mqtt_client
from sense_hat import SenseHat
from time import sleep


IP = "192.168.0.63" # Il faut mettre l'adresse IP du serveur MQTT
PORT = 1883
ALIVE = 45
TOPIC = "Turtlebot1"


def map(x, lastXmin, lastXmax, newXmin, newXmax):
	if x > lastXmax:
		return newXmax
	if x < lastXmin:
		return newXmin
	return newXmin + (((x - lastXmin) * (newXmax - newXmin)) / (lastXmax - lastXmin))


def recupDonneeCapteur(capteur):
	accel = capteur.get_accelerometer_raw()

	x = accel["x"]
	y = accel["y"]

	x = map(x, -1, 1, 100, -100)
	y = map(y, -1, 1, 100, -100)

	if abs(x) < 20 :
		x = 0
	if abs(y) < 20:
		y = 0

	print(x, y)
	return x, y


def envoi(donnees, client):
	msg = str(donnees[0])+","+str(donnees[1])
	r = client.publish(TOPIC, msg)
	print("\t" + ("envoyé" if r[0] == 0 else "echec"))


if __name__ == "__main__":
	clientMQTT = mqtt_client.Client(client_id=TOPIC+"Pub")
	try:
		clientMQTT.connect(host=IP, port=PORT, keepalive=ALIVE)
		sense = SenseHat()
		sense.set_imu_config(False, False, True) # magnetometre, gyroscope, accelerometer
		while True:
			x , y = recupDonneeCapteur(sense)
			envoi((x, y), clientMQTT)
			sleep(0.1)
	except KeyboardInterrupt:
		pass
	finally:
		r = clientMQTT.publish(TOPIC, "fin")
		print("\t" + ("envoyé" if r[0] == 0 else "echec"))
		clientMQTT.disconnect()

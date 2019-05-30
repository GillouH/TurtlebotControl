#!/usr/bin/env python3
# -*-coding:utf-8 -*


import paho.mqtt.client as mqtt_client
from Useful.XboxOneController import XboxOneController as Manette
from time import sleep
from copy import deepcopy


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
	x = deepcopy(capteur["SL"])["V"]
	y = deepcopy(capteur["SR"])["H"]

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
	try:
		clientMQTT = mqtt_client.Client(client_id=TOPIC+"Pub")
		print("Connexion en cours...")
		clientMQTT.connect(host=IP, port=PORT, keepalive=ALIVE)
		print("Connecté !")
		manette = Manette()
		manette.start()
		while True:
			x , y = recupDonneeCapteur(manette)
			envoi((x, y), clientMQTT)
			sleep(0.1)
	except KeyboardInterrupt:
		pass
	finally:
		clientMQTT.disconnect()

#!/bin/bash

# Mise à jour du système
sudo apt-get update
sudo apt-get upgrade

# Installation du serveur MQTT
sudo apt-get install mosquitto

# Redémarre le système
sudo reboot now


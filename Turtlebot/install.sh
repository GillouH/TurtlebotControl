#!/bin/bash

# Mise à jour du système
sudo apt-get update
sudo apt-get upgrade

# Installation de python 3 et pip3
sudo apt-get install python3
sudo apt-get install python3-pip

# Met à jour pip3
python3 -m pip install --upgrade pip

# Installation de la bibliothèque MQTT pour python3
python3 -m pip install paho_mqtt

# Redémarre le système
sudo reboot now

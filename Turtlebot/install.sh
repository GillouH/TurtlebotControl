#!/bin/bash

# Mise à jour du système
sudo apt update
sudo apt upgrade

# Installation de python 3, pip 3 et rospkg
sudo apt install python3 python3-pip rospkg

# Met à jour pip3
python3 -m pip install --upgrade pip

# Installation de la bibliothèque MQTT pour python3
python3 -m pip install paho_mqtt pyyaml rospkg

# Redémarre le système
sudo reboot now

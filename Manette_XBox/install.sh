#!/bin/bash

# Mise à jour du système
sudo apt update
sudo apt upgrade

# Installation de python 3 et pip3
sudo apt install python3 python3-pip

# Met à jour pip3
python3 -m pip install --upgrade pip

# Installation de la bibliothèque MQTT pour python3
python3 -m pip install paho_mqtt

# Installation de la bibliothèque permettant de lire les touches de la manette de XBox
python3 -m pip install inputs

# Redémarre le système
sudo reboot now

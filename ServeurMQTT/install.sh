#!/bin/bash

# Mise à jour du système
sudo apt update
sudo apt upgrade

# Installation du serveur MQTT
sudo apt install mosquitto

# Redémarre le système
sudo reboot now


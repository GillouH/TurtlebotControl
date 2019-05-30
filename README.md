# TurtlebotControl
Ensemble de programmes permettant de contrôler un robot Turtlebot (fonctionnant sur ROS) depuis divers appareils distants (manette de Xbox, IMU)

## Fonctionnement général
Ce projet s'apuuyera sur ROS, le protocole MQTT et python3.
Le Turtlebot devra mettre en route ROS afin de démarrer les rostopics qui serviront à le commander. Un autre programme se connectera à un serveur MQTT afin de recevoir les commandes venant des différent appareils et les publiera sur le topic ROS qui contrôle ses moteurs.
Les autres appareils seront connectés à des Raspberry qui récupèreront les données et les publierons en MQTT pour le Turtlbot.

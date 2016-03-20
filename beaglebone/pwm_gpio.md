PWM et GPIO
===============

### GPIO ###

[Schéma des pins](http://beagleboard.org/static/images/cape-headers-serial.png)

Les différentes étapes pour utiliser les GPIO :
* Création du gpio  
`echo numeropin > /sys/class/gpio/export`
* Choix entrée / Sortie  
`echo in > /sys/class/gpio/gpio60/direction`  
`echo out > /sys/class/gpio/gpio60/direction`
* Lecture ou Ecriture  
`cat /sys/class/gpio/gpio60/value`  
`echo 0 > /sys/class/gpio/gpio60/value`  
`echo 1 > /sys/class/gpio/gpio60/value`
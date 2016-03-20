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

### PWM ###

* Spécifier l'architecture utilisé au bone_capemgr  
`echo am33xx_pwm > /sys/devices/bone_capemgr.8/slots`

* Ajouter un PWM channel corréspond au PWM voulu par exemple P9_14  
`echo bone_pwm_(channel) > /sys/devices/bone_capemgr.8/slots`

* Configurer le PWM, name va étre de P9_14.* dans notre cas    
`echo (periode en us) > /sys/devices/ocp.3/(name)/period"`  
`echo (duty en us) > /sys/devices/ocp.3/(name)/duty"`

* Activer le PWM  
`echo 1 > sys/devices/ocp.3/(name)/run`

* Extra : Modifier la polarité :  
`/sys/devices/ocp.3/(name)/polarity`
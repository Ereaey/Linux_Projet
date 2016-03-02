Protocole sérial
===========

### Action, 1 octet ### 
* 0x01 : Modification Angle Moteur
* 0x02 : Allumer eteindre LED
* 0X03 : Lancer forme

### Angles moteurs, 2 octet ###
* Angle servo 1 en hexa
* Angle servo 2 en hexa

### LED, 1 octet ###
* 0x01 Allumer
* 0x00 Eteindre

### Lancer forme, 1 octet ###
* id_forme en hexa
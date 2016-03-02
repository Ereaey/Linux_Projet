Protocole sérial
===========

### Action, 1 octet ###
* 0x00 : Modification Angle Moteur (Deplacement de x)
* 0x01 : Modification Angle Moteur (Deplacement vers x)
* 0x02 : Allumer eteindre LED
* 0X03 : Lancer forme

### 0x00 : Angles moteurs, 2 octets ###
* Valeur à ajouter au servo 1 en hexa
* Valeur à ajouter au servo 2 en hexa  
Ajouter 100 à la valeur pour négatif  
Angle Max 90°

### 0X01 : Angles moteurs, 2 octets ###
* Angle servo 1 en hexa
* Angle servo 2 en hexa

### 0X02 : LED, 1 octet ###
* 0x00 Eteindre
* 0x01 Allumer

### 0x03 Lancer forme, 1 octet ###
* id_forme en hexa
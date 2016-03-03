Protocole sérial
===========

### Action, 1 octet ###
* 0x41 : Modification Angle Moteur (Deplacement de x)
* 0x42 : Modification Angle Moteur (Deplacement vers x)
* 0x43 : Allumer eteindre LED
* 0X44 : Lancer forme  

Enumération possible pour son implémentation en C++
` enum Command{Move, MoveTo, Led, Draw}; `

### 0x41 : Angles moteurs, 2 octets ###
* Valeur à ajouter au servo 1 en hexa
* Valeur à ajouter au servo 2 en hexa  
Ne pas se déplacer 0x41  
Se déplacer de + 10 0x42   
Se déplacer de - 10 0x43  


### 0X42 : Angles moteurs, 2 octets ###
* Angle servo 1 en hexa + 0x41
* Angle servo 2 en hexa + 0x41

### 0X43 : LED, 1 octet ###
* 0x41 Eteindre
* 0x42 Allumer
* 0x43 Switch

### 0x44 Lancer forme, 1 octet ###
* id_forme en hexa à partir de 0x41
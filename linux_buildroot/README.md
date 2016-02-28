Utilisation buildroot
----------------

Téléchargement direct sur le site ou via le git  
`git clone git://git.buildroot.net/buildroot`

Nous pouvons voir la liste des templates possible à l'aide de  
`make list_defconfigs`

Nous allons ensuite pouvoir utiliser le template de la beaglebone
`make beaglebone_defconfig`

Ensuite nous le configurons plus en détail  
`make menuconfig`  

Toute la configuration du noyau et du rootfs....  
(Selection de l'ajout du kernel, ajout de u-boot, modification diverses) Activer device tree  
`make uboot-menuconfig`

Lancer la compilation `make`

Pour finir nous pouvons récuperer les fichiers dans `output/images/`

On doit utiliser `make distclean` pour pouvoir refaire une compilation à partir de zéro
Compilation de u-boot, kernel et rootfs pour une beaglebone white
============

Pour commencer nous allons avoir besoin d'une toolchain qui nous permettra
la crosscompilation de nos différents élements.

Creation manuelle
----------------

### Toolchain ###


Pour cela, j'ai choisi la toolchain linaro.  
`https://releases.linaro.org/components/toolchain/binaries/5.2-2015.11/arm-linux-gnueabihf/gcc-linaro-5.2-2015.11-x86_64_arm-linux-gnueabihf.tar.xz`

Nous pouvons ensuite l'extraire et la tester avec `arm-linux-gnueabihf-gcc --version`

### U-boot ###

Téléchargement de u-boot depuis le git correspondant.  
`git clone https://github.com/u-boot/u-boot`

Nous vidons les anciens fichiers de configuration  
`make ARCH=arm CROSS_COMPILE=chemin_toolchain distclean`

L'arm de notre beaglebone est un am335x donc nous choissions le fichier de config correspondant  
`make ARCH=arm CROSS_COMPILE=chemin_toolchain am335x_evm_defconfig`

Ensuite nous pouvons personnaliser notre u-boot à l'aide du menuconfig  
`make menuconfig ARCH=arm CROSS_COMPILE=chemin_toolchain`

Et pour terminer nous le compilons  
`make ARCH=arm CROSS_COMPILE=chemin_toolchain`

### Kernel ###

Téléchargement du kernel depuis kernel.org  
`wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.4.2.tar.xz`

Nous vidons les anciens fichiers de configuration  
`make ARCH=arm CROSS_COMPILE=chemin_toolchain distclean`

Nous allons ensuite télécharger un fichier de configuration pour la beaglebone  
`https://github.com/beagleboard/linux/tree/4.1/arch/arm/configs`  
Et nous allons l'inclure à notre kernel dans le dossier `arch/arm/configs/`  

Ajouter celui ci dans notre .config  
`make ARCH=arm CROSS_COMPILE=chemin_toolchain bb.org_defconfig`

Ensuite nous pouvons personnaliser notre kernel à l'aide du menuconfig  
`make menuconfig ARCH=arm CROSS_COMPILE=chemin_toolchain`

Et pour terminer nous le compilons  
`make ARCH=arm CROSS_COMPILE=chemin_toolchain -j 4`

### Rootfs ###
#### Multistrap ####
Permet de génerer un rootfs avec base débian


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
(Selection de l'ajout du kernel, ajout de u-boot, modification diverses)  
`make uboot-menuconfig`

Lancer la compilation `make`

Pour finir nous pouvons récuperer les fichiers dans `output/images/`

On doit utiliser `make distclean` pour pouvoir refaire une compilation à partir de zéro

Mise en place de la SD
----------------

~~~
New size: 50MB
File System: FAT32
Label: BOOT

New Size: 1000MB
File System: EXT3
Label: RFS
~~~

~~~
Partition BOOT
U-boot
MLO
uImage
UEnv.txt
~~~

~~~
Partition RFS
rootfs
~~~

Code python
----------------

### Creation toolchain ###

~~~python
url_toolchain = "https://releases.linaro.org/components/toolchain/binaries/5.2-2015.11/arm-linux-gnueabihf/gcc-linaro-5.2-2015.11-x86_64_arm-linux-gnueabihf.tar.xz"
#  Telechargement toolchain
filename_toolchain = wget.download(url_toolchain)
os.rename(filename_toolchain, "toolchain.tar.xz")
#  Decompression toolchain
os.system("mkdir download/toolchain && tar xf "+filename_toolchain + " -C download/toolchain --strip-components 1")
path_toolchain = "/download/toolchain/bin/arm-linux-gnueabihf-"
~~~

### Creation U-boot ###

~~~python
# Telechargement de uboot depuis le git
os.system("git clone https://github.com/u-boot/u-boot download/u-boot")
os.system("cd download/u-boot")
# Nettoyage des fichiers
os.system("make ARCH=arm CROSS_COMPILE=" + path_toolchain + " distclean")
# Selection de la config am335
os.system("make ARCH=arm CROSS_COMPILE=" + path_toolchain + " am335x_evm_defconfig")
# Ouverture du menuconfig pour personnaliser le uboot
os.system("make menuconfig ARCH=arm CROSS_COMPILE=" + path_toolchain") 
# Compilation de uboot
os.system("make ARCH=arm CROSS_COMPILE=" + path_toolchain)
~~~

### Creation Kernel ###

~~~python
# Telechargement de uboot depuis le git
os.system("git clone https://github.com/u-boot/u-boot download/u-boot")
os.system("cd download/u-boot")
# Nettoyage des fichiers
os.system("make ARCH=arm CROSS_COMPILE=" + path_toolchain + " distclean")
# Selection de la config am335
os.system("make ARCH=arm CROSS_COMPILE=" + path_toolchain + " am335x_evm_defconfig")
# Ouverture du menuconfig pour personnaliser le uboot
os.system("make menuconfig ARCH=arm CROSS_COMPILE=" + path_toolchain") 
# Compilation de uboot
os.system("make ARCH=arm CROSS_COMPILE=" + path_toolchain)
~~~
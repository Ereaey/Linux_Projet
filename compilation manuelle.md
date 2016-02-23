Creation manuelle
----------------

Pour commencer nous allons avoir besoin d'une toolchain qui nous permettra la crosscompilation de nos différents élements.  

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
#### Busybox ####  
Configuration du rootfs  
`make menuconfig`  
`make`
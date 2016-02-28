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
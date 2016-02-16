import wget
import urllib
import bz2
import tarfile
import shutil
import os

#deb http://www.emdebian.org/debian wheezy main
url_toolchain = 'https://releases.linaro.org/components/toolchain/binaries/5.2-2015.11/arm-linux-gnueabihf/gcc-linaro-5.2-2015.11-x86_64_arm-linux-gnueabihf.tar.xz'
url_kernel = 'https://cdn.kernel.org/pub/linux/kernel/v3.0/linux-3.2.2.tar.bz2'

p=os.popen("echo `pwd`", "r").read().rstrip('\n') + "/gcc-linaro-5.2-2015.11-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-"

print '\033[92m' + "Creation de u-boot, kernel, rootfs pour beaglebone" + '\033[0m'
#print p
print '\033[31m' + "Suppresion des anciens fichiers" + '\033[0m'

print '\033[92m' + "Telechargement des fichiers" + '\033[0m'

print '\033[95m' + "Telechargement toolchain" + '\033[0m'
filename_toolchain = wget.download(url_toolchain)

print '\033[95m' + "\nTelechargement du kernel" + '\033[0m'
filename_kernel = wget.download(url_kernel)

print '\033[95m' + "\nTelechargement du u-boot" + '\033[0m'
os.system("git clone https://github.com/u-boot/u-boot")
os.system("cd u-boot/")
#os.system("git checkout v2016.01 -b tmp")
#os.system("wget -c https://rcn-ee.com/repos/git/u-boot-patches/v2016.01/0001-am335x_evm-uEnv.txt-bootz-n-fixes.patch")
#os.system("patch -p1 < 0001-am335x_evm-uEnv.txt-bootz-n-fixes.patch")
os.system("cd ..")
#urllib.urlretrieve('ftp://ftp.denx.de/pub/u-boot/u-boot-2016.01.tar.bz2', 'u-boot.tar.bz2')

print '\033[92m' + "Decompression toolchain" + '\033[0m'
os.system("tar xf " + filename_toolchain)
os.system(p + "gcc --version")#Test toolchain

print '\033[92m' + "Decompression kernel" + '\033[0m'
tar = tarfile.open(filename_kernel)
tar.extractall(path="kernel/")
tar.close()

print '\033[31m' + "Supression des archives" + '\033[0m'

try:
    os.remove(filename_kernel)
except OSError:
    pass
try:
    os.remove(filename_toolchain)
except OSError:
    pass

print '\033[92m' + "U-boot, config target beaglebone white : am335x_evm_defconfig" + '\033[0m'
os.chdir("u-boot/")
os.system("make ARCH=arm CROSS_COMPILE="+p+" distclean")
os.system("make ARCH=arm CROSS_COMPILE="+p+" am335x_evm_defconfig")
print 'Personnalisation du u-boot'
#Modification du message prompt .config
print '\033[92m' + "Compilation de u-boot" + '\033[0m'
os.system("make ARCH=arm CROSS_COMPILE="+p+" -j4")
print '\033[92m' + "U-boot est maintenant compile" + '\033[0m'

print '\033[92m' + "Kernel, config target beaglebone white : am335x_evm_config" + '\033[0m'
os.chdir("..")
#os.system("make ARCH=arm CROSS_COMPILE=arm-none-eabi-")
import wget
import urllib
import bz2
import tarfile
import shutil
import os
import subprocess

#out = subprocess.check_output(["ls", "-ltr"])

url_toolchain = 'https://releases.linaro.org/components/toolchain/binaries/5.2-2015.11/arm-linux-gnueabihf/gcc-linaro-5.2-2015.11-x86_64_arm-linux-gnueabihf.tar.xz'
url_kernel = 'https://cdn.kernel.org/pub/linux/kernel/v3.0/linux-3.2.2.tar.bz2'
rep_courant = os.popen("echo `pwd`", "r").read().rstrip('\n')
os.system("mkdir download")
os.system("mkdir generate")
#p=os.popen("echo `pwd`", "r").read().rstrip('\n') + "/gcc-linaro-5.2-2015.11-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-"

print '\033[92m' + "Creation de u-boot, kernel, rootfs pour beaglebone white" + '\033[0m'
#print p
#print '\033[31m' + "Suppresion des anciens fichiers" + '\033[0m'

print '\033[92m' + "Telechargement des fichiers" + '\033[0m'

print '\033[95m' + "Telechargement toolchain, linaro" + '\033[0m'
filename_toolchain = wget.download(url_toolchain)
os.rename(filename_toolchain, "toolchain.tar.xz")
filename_toolchain = "toolchain.tar.xz"
os.system("mv " + filename_toolchain + " download/" + filename_toolchain)

print '\033[95m' + "\nTelechargement du kernel, 3.2.2" + '\033[0m'
filename_kernel = wget.download(url_kernel)
os.rename(filename_kernel, "kernel.tar.bz2")
filename_kernel = "kernel.tar.bz2"
os.system("mv " + filename_kernel + " download/" + filename_kernel)

print '\033[95m' + "\nTelechargement du u-boot" + '\033[0m'
os.system("git clone https://github.com/u-boot/u-boot download/u-boot")

print '\033[92m' + "Decompression toolchain" + '\033[0m'
os.system("mkdir download/toolchain && tar xf " + filename_toolchain + " -C download/toolchain --strip-components 1")
path_toolchain = rep_courant + "/download/toolchain/bin/arm-linux-gnueabihf-"
print "path : " + path_toolchain

#os.system(p + "gcc --version")#Test toolchain

print '\033[92m' + "Decompression kernel" + '\033[0m'
tar = tarfile.open(filename_kernel)
tar.extractall(path="download/kernel/")
tar.close()

print '\033[31m' + "Supression des archives" + '\033[0m'

try:
    os.remove("download/" + filename_kernel)
except OSError:
    pass
try:
    os.remove("download" + filename_toolchain)
except OSError:
    pass

print '\033[92m' + "U-boot, config target beaglebone white : am335x_evm_defconfig" + '\033[0m'
os.chdir("download/u-boot/")
os.system("make ARCH=arm CROSS_COMPILE="+path_toolchain+" distclean")
os.system("make ARCH=arm CROSS_COMPILE="+path_toolchain+" am335x_evm_defconfig")
print 'Personnalisation du u-boot'
#Modification du message prompt .config
print '\033[92m' + "Compilation de u-boot" + '\033[0m'
os.system("make ARCH=arm CROSS_COMPILE="+path_toolchain+" -j4")
print '\033[92m' + "U-boot est maintenant compile" + '\033[0m'

print '\033[92m' + "Kernel, config target beaglebone white : am335x_evm_config" + '\033[0m'
os.chdir("..")
#os.system("make ARCH=arm CROSS_COMPILE=arm-none-eabi-")
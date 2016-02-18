import os

class Generator:
    def __init__(self):
        self.rep_courant = os.popen("echo `pwd`", "r").read().rstrip('\n')

    def generateUboot(self, toolchain):
        print '\033[92m' + "U-boot, config target beaglebone white : am335x_evm_defconfig" + '\033[0m'
        os.chdir("download/u-boot/")
        os.system("make ARCH=arm CROSS_COMPILE="+toolchain+" distclean")
        os.system("make ARCH=arm CROSS_COMPILE="+toolchain+" am335x_evm_defconfig")
        print '\033[92m' + 'Personnalisation du u-boot' + '\033[0m'
        os.system("cp ../../configuration/config_uboot ../../download/u-boot/.config")
        print '\033[92m' + "Compilation de u-boot" + '\033[0m'
        os.system("make ARCH=arm CROSS_COMPILE="+toolchain+" -j 4")
        print '\033[92m' + "U-boot est maintenant compile" + '\033[0m'
        os.system("cp u-boot.img ../../generate/boot/u-boot.img")
        os.chdir("../..")
        
    def generateKernel(self, toolchain):
        print '\033[92m' + "Kernel, config target beaglebone white : am335x_evm_defconfig" + '\033[0m'
        os.chdir("download/kernel")
        os.system("make ARCH=arm CROSS_COMPILE="+toolchain+" distclean")
        os.system("cp ../../configuration/bb.org_defconfig ../../download/kernel/arch/arm/configs/bb.org_defconfig")
        os.system("make menuconfig ARCH=arm CROSS_COMPILE="+toolchain+" bb.org_defconfig")
        print '\033[92m' + "Compilation du kernel" + '\033[0m'
        os.system("make ARCH=arm CROSS_COMPILE="+toolchain+" -j4")
        os.system("make ARCH=arm CROSS_COMPILE="+toolchain+" uImage LOADADDR=0x80008000 -j4")
        #os.system("make ARCH=arm CROSS_COMPILE="+toolchain+" uImage-dtb.am335x-bone -j4")
        os.system("make ARCH=arm CROSS_COMPILE="+toolchain+" modules -j4")
        print '\033[92m' + "le kernel est maintenant compile" + '\033[0m'
        #os.system("cp u-boot.img ../../generate/boot/u-boot.img")
        '''
        sudo cp arch/arm/boot/dts/*.dtb /boot/
        sudo cp arch/arm/boot/dts/overlays/*.dtb* /boot/overlays/
        sudo cp arch/arm/boot/dts/overlays/README /boot/overlays/
        sudo scripts/mkknlimg arch/arm/boot/zImage /boot/$KERNEL.img
        '''
        os.chdir("../..")
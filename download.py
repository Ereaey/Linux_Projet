import os
import wget
import tarfile
import shutil
import subprocess

class Download:
    def __init__(self):
        self.url_toolchain = 'https://releases.linaro.org/components/toolchain/binaries/5.2-2015.11/arm-linux-gnueabihf/gcc-linaro-5.2-2015.11-x86_64_arm-linux-gnueabihf.tar.xz'
        self.url_kernel = 'https://cdn.kernel.org/pub/linux/kernel/v3.0/linux-3.2.2.tar.bz2'
        self.rep_courant = os.popen("echo `pwd`", "r").read().rstrip('\n')
        #os.mkdir('download')
        self.filename_toolchain = "toolchain.tar.xz"
        self.filename_kernel = "kernel.tar.bz2"
        
    def downloadToolchain(self):
        print '\033[95m' + "Telechargement toolchain, linaro" + '\033[0m'
        self.filename_toolchain = wget.download(self.url_toolchain)
        os.rename(self.filename_toolchain, "toolchain.tar.xz")
        self.filename_toolchain = "toolchain.tar.xz"
        os.system("mv " + self.filename_toolchain + " download/" + self.filename_toolchain)
        print '\033[95m' + "\nTelechargement effectue" + '\033[0m'
        
    def downloadKernel(self):
        print '\033[95m' + "\nTelechargement du kernel, 3.2.2" + '\033[0m'
        self.filename_kernel = wget.download(self.url_kernel)
        os.rename(self.filename_kernel, "kernel.tar.bz2")
        self.filename_kernel = "kernel.tar.bz2"
        os.system("mv " + self.filename_kernel + " download/" + self.filename_kernel)
        print '\033[95m' + "\nTelechargement effectue" + '\033[0m'

    def downloadUboot(self):
        print '\033[95m' + "\nTelechargement du u-boot a partir de git" + '\033[0m'
        os.system("git clone https://github.com/u-boot/u-boot download/u-boot")
        print '\033[95m' + "Telechargement effectue" + '\033[0m'
        
    def decompressToolchain(self):
        print '\033[95m' + "\nDecompression toolchain" + '\033[0m'
        try:
            with open("download/"+self.filename_toolchain): pass
            os.system("mkdir download/toolchain && tar xf download/"+self.filename_toolchain + " -C download/toolchain --strip-components 1")
            print '\033[95m' + "Fin decompression toolchain" + '\033[0m'
        except IOError:
           print '\033[95m' + "Erreur decompression toolchain (fichier manquant)" + '\033[0m'
        
        
    def decompressKernel(self):
        print '\033[95m' + "\nDecompression kernel" + '\033[0m'
        tar = tarfile.open("download/"+self.filename_kernel)
        tar.extractall(path="download/kernel/")
        tar.close()
        print '\033[95m' + "Fin decompression kernel" + '\033[0m'


    def cleanFiles(self):
        try:
            os.remove("download/kernel.tar.bz2")
        except OSError:
            pass
        try:
            os.remove("download/toolchain.tar.xz")
        except OSError:
            pass
        
    def clearFolders(self):
        shutil.rmtree("download", ignore_errors=True)
        os.mkdir('download')
        print '\033[95m' + "Suppression effectuee" + '\033[0m'
        return True
    def clearKernel(self):
        shutil.rmtree("download/kernel", ignore_errors=True)
    def clearUboot(self):
        shutil.rmtree("download/u-boot", ignore_errors=True)
    def clearToolchain(self):
        shutil.rmtree("download/toolchain", ignore_errors=True)
    def getToolchain(self):
        return self.rep_courant + "/download/toolchain/bin/arm-linux-gnueabihf-"
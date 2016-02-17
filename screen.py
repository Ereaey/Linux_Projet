#!/usr/bin/env python

from os import system
import os
import curses
from download import *
import fileinput

d = Download()

x = 0
e = 0
while x != ord('6'):
    screen = curses.initscr()
    screen.clear()
    screen.addstr(1, 1, "Creation de u-boot, kernel, rootfs pour beaglebone white")
    screen.addstr(3, 1, "1 - Telecharger les fichiers")
    screen.addstr(4, 1, "2 - Compiler")
    screen.addstr(5, 1, "3 - Supprimer les fichiers")
    screen.addstr(6, 1, "4 - Recuperer les fichiers")
    screen.addstr(7, 1, "5 - Automatique mode")
    screen.addstr(8, 1, "6 - Quitter")
    screen.addstr(9, 1, "Votre choix ? ")
    screen.refresh()
    
    x = screen.getch()
    
    if x == ord('1'):
        e = 0
        while e != ord('6'):
            screen.clear()
            screen.addstr(1, 1, "Telechargement des fichiers")
            screen.addstr(3, 1, "1 - Tout")
            screen.addstr(4, 1, "2 - Toolchain")
            screen.addstr(5, 1, "3 - Kernel")
            screen.addstr(6, 1, "4 - u-boot")
            screen.addstr(7, 1, "5 - rootfs")
            screen.addstr(8, 1, "6 - Quitter")
            screen.addstr(9, 1, "Votre choix ? ")
            screen.refresh()
            e = screen.getch()
            screen.clear()
            screen.refresh()
            curses.endwin()
            if e == ord('1'):
                d.clearFolders()
                d.downloadToolchain()
                d.downloadKernel()
                d.downloadUboot()
                d.decompressToolchain()
                d.decompressKernel()
                d.cleanFiles()
            elif e == ord('2'):
                d.clearToolchain()
                d.downloadToolchain()
                d.decompressToolchain()
                d.cleanFiles()
            elif e == ord('3'):
                d.clearKernel()
                d.downloadKernel()
                d.decompressKernel()
                d.cleanFiles()
            elif e == ord('4'):
                d.clearUboot()
                d.downloadUboot()
        curses.endwin()
    if x == ord('2'):
        e = 0
        while e != ord('5'):
            screen.clear()
            screen.addstr(1, 1, "Compilation pour la beaglebone white")
            screen.addstr(3, 1, "1 - Tout")
            screen.addstr(4, 1, "2 - Kernel")
            screen.addstr(5, 1, "3 - u-boot")
            screen.addstr(6, 1, "4 - rootfs")
            screen.addstr(7, 1, "5 - Quitter")
            screen.addstr(8, 1, "Votre choix ? ")
            screen.refresh()
            e = screen.getch()
            screen.clear()
            screen.refresh()
            curses.endwin()
            if e == ord('1'):
                screen.clear()
                screen.refresh()
                curses.endwin()
                d.clearFolders()
                d.cleanFiles()
                d.downloadToolchain()
                d.downloadKernel()
                d.downloadUboot()
                d.decompressToolchain()
                d.decompressKernel()
                d.cleanFiles()
            elif e == ord('2'):
                d.clearToolchain()
                d.downloadToolchain()
                d.decompressToolchain()
                d.cleanFiles()
            elif e == ord('3'):
                print '\033[92m' + "U-boot, config target beaglebone white : am335x_evm_defconfig" + '\033[0m'
                os.chdir("download/u-boot/")
                os.system("make ARCH=arm CROSS_COMPILE="+d.getToolchain()+" distclean")
                os.system("make ARCH=arm CROSS_COMPILE="+d.getToolchain()+" am335x_evm_defconfig")
                print '\033[92m' + 'Personnalisation du u-boot' + '\033[0m'
                #Modification du message prompt .config
                #CONFIG_AUTOBOOT_PROMPT="Press SPACE to abort autoboot in %d seconds\n"
                '''
                f = file(".config","r")    # ouvrir le fichier
                chaine = f.read()                   # le charger dans une chaine de caracteres
                f.close()                           # fermer le fichier
                result=chaine.replace('CONFIG_AUTOBOOT_PROMPT="', 'CONFIG_AUTOBOOT_PROMPT="ARTHUS Anthony \n PAUCHET Adeline \n')
                f = file(".config","w")    # ouvrir le fichier de sortie
                # en ecriture  Tu peux ouvrir le meme si tu veux lecraser
                f.write(result)                     # ecrire le resultat dans le fichier
                f.close()            
                '''
                print '\033[92m' + "Compilation de u-boot" + '\033[0m'
                os.system("make ARCH=arm CROSS_COMPILE="+d.getToolchain()+" -j4")
                print '\033[92m' + "U-boot est maintenant compile" + '\033[0m'
            elif e == ord('4'):
                screen.clear()
                screen.refresh()
                curses.endwin()
                d.clearUboot()
                d.downloadUboot()
        curses.endwin()
        #execute_cmd("apachectl restart")
        
    if x == ord('3'):
        d.clearFolders()
        curses.endwin()

curses.endwin()



'''
username = get_param("Enter the username")
homedir = get_param("Enter the home directory, eg /home/nate")
groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
shell = get_param("Enter the shell, eg /bin/bash:")
curses.endwin()
execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
'''
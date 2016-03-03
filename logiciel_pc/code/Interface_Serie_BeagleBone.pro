#-------------------------------------------------
#
# Project created by QtCreator 2016-02-23T12:14:35
#
#-------------------------------------------------

QT       += core gui
QT       += serialport

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Interface_Serie_BeagleBone
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    connexionserie.cpp \
    protocole.cpp

HEADERS  += mainwindow.h \
    connexionserie.h \
    protocole.h

FORMS    += mainwindow.ui \
    connexionserie.ui

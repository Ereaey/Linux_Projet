#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    SerialWindow = new ConnexionSerie(this);
    ProtocoleBeagleBone = new Protocole;
    QObject::connect(SerialWindow, SIGNAL(InitSerialConnection(QString)), this, SLOT(SerialConnect(QString)));
    //connect(serial,SIGNAL(readyRead()),this,SLOT(donnee_recue()));
}

MainWindow::~MainWindow()
{
    delete SerialWindow;
    delete ProtocoleBeagleBone;
    delete ui;
}

void MainWindow::on_ButtonSerial_clicked()
{
    SerialWindow->show();
}

void MainWindow::SerialConnect(QString PortName)
{
    serial = new QSerialPort(this);
    serial->setPortName(PortName);
    if (serial->open(QIODevice::ReadWrite))
    {
        serial->setBaudRate(QSerialPort::Baud9600);
        serial->setDataBits(QSerialPort::Data8);
        serial->setParity(QSerialPort::NoParity);
        serial->setStopBits(QSerialPort::OneStop);
        serial->setFlowControl(QSerialPort::NoFlowControl);
        ui->textEditLog->append("Connecté à : " + PortName + " 9600Bds, 8 Data, NoParity, 1 Stop ");
        ui->GroupBoxFormes->setEnabled(true);
        ui->GroupBoxCommandeManuelle->setEnabled(true);
        connect(serial, SIGNAL(bytesWritten(qint64)), this,SLOT(DataWritten(qint64)));

    }
    else
    {
        serial->close(); //fermeture de la liaison série
        ui->textEditLog->append("Impossible de se connecter à : " + PortName);
    }

}

void MainWindow::DataWritten(qint64)
{
    ui->textEditLog->append("Trame envoyée : " + ProtocoleBeagleBone->GetTrame());
}

void MainWindow::on_ButtonDeconexion_clicked()
{
    if(serial->isOpen())
    {
        ui->textEditLog->append("Connexion " + serial->portName() + " fermée");
        ui->GroupBoxCommandeManuelle->setEnabled(false);
        ui->GroupBoxFormes->setEnabled(false);
        serial->close();
    }
}

void MainWindow::on_ButtonLaser_clicked()
{
    ProtocoleBeagleBone->SwitchLaser();
    serial->write(ProtocoleBeagleBone->GetTrame());
}

void MainWindow::on_ButtonSquare_clicked()
{
    ProtocoleBeagleBone->LancerForme(65);
    serial->write(ProtocoleBeagleBone->GetTrame());
}

void MainWindow::on_ButtonCircle_clicked()
{
    ProtocoleBeagleBone->LancerForme(66);
    serial->write(ProtocoleBeagleBone->GetTrame());
}

void MainWindow::on_ButtonUp_clicked()
{
    ProtocoleBeagleBone->DeplacerMoteur(1,0);
    serial->write(ProtocoleBeagleBone->GetTrame());
}

void MainWindow::on_ButtonDown_clicked()
{
    ProtocoleBeagleBone->DeplacerMoteur(-1,0);
    serial->write(ProtocoleBeagleBone->GetTrame());
}

void MainWindow::on_ButtonLeft_clicked()
{
    ProtocoleBeagleBone->DeplacerMoteur(0,-1);
    serial->write(ProtocoleBeagleBone->GetTrame());
}

void MainWindow::on_ButtonRight_clicked()
{
    ProtocoleBeagleBone->DeplacerMoteur(0,1);
    serial->write(ProtocoleBeagleBone->GetTrame());
}

void MainWindow::on_ButtonCenter_clicked()
{
    ProtocoleBeagleBone->GoToAngle(0,0);
    serial->write(ProtocoleBeagleBone->GetTrame());
}

#include "connexionserie.h"
#include "ui_connexionserie.h"

ConnexionSerie::ConnexionSerie(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::ConnexionSerie)
{
    ui->setupUi(this);
    QList<QSerialPortInfo> list;
    list = QSerialPortInfo::availablePorts();

    for(int i = 0; i < list.size(); i++)
        ui->ComboBoxLine->addItem(list.at(i).portName());
}

ConnexionSerie::~ConnexionSerie()
{
    delete ui;
}

void ConnexionSerie::on_buttonBox_accepted()
{
    emit InitSerialConnection(ui->ComboBoxLine->currentText());
}

void ConnexionSerie::on_ButtonRefresh_clicked()
{
    ui->ComboBoxLine->clear();
    QList<QSerialPortInfo> list;
    list = QSerialPortInfo::availablePorts();

    for(int i = 0; i < list.size(); i++)
        ui->ComboBoxLine->addItem(list.at(i).portName());
}

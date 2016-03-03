#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtSerialPort/QSerialPort>
#include "connexionserie.h"
#include "protocole.h"

/*!
 * \file mainwindow.h
 * \brief Classe gérant la fenetre principale
 * \author Simonutti Thibault
 * \date 02/03/2016
 */

namespace Ui {
class MainWindow;
}

struct ParametresSerie
{

};

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    /*!
     * \brief on_ButtonSerial_clicked : Slot permettant d'afficher la fenetre de parametrage de la connexion série
     */
    void on_ButtonSerial_clicked();

    /*!
     * \brief SerialConnect permet de lancer la connexion série
     * \param PortName Port auquel on veut se connecter
     */
    void SerialConnect(QString PortName);

    /*!
     * \brief on_ButtonDeconexion_clicked Slot permettant de couper la liaison série
     */
    void on_ButtonDeconexion_clicked();

    /*!
     * \brief on_ButtonLaser_clicked : slot permettant d'allumer ou d'éteindre le laser
     */
    void on_ButtonLaser_clicked();

    /*!
     * \brief on_ButtonUp_clicked : Slot permettant d'éffectuer un déplacement de 10° vers le haut
     */
    void on_ButtonUp_clicked();

    /*!
     * \brief on_ButtonDown_clicked : Slot permettant d'éffectuer un déplacement de 10° vers le bas
     */
    void on_ButtonDown_clicked();

    /*!
     * \brief on_ButtonLeft_clicked: Slot permettant d'éffectuer un déplacement de 10° vers la gauche
     */
    void on_ButtonLeft_clicked();

    /*!
     * \brief on_ButtonRight_clicked : Slot permettant d'éffectuer un déplacement de 10° vers la droite
     */
    void on_ButtonRight_clicked();

    /*!
     * \brief on_ButtonCircle_clicked : Slot permettant de déssiner un cercle avec le laser
     */
    void on_ButtonCircle_clicked();

    /*!
     * \brief on_ButtonSquare_clicked : Slot permettant de déssiner un carré avec le laser
     */
    void on_ButtonSquare_clicked();

    /*!
     * \brief on_ButtonCenter_clicked : Slot permettant de remettre le pointeur laser à la position intiale
     */
    void on_ButtonCenter_clicked();

    /*!
     * \brief DataWritten : Slot emit lors de l'envoie de données sur la liaison série, il est utilisé pour afficher les logs dans
     * la fenêtre de logs
     */
    void DataWritten(qint64);

private:
    Ui::MainWindow *ui;
    QSerialPort *serial;
    ConnexionSerie *SerialWindow;
    Protocole *ProtocoleBeagleBone;
};

#endif // MAINWINDOW_H

#ifndef CONNEXIONSERIE_H
#define CONNEXIONSERIE_H

#include <QDialog>
#include <QtSerialPort/QSerialPort>
#include <QtSerialPort/QSerialPortInfo>
#include <QList>


/*!
 * \file connexionserie.h
 * \brief Classe permettant de selectioner les paramètres de la connexion série
 * \author Simonutti Thibault
 * \date 02/03/2016
 */


namespace Ui {
class ConnexionSerie;
}

class ConnexionSerie : public QDialog
{
    Q_OBJECT

public:
    explicit ConnexionSerie(QWidget *parent = 0);
    ~ConnexionSerie();

signals:
    /*!
     * \brief InitSerialConnection
     *
     *  signal envoyé lors de l'appui du bouton "ok"
     *
     * \param line : Port sur lequel on désire établir la connexion série
     *
     */
    void InitSerialConnection(QString line);

private slots:
    /*!
     * \brief on_buttonBox_accepted
     *
     * Permet d'envoyer le signal "InitSerialConnection"
     *
     */

    void on_buttonBox_accepted();

    /*!
     * \brief on_ButtonRefresh_clicked
     *
     * permet d'actualiser les ports série accessibles pour la connexion série.
     *
     */
    void on_ButtonRefresh_clicked();

private:
    Ui::ConnexionSerie *ui;
};

#endif // CONNEXIONSERIE_H

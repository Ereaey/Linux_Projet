#ifndef PROTOCOLE_H
#define PROTOCOLE_H

#include <QByteArray>

/*!
 * \file protocoleserie.h
 * \brief Classe gérant le protocole de communication série
 * \author Simonutti Thibault
 * \date 02/03/2016
 */

#define FinTrame '\0'



class Protocole
{

public:

    /*!
     * \brief AllumerLaser est une
     *  Méthode qui permet de créer une trame permettant d'allumer le laser
     */
    void AllumerLaser(void);

    /*!
     * \brief EteindreLaser est une
     *  Méthode qui permet de créer une trame permettant d'éteindre le laser
     */
    void EteindreLaser(void);


    /*!
     * \brief SwitchLaser est une méthode qui permet de changer l'état actuel du laser
     */
    void SwitchLaser(void);

    /*!
     * \brief DeplacerMoteur1 permet de déplacer le premier moteur de 10° dans le sens voulu
     */
    void DeplacerMoteur(int SensMoteur1, int SensMoteur2);

    /*!
     * \brief GoToAngle est une
     *  Méthode qui permet de créer une trame pour déplacer les servos moteur à un angle désiré
     *
     * \param AngleServo1 : Angle voulu pour le servo moteur N°1
     * \param AngleServo2 : Angle voulu pour le servo moteur N°2
     * \return 0 Si succes,
     * 1 Si erreur sur le premier angle
     * 2 Si erreur sur le deuxième angle
     */
    int GoToAngle(int AngleServo1, int AngleServo2);

    /*!
     * \brief LancerForme est une
     *  Méthode qui permet de créer une trame pour lancer le déssin d'une forme voulue
     * \param Forme : Identifiant de la forme désirée
     */
    void LancerForme(int Forme);

    /*!
     * \brief Constructeur de la classe "protocoleserie"
     */
    ProtocoleSerie();

    /*!
     * \brief GetTrame est un accesseur pour l'attribut Trame.
     * \return Retourne l'attribut trame de type QByteArray
     */
    QByteArray GetTrame(void);

private:
    /*!
     * \brief The Command enum
     * Enumeration des commandes
     *!< Commande Move, valeur : 0x00
     *!< Commande MoveTo, valeur : 0x01
     *!< Commande Laser, valeur : 0x02
     *!< Commane Draw, valeur : 0x03
     */
    enum Command{
                 Move = 65,
                 MoveTo,
                 Laser,
                 Draw};

    enum Formes{
                Carre = 65,
                Cercle,
                Losange};

    enum Laser{
                Off = 65,
                On,
                Switch};

    enum Direction{
                    Rien = 65,
                    Droite,
                    Gauche};

    QByteArray trame; //!< Trame a envoyer sur la liaison série */
};

#endif // PROTOCOLE_H

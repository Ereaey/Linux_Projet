#include "protocole.h"

/*!
 * \file protocoleserie.cpp
 * \author Simonutti Thibault
 * \date 02/03/2016
 */

Protocole::ProtocoleSerie()
{

}

void Protocole::AllumerLaser()
{
    trame.clear();
    trame.append(Laser);
    trame.append(On);
    trame.append(FinTrame);
}

void Protocole::EteindreLaser()
{
    trame.clear();
    trame.append(Laser);
    trame.append(Off);
    trame.append(FinTrame);
}

void Protocole::SwitchLaser()
{
    trame.clear();
    trame.append(Laser);
    trame.append(Switch);
    trame.append(FinTrame);
}

void Protocole::DeplacerMoteur(int SensMoteur1, int SensMoteur2)
{
    trame.clear();
    trame.append(Move);
    switch(SensMoteur1)
    {
        case -1:trame.append(Gauche);break;
        case 0:trame.append(Rien);break;
        case 1:trame.append(Droite);break;
    }
    switch(SensMoteur2)
    {
        case -1:trame.append(Gauche);break;
        case 0:trame.append(Rien);break;
        case 1:trame.append(Droite);break;
    }
    trame.append(FinTrame);
}

int Protocole::GoToAngle(int AngleServo1, int AngleServo2)
{
    AngleServo1 += 65;
    AngleServo2 += 65;
    int CodeErreur = 0;
    if(AngleServo1 > 90 || AngleServo1 < 0)
        CodeErreur = -1;
    if(AngleServo2 >90 || AngleServo2 < 0)
        CodeErreur = -2;
    trame.clear();
    trame.append(MoveTo);
    trame.append(AngleServo1);
    trame.append(AngleServo2);
    trame.append(FinTrame);

    return CodeErreur;
}

void Protocole::LancerForme(int Forme)
{
    trame.clear();
    trame.append(Draw);
    trame.append(Forme);
    trame.append(FinTrame);
}

QByteArray Protocole::GetTrame(void)
{
    return this->trame;
}

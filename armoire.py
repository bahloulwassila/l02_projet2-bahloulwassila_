from consts import *
import random
import pandas as pd
from typing import List, NoReturn, Tuple


# Créer la classe Vetement avec les paramètres estDIY, prixAchat, prixVente, profit, couleur1, couleur2, style, typeObj
class Vetement:
    def __init__(self, nom: str, estDIY: bool, prixAchat: int, prixVente: int, balance: int, couleur1: str,
                 couleur2: str, style: str, typeObj: str):
        """Initialisateur de la classe Vetement"""
        # Initialiser les autres attributs
        self.__nom__ = nom
        self.__prixAchat__ = prixAchat
        self.__prixVente__ = prixVente
        self.__balance__ = balance
        self.__couleurs__ = [couleur1, couleur2]
        self.__style__ = style
        self.__type__ = typeObj

        # Verifier cohérence du profit avec le prix d'achat et le prix de vente
        if balance == prixVente - prixAchat:
            self.__balance__ = balance

        else:
            print("Erreur de comptabilité")
            self.__balance__ = prixVente - prixAchat

        # Initialiser DIY:
        if estDIY == "Yes":
            self.__estDIY__ = True
        else:
            self.__estDIY__ = False


class Armoire:
    def __init__(self, dataframe: pd.DataFrame):
        """Initialisateur de la classe Armoire"""
        self.__listeVetements__ = self.remplirArmoire(dataframe)

    def remplirArmoire(self, dataframe: pd.DataFrame) -> List:
        # Initialiser inventaire:
        inventaire = []

        # Transformer chaque vêtement dans dataframe en objet Vetement
        for _, row in dataframe.iterrows():
            # Créer vêtements:
            vetementObj = Vetement(
                nom=row['Name'],
                estDIY=row['DIY'],
                prixAchat=row['Buy_Price'],
                prixVente=row['Sell_Price'],
                balance=row['Balance'],
                couleur1=row['Color 1'],
                couleur2=row['Color 2'],
                style=row['Style'],
                typeObj=row['Type']
            )

            # Ajouter objet vêtement à l'inventaire
            inventaire.append(vetementObj)

        return inventaire

    def calculerValeurTotale(self) -> int:
        # Initialiser valeur totale:
        valeur_totale = 0

        # Ajouter valeur de chaque vêtement à la valeur totale:
        for vetementObj in self.__listeVetements__:
            valeur_totale += vetementObj.__prixVente__

        return valeur_totale

    def ajouterVetement(self, vetementObj: Vetement) -> NoReturn:
        self.__listeVetements__.append(vetementObj)

    def enleverVetement(self, vetementNom: str, vetementType: str) -> NoReturn:
        # Initialiser registres des vêtements à enlever:
        registre = []

        # Chercher tout les objets vêtements portant le nom specifié, et enregistrer leur position dans l'inventaire:
        for i in range(len(self.__listeVetements__)):
            vetementObj = self.__listeVetements__[i]

            # Vérifier si le vêtement doit être enlevé:
            if vetementObj.__nom__ == vetementNom and vetementObj.__type__ == vetementType:
                registre.append(i)

        # Enlever les vêtement retenus dans le registre:
        self.__listeVetements__ = [
            vetement
            for i, vetement in enumerate(self.__listeVetements__)
            if i not in set(registre)
        ]

    def obtenirNombreDIY(self) -> int:
        # Initialiser compteur d'objet DIY:
        compteur = 0

        # Identifier les vêtements fait à la main
        for vetementObj in self.__listeVetements__:
            # Si le vêtement est fait à la main, alors __estDIY__ = True
            if vetementObj.__estDIY__:
                compteur += 1

        return compteur

    def filtrerParTypeEtCouleur(self, typeObj: str, couleur: str) -> List:
        # Initialiser liste filtrée:
        listeFiltre = []

        # Identifier tout les objets Vetement du type et couleur specifié:
        for vetementObj in self.__listeVetements__:

            # Verifier si le vêtement doit être retenu:
            if vetementObj.__type__ == typeObj and couleur in vetementObj.__couleurs__:
                listeFiltre.append(vetementObj)

        return listeFiltre

    def creerHabitParStyle(self, style: str) -> Tuple[Vetement, Vetement, Vetement]:
        # Créer les repertoires bas, hauts, et chaussures correspondant au style:
        listeBas = [
            vetementObj for vetementObj in self.__listeVetements__
            if vetementObj.__type__ == 'Bottom' and vetementObj.__style__ == style
        ]
        listeHauts = [
            vetementObj for vetementObj in self.__listeVetements__
            if vetementObj.__type__ == 'Top' and vetementObj.__style__ == style
        ]
        listeChaussures = [
            vetementObj for vetementObj in self.__listeVetements__
            if vetementObj.__type__ == 'Shoe' and vetementObj.__style__ == style
        ]

        # Choisir un objet aléatoire de chaque liste:
        bas = random.choice(listeBas)
        haut = random.choice(listeHauts)
        chaussures = random.choice(listeChaussures)


        # Retourner l'habit créer:
        return bas, haut, chaussures

from consts import *
import pandas as pd
from typing import List, NoReturn, Tuple


def lireDonnees(cheminHauts: str, cheminBas: str, cheminChaussures: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    # Lire donnees:
    hautsDf = pd.read_csv(cheminHauts)
    basDf = pd.read_csv(cheminBas)
    chaussuresDf = pd.read_csv(cheminChaussures)

    # Enleve donnees des items pas a vendre:
    hautsDf = hautsDf[hautsDf['Buy'] != "NFS"]
    hautsDf['Buy'] = hautsDf['Buy'].astype(int)

    basDf = basDf[basDf['Buy'] != "NFS"]
    basDf['Buy'] = basDf['Buy'].astype(int)

    chaussuresDf = chaussuresDf[chaussuresDf['Buy'] != "NFS"]
    chaussuresDf['Buy'] = chaussuresDf['Buy'].astype(int)

    return hautsDf, basDf, chaussuresDf


def filtrerColonnes(dataframe: pd.DataFrame, colonnesAGarder: List[str]) -> pd.DataFrame:
    # Filter le dataframe pour juste garder les colonnes spécifiées dans colonnesAGarder
    dataframeFiltre = dataframe[colonnesAGarder]

    return dataframeFiltre


def renommerColonne(dataframe: pd.DataFrame, vieuxNom: str, nouveauNom: str) -> pd.DataFrame:
    # Renommer la colonne nommée vieuxNom en nouveauNom
    dataframeRenomme = dataframe.rename(columns={vieuxNom: nouveauNom})

    return dataframeRenomme


def enleverDoublons(dataframe: pd.DataFrame) -> pd.DataFrame:
    #Enlever les lignes doublées du dataframe, rechiffrer l'index du dataframe
    dataframeSansDoublons = dataframe.drop_duplicates(ignore_index=True)

    return dataframeSansDoublons


def ajouterColonneType(dataframe: pd.DataFrame, colType: str) -> pd.DataFrame:
    # Copier la dataframe donnee
    dataframeAvecType = dataframe.copy()

    # Ajouter une colonne nommée "Type" avec la valeur par défaut colType
    dataframeAvecType['Type'] = colType

    return dataframeAvecType


def ajouterColonneBalance(dataframe: pd.DataFrame) -> pd.DataFrame:
    # Copier la dataframe donnee
    dataframeAvecProfit = dataframe.copy()

    # Calculer la colonne balance à partir des colonnes Buy_Price et Sell_Price
    # Balance = Buy_Price - Sell_Price
    dataframeAvecProfit['Balance'] = dataframeAvecProfit['Sell_Price'] - dataframeAvecProfit['Buy_Price']

    return dataframeAvecProfit


def pretraiterDataframe(dataframe: pd.DataFrame, objType: str) -> pd.DataFrame:
    # Exécuter les fonctions pour prétraiter le dataframe
    # 1 - Filtrer le dataframe pour juste garder les colonnes COLONNES_IMPORTANTES
    dataframe = filtrerColonnes(dataframe, COLONNES_IMPORTANTES)

    # 2 - renommer colonne "Buy" à "Buy_Price"
    dataframe = renommerColonne(dataframe, vieuxNom = "Buy", nouveauNom = "Buy_Price")

    # 3 - renommer colonne "Sell" à "Sell_Price"
    dataframe = renommerColonne(dataframe, vieuxNom="Sell", nouveauNom="Sell_Price")

    # 4 - Enlever les doublons dans le dataframe
    dataframe = enleverDoublons(dataframe)

    # 5 - Ajouter une colonne type avec la valeur par defaut objType
    dataframe = ajouterColonneType(dataframe, colType=objType)

    # 6 - Ajouter la colonne profit
    dataframe = ajouterColonneBalance(dataframe)

    return dataframe


def mergerDataframes(listeDataframes: List[pd.DataFrame]) -> pd.DataFrame:
    # Merger tous les dataframe dans la liste listeDataframes en un seul, sans les indices
    # -- Initialiser la nouvelle dataframe
    dataframeMerge = pd.DataFrame(columns=listeDataframes[0].columns)

    # -- Merger toutes les dataframes donnees:
    for i in range(len(listeDataframes)):
        dataframeMerge = pd.concat([dataframeMerge, listeDataframes[i]])

    # Enlever les indices:
    dataframeMerge.reset_index(drop=True, inplace=True)

    return dataframeMerge


def sauvegarderDataframe(dataframe: pd.DataFrame, nomFichier: str) -> NoReturn:
    # Sauvegarder le dataframe dans le fichier nomFichier, sans les indices
    dataframe.to_csv(nomFichier, index=False)


if __name__ == "__main__":
    # Lecture des données
    hautsDf, basDf, chaussuresDf = lireDonnees(CHEMIN_DF_HAUTS, CHEMIN_DF_BAS, CHEMIN_DF_CHAUSSURES)

    # Prétraitement des dataframes
    hautsDf      = pretraiterDataframe(hautsDf, NOM_TYPE_HAUT)
    basDf        = pretraiterDataframe(basDf, NOM_TYPE_BAS)
    chaussuresDf = pretraiterDataframe(chaussuresDf, NOM_TYPE_CHAUSSURES)

    # Création du dataframe complet
    dataframeComplet = mergerDataframes([hautsDf, basDf, chaussuresDf])

    # Sauvegarde du dataframe
    sauvegarderDataframe(dataframeComplet, CHEMIN_DF_COMPLET)
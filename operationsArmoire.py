import pandas as pd
from consts import *
from armoire import *

if __name__ == "__main__":
    # 1. Lire le dataframe de la partie 1 contenu dans CHEMIN_DF_COMPLET
    dataframe = pd.read_csv(CHEMIN_DF_COMPLET)

    # 2. Créer un objet armoire à partir du dataframe
    armoire = Armoire(dataframe)

    # 3. Créer un nouveau haut
    nouveauHaut = Vetement(
        nom='T-Shirt Vans x NatGeo',
        estDIY="No",
        prixAchat=999,
        prixVente=10000,
        balance=0,
        couleur1="Black",
        couleur2="Yellow",
        style="Cool",
        typeObj="Top"
    )

    # 4. Ajouter le nouveau haut à armoire
    armoire.ajouterVetement(nouveauHaut)

    # 5. Enlever le bas avec le nom "animal-stripes skirt"
    armoire.enleverVetement(vetementNom="animal-stripes skirt", vetementType="Bottom")

    # 6. Afficher la valeur totale de l'armoire
    valeurTotale = armoire.calculerValeurTotale()
    print(f"La valeur totale de l'armoire est: {valeurTotale}\n")

    # 7. Afficher le nom de toutes les chaussures de couleur 'Blue'
    # -- Filtrer l'armoire
    chaussuresBleues = armoire.filtrerParTypeEtCouleur(typeObj='Shoe', couleur="Blue")
    # -- Afficher le nom de chaussures bleue:
    for chaussure in chaussuresBleues:
        print(chaussure.__nom__)

    # 8. Afficher le nombre de vêtements qui sont DIY
    compteurDIY = armoire.obtenirNombreDIY()
    print(f"Il y a {compteurDIY} vêtements DIY.\n")

    # 9. Générer un habit avec le style 'Cool'
    # -- Générer habit
    habitCool = armoire.creerHabitParStyle(style="Cool")
    # -- Afficher habit
    print(
        f"Habit Cool: \n"
        f"Haut: {habitCool[0].__nom__}\n"
        f"Bas: {habitCool[1].__nom__}\n"
        f"Chaussure: {habitCool[2].__nom__}\n"
    )

    # 10. Générer un habit avec le style 'Cute'
    # -- Générer habit
    habitCute = armoire.creerHabitParStyle(style="Cute")
    # -- Afficher habit
    print(
        f"Habit Cute: \n"
        f"Haut: {habitCute[0].__nom__}\n"
        f"Bas: {habitCute[1].__nom__}\n"
        f"Chaussure: {habitCute[2].__nom__}\n"
    )

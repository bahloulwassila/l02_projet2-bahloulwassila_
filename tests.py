from armoire import *
import pandas as pd

# CREER UNE ARMOIRE TEST
TEST_DF = pd.DataFrame({
    'Name': ['Haut A', 'Haut B', 'Haut C', 'Bas X', 'Bas Y', 'Bas Z', 'Shoes 1', 'Shoes 2', 'Shoes 3'],
    'DIY': ['Yes', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes'],
    'Buy_Price': [10, 20, 30, 11, 22, 33, 1, 2, 3],
    'Sell_Price': [9, 19, 29, 10, 21, 32, 0, 1, 2],
    'Balance': [-1]*9,
    'Color 1': ['Blanc', 'Rose', 'Violet', 'Jaune', 'Bleu', 'Violet', 'Jaune', 'Noir', 'Vert'],
    'Color 2': ['Noir', 'Violet', 'Rouge', 'Orange', 'Vert', 'Rose', 'Rouge', 'Blanc', 'Indigo'],
    'Style': ['Cool', 'Moche', 'Vieux', 'Jeune', 'Cool', 'Moche', 'Vieux', 'Jeune', 'Cool'],
    'Type': ['Top', 'Top', 'Top', 'Bottom', 'Bottom', 'Bottom', 'Shoe', 'Shoe', 'Shoe']
}
)
# Tester la fonction remplirArmoire de la classe Armoire
def testRemplirArmoire():
    # Essayer de remplir l'armoire:
    armoireTest = Armoire(dataframe=TEST_DF)

    # Si l'armoire comporte 9 vêtements, le test est réussi
    if len(armoireTest.__listeVetements__) == 9:
        print("RemplirArmoire: test réussi")

    else:
        print("RemplirArmoire: test échoué")


# Tester la fonction calculerValeurTotale de la classe Armoire
def testCalculerValeurTotale():
    # Initialiser l'armoire:
    armoireTest = Armoire(dataframe=TEST_DF)

    # Calculer valeur totale
    valeur_totale = armoireTest.calculerValeurTotale()

    if valeur_totale == 123:
        print("CalculerValeurTotale: test réussi")
    else:
        print("CalculerValeurTotale: test échoué")


# Tester la fonction ajouterVetement de la classe Armoire
def testAjouterVetement():
    # Initialiser l'armoire:
    armoireTest = Armoire(dataframe=TEST_DF)

    # Créer nouveau bas:
    BasGreekFreak = Vetement(
        nom='Short Nike x GreekFreak',
        estDIY="No",
        prixAchat=6666,
        prixVente=9999,
        balance=3333,
        couleur1="Noir",
        couleur2="VertMilwaukee",
        style="Cool",
        typeObj="Bas"
    )

    # Ajouter a l'armoire
    armoireTest.ajouterVetement(vetementObj=BasGreekFreak)

    # L'armoire test a 9 vêtements de base. Si le vêtement a correctement été ajouté, alors il y en a maintenant 10.
    if len(armoireTest.__listeVetements__) == 10:
        print("AjouterVetement: test réussi")

    else:
        print("AjouterVetement: test échoué")


# Tester la fonction enleverVetement de la classe Armoire
def testEnleverVetement():
    # Initialiser l'armoire:
    armoireTest = Armoire(dataframe=TEST_DF)

    # Essayons d'enlever le Haut 1:
    armoireTest.enleverVetement(vetementNom='Haut A', vetementType='Top')

    # L'armoire test a 9 vêtements de base. Si le vêtement a correctement été enlevé, alors il y en a maintenant 8.
    if len(armoireTest.__listeVetements__) == 8:
        print("EnleverVetement: test réussi")

    else:
        print("EnleverVetement: test échoué")


# Tester la fonction obtenirNombreDIY de la classe Armoire
def testObtenirNombreDIY():
    # Initialiser l'armoire:
    armoireTest = Armoire(dataframe=TEST_DF)

    # Obtenir nombre DIY:
    nombre_DIY = armoireTest.obtenirNombreDIY()

    # L'armoire test a 3 vêtements DIY de base.
    if nombre_DIY == 3:
        print("ObtenirNombreDIY: test réussi")

    else:
        print("ObtenirNombreDIY: test échoué")



# Tester la fonction filtrerParTypeEtCouleur de la classe Armoire
def testFiltrerParTypeEtCouleur():
    # Initialiser l'armoire:
    armoireTest = Armoire(dataframe=TEST_DF)

    # Obtenir liste filtré:
    listeHautsViolet = armoireTest.filtrerParTypeEtCouleur(typeObj='Top', couleur='Violet')

    # L'armoire test a 2 hauts violet de base.
    if len(listeHautsViolet) == 2:
        print("FiltrerParTypeEtCouleur: test réussi")
    else:
        print("FiltrerParTypeEtCouleur: test échoué")


# Tester la fonction creerHabitParStyle de la classe Armoire
def testCreerHabitParStyle():
    # Initialiser l'armoire:
    armoireTest = Armoire(dataframe=TEST_DF)

    # Obtenir habit Cool
    habitCool = armoireTest.creerHabitParStyle(style='Cool')
    basCool, hautCool, shoesCool = habitCool

    # Il n'y a qu'une option Cool par type d'habit, verifier donc qu'elles ont été choisies.
    if hautCool.__nom__ == 'Haut A' and basCool.__nom__ == 'Bas Y' and shoesCool.__nom__ == 'Shoes 3':
        print("CreerHabitParStyle: test réussi")
    else:
        print("CreerHabitParStyle: test échoué")



if __name__ == "__main__":
    # Exécuter les tests et afficher les résultats
    testRemplirArmoire()
    testCalculerValeurTotale()
    testAjouterVetement()
    testEnleverVetement()
    testObtenirNombreDIY()
    testFiltrerParTypeEtCouleur()
    testCreerHabitParStyle()



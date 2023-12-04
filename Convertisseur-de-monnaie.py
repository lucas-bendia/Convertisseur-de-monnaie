from forex_python.converter import CurrencyRates
import datetime

cr = CurrencyRates()

montant = int(input("Veuillez entrer le montant que vous souhaitez convertir : "))

de_devise = input("Veuillez entrer le code de la devise à convertir : ").upper()

à_devise = input("Veuillez entrer le code de la devise à convertir en : ").upper()

print("Vous convertissez", montant, de_devise, "en", à_devise,".")

résultat = cr.convert(de_devise, à_devise, montant)

print("Le taux converti est :", résultat)

# Sauvegarder les détails de la conversion dans un fichier
with open('historique_des_conversions.txt', 'a') as f:
    f.write(f"{datetime.datetime.now()}: Converti {montant} {de_devise} en {à_devise}. Le taux converti est : {résultat}\n")
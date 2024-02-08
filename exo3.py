# TODO : Calculer la distance que chaque rocher lancé par les catapultes peut atteindre en utilisant la formule de la portée d'un projectile.

import math
G=9.81
vitesse_initiale=float(input("Entrez la vitesse initiale (en m/s) :"))
angle_lancement=float(input(" Entrez l'angle de lancement (en degres) :"))
D=(vitesse_initiale**2)*(math.sin(2*math.radians(angle_lancement)))/G
D=f"{D:.2f}"
print(f" La distance parcourue par le projectile est de {D} metres.")

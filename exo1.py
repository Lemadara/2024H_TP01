# TODO : Créer un script Python pour saisir et publier des découvertes planétaires sur un blog intergalactique.

planete = input("Entrez le nom de la planete exploree: ")
date_visite = input("Entrez la date de votre visite (JJ/MM/AAAA):")
description = input(" Decrivez la planete:")
finalDescription = f"Titre : Decouverte de {planete}\nDate : {date_visite}\nDescription : {description}"
print(" Votre exploration a ete ajoutee au Journal des Astres !\n-------------------------------\n"+finalDescription)

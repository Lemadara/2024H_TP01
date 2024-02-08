# TODO : Écrire un programme qui demande le pourcentage de charge actuel de la batterie de la Batmobile, calcule le temps restant en minutes en fonction de ce pourcentage, et affiche le résultat au format "XXhYYmin". Assurer la gestion des pourcentages valides et des messages d'erreur appropriés.

niveau_charge=int(input("Entrez le pourcentage de charge actuel de la batterie de la Batmobile :")) 

# continuation a condition que le input est bien entre 0% et 100%; control d'erreur d'entrée
if 0<=niveau_charge<=100:

    # les conditions A, B, C pour chaque cas de figures des pourcentages
    A= niveau_charge>=51
    B= (not A) and (niveau_charge >=6)
    C= (not A) and (not B)

    battTimeLeft = (niveau_charge-50)*1+45*2+5*5 if A else (niveau_charge-5)*2+5*5 if B else niveau_charge*5 # calcul du temps restant en minutes selon l'ensemble des % restants
   
     
    if A:
        battTimeleft= (niveau_charge-50)*1+45*2+5*5
    elif B:
        battTimeleft= (niveau_charge-5)*2+5*5
    else:
        battTimeleft=niveau_charge*5
    # i dont know why - it gets confused in my mind by thinking about it that way - instead of just thinking like in one line
    

    # conversion en heures et minutes
    h,m=battTimeLeft//60,battTimeLeft-(battTimeLeft//60)*60 

    # affichage du temps final
    m=f"{m:02}"
    print(f" Temps restant : {h}h{m}min") 
 
# quoi faire pour un chemain imprevue d'input; prevue mais on peut rien faire avec l'input dans ce program ou on veut pas travailler avec de base c'est pas logique d'entré cela/ autre option faire une boucle infini pour redemander, input, ou quitter selon lentrée de lutilisateur
else:
    print(" Erreur : niveau de charge invalide.")
# TP2 fait le 16 septembre 2022
# Fait par Enoch Immanuel wang
# on import le module random
import random
# on crée une variable qui s'appellera NOMBRE, cette variable a pour but de choisir un nombre random entre 1-100, donc cela serait le nombre de l'ordinateur qu'on devra essayer de deviner
def jeuxdevinette():
    NOMBRE = random.randint(1, 100)
    # on cée une autre variable qui s'appellera "le_nombre_de_essai" et le nombre d'essai est le nombre de fois que la personne va faire un guess et le nombre d'essaie augmente a chaque fois
    le_nombre_de_essai = 0
    # ainsi, on créera une autre variable pour le nombre d'essaie maxi, on aurait pu le faire de facon que a chaque fois il prend un guess le nombre de chance restante diminue mais je préferes de cette facon si, donc l'orsque la personne aura utiliser dix guess, le jeux sera terminer
    maxessai = 10
    # on crée une variable qui s'appelle try comme ca à chaque fois que le joueur esseyera une autre fois, on ajoute tryy au nombre d'essaie, on fait cela continuellement
    tryy = 1
    # on crée une variable qui s'appelle x qui sera le nombre choisi par le joueur, donc on fera un input avec ceci et il entra le nombre choisi pour le guess
    x = 0
    # on va créer une variable qui s'applle retryy afin que la peersonne écris o/n
    retryy = ""
    # jouer = vrai
    jouer = True
    # print la phrase de bienvenue
    print('Bonjour, le but du jeux est de deviner le nombre choisi entre 1-100 par le systeme en le moin de coup possible, vous avez 10 chance au max')
    # on crée un while jouer, tous se retrouve dedans, tant qu'il est vrai
    while jouer:
        # tant que x est inégale au nombre de l'ordi et que le nombre d'essaie est plus que dix
        while x != NOMBRE and le_nombre_de_essai <= maxessai:
            # x = a un integer que le jouer va entrez dans intput
            x = int(input("Entrez votre nombre:"))
            # si le nombre entrez est plus grand
            if int(x) > NOMBRE:
                # on additionne un essaie
                le_nombre_de_essai = le_nombre_de_essai + tryy
                # print que le nombre est plus grand
                print("Votre nombre est plus grand que celui de l'ordi!")
                # print le nombre d'essaie du joueur
                print(" Vous êtes à", le_nombre_de_essai, "nombres d'essais")
            # si x < que le nombre de l,ordi
            elif int(x) < NOMBRE:
                # on additione 1 au nombre d'essaie a chaque fois il essaie.
                le_nombre_de_essai = le_nombre_de_essai + tryy
                # print le nombre plus petit
                print("Votre nombre est plus petit que celui de l'ordi!")
                # le nombre d,essaie il est rendu
                print(" Vous êtes à", le_nombre_de_essai, "nombres d'essais")
                # autre
            else:
                # print message gagnant
                print('Vous avez deviner le nombre, lol vous êtes trop fort!')
                # print nombre d'essais utiliser
                print("Vous avez utiliser", le_nombre_de_essai, "nombre d'essaie")

                # vouler vous reéssayer de jouer
                retryy = input("ah Nice vous avez gagné, vous êtes très bon, get bad, voulez vous recommencer o/n!:")
            if retryy == "n":
                print('byebye')
                jouer = False
            elif retryy == "o":
                jeuxdevinette()

            if le_nombre_de_essai >= maxessai and x != NOMBRE:
                print('le nombre est', NOMBRE)
                retryy = input(
                    "ah rip vous avez utiliser tous vos essaie, vous êtes pas très bon, get good, voulez vous recommencer o/n!:")


jeuxdevinette()

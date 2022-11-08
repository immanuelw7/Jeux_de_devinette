# TP2 fait le 16 septembre 2022
# Fait par Enoch Immanuel wang Ching Chong
# on import le module random
import random

maxnumb = '100'
minnumb = '1'
nombresus = -1

def nombedemaxmin():
    global maxnumb
    global minnumb
    minnumb = input('choissez le premier nombre(la limite) que vous voulez jouer sur:')
    maxnumb = input('choisissez le deuxième nombre(la limite) sur laquelle vous voulez jouer sur:')

    if int(maxnumb) < int(minnumb):
        maxnumb, minnumb = minnumb, maxnumb

    nombresecret()

def nombresecret():
    global nombresus
    nombresus = random.randint(int(minnumb), int(maxnumb))
    return nombresus


def jeuxdevinette():
    global nombresus

    choix = input('veut tu choisir les bornes du jeux? oui/non:')
    if choix == 'oui':
        nombedemaxmin()
    if choix == 'non':
        nombresus = random.randint(1,100)

    #nbr essaie = 0
    le_nombre_de_essai = 0
    #maximum d'essaie est 10
    maxessai = 10
    #essaie = 10
    tryy = 1
    x = 0
    # on va créer une variable qui s'applle retryy afin que la peersonne écris o/n
    retryy = ""
    # jouer = vrai
    jouer = True

    # print la phrase de bienvenue
    print('Bonjour, le but du jeux est de deviner le nombre choisi entre', minnumb, 'et', maxnumb, ' par le systeme en le moin de coup possible, vous avez 10 chance au max')
    # on crée un while jouer, tous se retrouve dedans, tant qu'il est vrai
    while jouer:
        # tant que x est inégale au nombre de l'ordi et que le nombre d'essaie est plus que dix
        while x != nombresus and le_nombre_de_essai <= maxessai:
            # x = a un integer que le jouer va entrez dans intput
            x = int(input("Entrez votre nombre:"))
            # si le nombre entrez est plus grand
            if int(x) > nombresus:
                # on additionne un essaie
                le_nombre_de_essai += 1
                # print que le nombre est plus grand
                print("Votre nombre est plus grand que celui de l'ordi!")
                # print le nombre d'essaie du joueur
                print(" Vous êtes à", le_nombre_de_essai, "nombres d'essais")
            # si x < que le nombre de l,ordi
            elif int(x) < nombresus:
                # on additione 1 au nombre d'essaie a chaque fois il essaie.
                le_nombre_de_essai += 1
                # print le nombre plus petit
                print("Votre nombre est plus petit que celui de l'ordi!")
                # le nombre d,essaie il est rendu
                print(" Vous êtes à", le_nombre_de_essai, "nombres d'essais")
                # autre
            else:
                le_nombre_de_essai += 1
                # print message gagnant
                print('Vous avez deviner le nombre, lol vous êtes trop fort!')
                # print nombre d'essais utiliser
                print("Vous avez utiliser", le_nombre_de_essai, "nombre d'essaie")

                # vouler vous reéssayer de jouer
                retryy = input("ah Nice vous avez gagné, vous êtes très bon, get bad, voulez vous recommencer o/n!:")
                #si il ne veut pas
            if retryy == "n":
                #bybye
                print('byebye')
                #on end le code
                jouer = False
                #si il veut recommencer
            elif retryy == "o":
                jouer = False
                #on recommence le jeux
                jeuxdevinette()
            # si il utilise tous ses essais
            if le_nombre_de_essai >= maxessai and x != nombresus:
                #on dit le nombre secret
                print('le nombre est', nombresus)
                retryy = input("ah rip vous avez utiliser tous vos essaie, vous êtes pas très bon, get good, voulez vous recommencer o/n!:")


jeuxdevinette()

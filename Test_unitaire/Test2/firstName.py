def greet_user(name = None):
    firstname = name if name else input('Veuillez entrer votre prénom :')
# Vérifier si le prénom saisi n'est pas vide

    if firstname:
        print (f'Merci {firstname} !')

    else:
        print( f'Vous n avez pas saisi un prénom valide')

greet_user()

import hashlib

def ajouter_entree_auth(user, mdp, fichier='auth.txt'):
    mdp_hash = hashlib.sha256(mdp.encode('utf-8')).hexdigest()
    with open(fichier, 'a') as f:
        f.write(f"{user}:{mdp_hash}\n")
    print(f"Entrée ajoutée pour l'utilisateur '{user}'.")

if __name__ == "__main__":
    utilisateur = input("Nom d'utilisateur : ")
    mot_de_passe = input("Mot de passe : ")
    ajouter_entree_auth(utilisateur, mot_de_passe)
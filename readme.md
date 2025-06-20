## Server FastAPI pour la génération de description d'images (EN et FR)
### Utilisation 
Ce projet sert de base pour la génération d'ALT pour des images.  
Il utilise un modèle de génération de texte pré-entraîné pour créer des descriptions d'images en anglais. Il utilise également un modèle de traduction pour traduire ces descriptions en français.  
Il utilise les modèles suivants :
- [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) pour la génération de texte à partir d'images.
- [Helsinki-NLP/opus-mt-en-fr](https://huggingface.co/Helsinki-NLP/opus-mt-en-fr) pour la traduction de l'anglais vers le français.

### Installation
Pour installer et exécuter le serveur FastAPI, suivez les étapes suivantes :  
1. Cloner le dépôt git  
2. Se placer dans le dossier du projet  
3. Créer un environnement virtuel Python :  
    ```bash
    python -m venv venv
    ```
    (Windows)
4. Activer l'environnement virtuel :  
    ```bash
    venv\Scripts\activate.bat
    ```
    (Windows)
5. Installer les dépendances :  
    ```bash
    pip install -r requirements.txt
    ```

### Lancement du serveur
Pour lancer le serveur FastAPI, utilisez la commande suivante :
```bash
uvicorn app:app --reload
```

### Utilisation de l'API
- Créez un utilisateur avec :  
  ```bash
  python app/auth/ajout_user.py
  ```
  Renseignez un nom d'utilisateur et un mot de passe.
- Ensuite, vous pouvez utiliser l'API pour générer des descriptions d'images en utilisant une basic auth avec le nom d'utilisateur et le mot de passe que vous avez créés.
- Vous trouverez la documentation de l'API à l'adresse suivante (une fois le serveur FastAPI lancé) : [http://localhost:8000/docs](http://localhost:8000/docs)

### Bon à savoir
- Le serveur tourne en local sur le port 8000 par défaut. Vous pouvez changer le port en modifiant la commande de lancement du serveur.
- Pour arrêter le serveur, utilisez `CTRL + C` dans le terminal où il est exécuté.
- Utilisation de la puissance de calcul de la machine sur laquelle le serveur est exécuté. Si le temps de réponse est long, c'est normal si vous l'exécutez sur votre ordinateur personnel. À titre personnel, en utilisant un ordinateur portable "gaming" de milieu de gamme, le temps de réponse est d'environ 5 secondes.

### Pourquoi ce projet ?
L'idée de ce projet est de permettre de générer des descriptions automatiquement pour des images, ce qui peut être utile pour améliorer l'accessibilité des contenus visuels sur le web mais aussi pour le référencement.  
C'est une tâche qui est souvent négligée mais qui est particulièrement importante pour les personnes malvoyantes ou pour les moteurs de recherche qui indexent les images.  
Le but est donc de permettre d'automatiser cette tâche en utilisant des modèles de génération de texte et de traduction pré-entraînés.  
Pourquoi en anglais et en français ?  
Parce que le projet est français mais pour un bon référencement, il est important de proposer du contenu en anglais aussi.

### Modularité
J'ai essayé de rendre les modèles qu'on utilise pour la génération de texte et de traduction le plus modulaires possible. Mais je ne suis pas un développeur Python, donc si vous avez des suggestions pour améliorer le code, n'hésitez pas à me contacter ou à faire une PR sur le dépôt GitHub.  
Si des modèles open source différents vous semblent plus pertinents, n'hésitez pas à les utiliser et à me faire un retour. Je suis preneur de toute amélioration ou suggestion pour ce projet !

### Open source
Ce projet est totalement open source, pas de licence particulière, vous pouvez l'utiliser comme bon vous semble. Tous vos retours sont les bienvenus, que ce soit pour améliorer le code, la documentation ou pour proposer de nouveaux modèles à utiliser.  
J'ai essayé de rendre le code le plus simple possible, c'est pour cela qu'il n'y a pas de base de données à proprement parler mais uniquement un fichier `auth.txt` pour stocker les utilisateurs et mots de passe.

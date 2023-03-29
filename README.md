## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).



#### Cloner le repository

- `git clone https://github.com/idarousse21/Projet_13.git`
- `cd Projet_13`

#### Créer l'environnement virtuel

##### Mac et Linux
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

##### Windows
- `python -m venv env`
- `env\Scripts\activate`
- `pip install -r requirements.txt`

#### Exécuter le site

- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `flake8`

#### Tests unitaires

- `pytest`

#### Base de données

- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from profiles_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`


## Déploiement
Le déployment de l'application se fera en créant une image Docker, cette image est ensuite utilisée pour créer des conteneurs Docker, qui est une instance exécutant l'application. Nous effectuerons par la suite un deployment sur la plateforme Heroku et enfin nous utilisera le service d'intégration continue de CircleCI pour créer un pipeline qui automatisera le processus de test, de conteneurisation et de deployment.

### Prérequis

#### Installation et conteneurisation de Docker

  - Installer <a href="https://www.docker.com/">Docker</a>
  - Créer un compte Docker et connectez-vous

##### Construire l'image Docker et le pousser dans le registre des conteneurs DockerHub en ouvrant votre invite de commande et en tapant ces commandes:
  - docker login -u <username-docker>
  - docker build -t lettings .
  - docker docker tag lettings:latest <username-docker>/lettings:latest
  - docker push <username-docker>/lettings:latest

##### Vous pouvez aussi récuperer l'image Docker:
  - docker pull <username-docker>/lettings:latest

##### Lancer le site localement en utilisant l'image Docker
  - docker run -it -p 8000:8000 <username-docker>/lettings
  - Acceder ensuite a la page sur `http://localhost:8000`

#### Configuration et deployement sur Heroku

  - Créer un compte sur <a href="https://signup.heroku.com/">Heroku</a>
  - Connecter vous et créer une nouvelle application avec comme nom "lettings"

##### Créer des variable d'environnement dans l'application

  - SECRET_KEY: "fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"
  - HEROKU_APP_NAME: "lettings"

#### Configuration et lancement de la pipeline CircleCi

  - Créer un compte <a href="https://circleci.com/signup/">CircleCI</a> via votre compte github
  - Aller sur le projet correspondant

##### Créer des variable d'environnement dans le projet

  - API_KEY_HEROKU: "API-KEY-HEROKU"
  - DOCKER_USERNAME: "DOCKER-USERNAME"
  - DOCKER_PASSWORD: "DOCKER-PASSWORD"
  - HEROKU_LOGIN: "HEROKU6LOGIN"
  - SENTRY_DSN: *Voir la partie sur sentry

#### Journalisation sur Sentry

  - Créer un compte <a href="https://sentry.io/signup/">Sentry</a> via votre compte github
  - Créer un projet
  - Récupérer le DSN du projet


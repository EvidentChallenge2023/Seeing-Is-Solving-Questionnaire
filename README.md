# EvidentChallenge2023 

Bienvenue à tous!

---

Welcome to all!

# Questionnaire repository

Ceci est le dépôt de code pour les questions de l'édition 2023. Plusieurs outils sont nécéssaire afin d'être en mesure de répondre aux questions. Nous vous invitons à bien lire les sections suivantes afin de compléter votre installation.

**Aucun support de la part de Evident Scientific sera fournit pour des problèmes d'installation d'outils. Les membres de l'organisation du Evident Challenge ne consulterons pas et ne commenterons pas les merge request/pull request d'aucune équipe afin d'être équitable envers tous. Et cela même si vous les ajoutez comme reviewer. Il est autorisé de créer et d'utiliser les merge request/pull request entre les membres de votre équipe. Veuillez consulter attentivement la date et l'heure limite afin d'effectuer le commit final sur Github classroom. Après ce délais, aucune équipe de pourra envoyer du nouveau code dans le repository de leur assignement.**

---

This is the code repository for the 2023 edition questions. Several tools are needed in order to be able to answer the questions. Please read the following sections to complete your installation.

**No support from Evident Scientific will be provided for tool installation issues. The members of the Evident Challenge organization will not consult or comment on any team’s merge request/pull request to be fair to all. And this even if you add them as a reviewer. It is allowed to create and use merge request/pull request between your team members. Please carefully check the cut-off date and time to perform the final commit on Github classroom. After this time, no team will be allowed to send new code in the repository of their assignment.**

## Procédure d'installation des outils nécéssaires pour répondre aux questions - How to install the necessary tools to answer the questions

### Git for Windows

L'outil git est nécéssaire afin d'aller récupérer le code sur le dépôt github.
\*Pour l'installer : https://git-scm.com/downloads

---

The git tool is needed to get the code from the github repository.
\*To install: https://git-scm.com/downloads

### VSCode

\*Installer VSCode : https://code.visualstudio.com/download

---

\*Install VSCode: https://code.visualstudio.com/download

### Python 3.11.1

*Installer Python : https://www.python.org/downloads/
*Installer l'extension de python dans VSCode : https://marketplace.visualstudio.com/items?itemName=ms-python.python

Comment utiliser Python dans VSCode: https://code.visualstudio.com/docs/python/python-tutorial

---

*Install Python: https://www.python.org/downloads/
*Install the python extension in VSCode: https://marketplace.visualstudio.com/items?itemName=ms-python.python

How to use Python in VSCode: https://code.visualstudio.com/docs/python/python-tutorial

### PIP

PIP est un gestionnaire de paquet pour Python et sera nécéssaire afin d'aller chercher les dépendences que le projet nécéssite.

Installer PIP =>

Windows : https://www.dataquest.io/blog/install-pip-windows/

macOS : https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

Tel que le tutoriel pour Windows le démontre, ne pas oublier d'aller ajouter Python à vos variables d'environnement si cela n'est aps déjà fait.

---

PIP is a package manager for Python and will be needed in order to fetch the dependencies that the project needs.

\*Install PIP =>

Windows : https://www.dataquest.io/blog/install-pip-windows/

macOS : https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

As Windows tutorial shows, don’t forget to add Python to your environment variables if it’s not already done.

### Jupyter Notebook

\*Installer l'extension de Jupyter dans VSCode : https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

Comment débuter avec Jupyter Notebook dans VSCode : https://code.visualstudio.com/learn/educators/notebooks

---

\*Install the Jupyter extension in VSCode: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

Getting Started with Jupyter Notebook in VSCode: https://code.visualstudio.com/learn/educators/notebooks

### Exécuter un notebook truc - Running a notebook tip

Si vous êtes sur Windows, VSCode vous indiquera probablement qu'il doit installer ipkernel, dite oui.

---

If you are on Windows, VSCode will probably tell you that it should install ipkernel, say yes.

### Auto pep-8

Pep8 est la norme d'écriture de fichier python. Il existe un plugin dans VSCode vous permettant d'utiliser Pep8. Nous vous encourageons à l'installer.

---

Pep8 is the python file writing standard. There is a plugin in VSCode that allows you to use Pep8. We encourage you to install it.

## Comment démarrer le projet - How to start the project

### Installer les dépendences et démarrer l'environnement virtuel - Install dependencies and start virtual environment

Utiliser le script suivant =>

&nbsp;&nbsp;&nbsp;&nbsp; Windows : ActiverEnvironnementVirtuel.bat


**_ATTENTION : Si vous obtenez une erreur de droit style "UnauthorizedAccess" lorsque vous tenter de démarrer l'environnement virtuel, tenter d'utiliser un invite de commande au lieu du powershell._**

---

Use the following script =>

&nbsp;&nbsp;&nbsp;&nbsp; Windows : ActiverEnvironnementVirtuel.bat


**_CAUTION: If you get a "UnauthorizedAccess" style error when trying to start the virtual environment, try using a command prompt instead of the powershell._**

### Arrêter l'environnement virtuel - Stop virtual environment

Utiliser le script suivant =>

&nbsp;&nbsp;&nbsp;&nbsp; Window : DésactiverEnvironnementVirtuel.bat

---

Use the following script =>

&nbsp;&nbsp;&nbsp;&nbsp; Window : DésactiverEnvironnementVirtuel.bat


### Autres commandes utiles - Other useful commands\_\_

Pour rouler le test coverage (L'environnement virtuel doit être lancé d'abord):

    coverage run -m --source=src pytest -v

---

Pour rouler les test (L'environnement virtuel doit être lancé d'abord):

    pytest

**_ATTENTION : Si vous obtenez une erreur, tenter d'utiliser un invite de commande (cmd) au lieu du powershell dans VSCode._**

---

Pour rouler pylint (L'environnement virtuel doit être lancé d'abord):

    pycodestyle --config={LE PATH DE VOTRE REPO}\pycodestyle.py {LE PATH DE VOTRE REPO}\sources

Pour info sur les normes PEP8 : https://www.python.org/dev/peps/pep-0008/

---

To run the test coverage (The virtual environment must be launched first):

    coverage run -m --source=src pytest -v

---

To run the tests (The virtual environment must be launched first):

    pytest

**_CAUTION: If you get an error, try using a command prompt(cmd) instead of the powershell into VSCode._**

---

To run pylint (The virtual environment must be launched first):

    pycodestyle --config={LE PATH DE VOTRE REPO}\pycodestyle.py {LE PATH DE VOTRE REPO}\sources

For PEP8 info: https://www.python.org/dev/peps/pep-0008/

## Trucs - Tips :

- Utiliser des path relatif pour les imports
- Toujours nommer vos classe de test et module de test avec le préfix "test\_" sinon l'engin de tests ne découvrira pas vos tests.
- Ajouter un fichier vide **init**.py dans TOUS les nouveau dossier où vous ajouter des classe de code (cela indique que ca devient un module et permet ainsi de faire fonctionner les imports - si un import ne fonctionne pas, validez que vous n'avez pas oublié d'ajouter ce fichier vide)
- Démarrer l'environnement virtuel à l'aide du script dédié à cet effet avant de rouler les commande pour éxécuter les test et le linter sur votre poste.

---

- Use relative path for imports
- Always name your test class and module with the prefix "test\_" otherwise the test machine will not discover your tests.
- Add an empty **init**.py file to ALL new folders where you add code classes (this indicates that this becomes a module and this allows to run the imports - if an import does not work, validate that you have not forgotten to add this empty file)
- Start the virtual environment using the dedicated script before rolling the commands to run the tests and linter on your computer.

# Débuter le défi - Start the challenge

Pour débuter le défi, nous vous invitons à consulter le notebook suivant :

[ÉnoncéPrincipal-MainStatement notebook](sources/challengepart2/EnoncePrincipal_MainStatement.ipynb)

**Bon défi à tous, amusez-vous bien!!!**

---

To start the challenge, we invite you to consult the following notebook:

[ÉnoncéPrincipal-MainStatement notebook](sources/challengepart2/EnoncePrincipal_MainStatement.ipynb)

**Good challenge to all, have fun!!!**


# Comment la compétition se déroulera?

- La compétition sera ouverte le 3 juin au matin, dès que le courriel sera envoyé à tous les participants et prendra fin le 17 juin à 23h59. À partir de 23h59, il ne sera plus possible de soumettre les réponses sur la copie de votre questionnaire Github Classroom. 
- Après ce délai, les branches **"main"** seront clonées par les correcteurs afin d'effectuer la correction. 
- **----------ATTENTION : Aucune autre branche ne sera corrigée. ----------**
- L'annonce du classement préliminaire sera faite le 30 juillet 2023 au plus tard. Les candidats au classement seront alors contactés afin de remettre la documentation nécessaire afin de récupérer le prix (preuve de fréquentation scolaire et autres documents vous seront exigés). Ces derniers auront un délai de 7 jours pour transmettre les documents requis. Après ce délai, la prochaine équipe au classement sera contactée. La première équipe à fournir les documents nécessaires sera déterminée équipe gagnante. 
- Le dévoilement du ou des gagnants officiels sera fait le 31 août 2023 au plus tard. Une cérémonie de remise de prix sera organisée dans le mois suivant la détermination du gagnant officiel.
- La compétition pourra être fait seul ou en équipe avec un maximum de 3 personnes par équipe. Il sera de votre responsabilité de créer vos équipes sur Github Classroom. Le premier à aller se connecter à la Classroom aura l'opportunité de créer l'équipe. Il devra alors transmettre à ses coéquipiers le nom de l'équipe afin que ces derniers joignent la bonne équipe à leur première connexion à la Classroom.
- Création d'équipe par erreur => si vous créer une équipe par erreur, nous vous invitons à nous contacter à cette adresse courriel afin que nous puissions supprimer l'équipe : **challenge@evidentscientific.com**
- Pendant la compétition, afin d'être équitable envers tous les participants, aucune question par courriel sur la compétition, que ce soit en lien avec l'installation des outils ou le contenu des questions ne sera répondues. Si une question comporte une erreur, nous vous invitons à répondre à la question du mieux que vous le pouvez et à nous indiquer sur le notebook de la question quelle est l'erreur et comment vous avez fait pour régler le problème. Nous effectuerons une correction équitable envers toutes les équipes en considérant les erreurs dans le questionnaire après coups. Évidemment nous souhaitons que le questionnaire ne comporte pas d'erreur dans le meilleur des mondes possibles. Mais rien n'est parfait, particulièrement en ingénierie, nous le savons!
- Tricherie => toute trace de tricherie conduira à une expulsion de la compétition. 
- Voici ce qui est considéré comme une trace de tricherie :
    - Un extrait de code identique se retrouvant sur 2 copies différentes.
    - Un extrait de code copié sur internet directement.
    - Un extrait de code provenant de ChatGpt directement.
    - Une personne ou une équipe ayant participée avec 2 comptes github différents.
    - Une personne qui est actuellement employée ou stagiaire chez Evident.
    - Obtenir un aide privilégié d’une personne travaillant chez Evident.
    - Une collaboration évidente entre 2 équipes, même si le code n'est pas identique, nous serons en mesure de constater si des solutions ont été échangés d'une équipe à une autre.  
    - Ne pas respecter les critères d'admission à la compétition qui se situe dans les Termes et Conditions acceptés lors de l'inscription.
    - La publication sur internet des réponses. Si une des équipes partage de façon publique les réponses au questionnaire, cette équipe sera expulsée et les membres ne pourront plus jamais participer à un défi Evident. La ou les questions touchées seront alors corrigées différemment selon la gravité de la publication afin d'être équitable envers tous les participants.

- Voici ce qui n'est pas considéré comme de la tricherie:
    - Utiliser une librairie python.
    - Être plusieurs membres d'une même équipe à contribuer à répondre à une seule et même question du défi.
    - Consulter de la documentation sur le NDT.
    - Consulter des brevets publiés relié au domaine du NDT.
    - Consulter les SDK existantes dans le domaine du NDT.
    - Réutiliser du code python dont vous êtes l'auteur que vous possédiez déjà dans le cadre d'un autre projet en python.
    - Utiliser un linter.
    - Utiliser des outils de validation d'architecture tel que SonarQube par exemple. 
    - Écrire des tests automatisés validant vos réponses.
    - Utiliser des outils de calculs tel que Maple ou WolframAlpha.
    - Utiliser des outils de validation tel que Postman ou Postwomen. 
    - Poser des questions à ChatGpt.

Nous vous souhaitons un très bon défi, amusez-vous bien 😊

***

# How will the competition proceed?

- The competition will open on the morning of June 3rd, as soon as the email is sent to all participants and will end on June 17th at 11:59 PM. After 11:59 PM, it will no longer be possible to submit answers on your Github Classroom questionnaire copy.
- After this deadline, the **"main"** branches will be cloned by the graders for evaluation.
- **----------ATTENTION: No other branches will be evaluated. ----------**
- The preliminary ranking announcement will be made no later than July 30th, 2023. The ranking candidates will be contacted to provide the necessary documentation to claim the prize (proof of school attendance and other required documents). They will have a 7-day period to submit the required documents. After this period, the next team in the ranking will be contacted. The first team to provide the necessary documents will be determined as the winning team.
- The official winner(s) announcement will be made no later than August 31st, 2023. An award ceremony will be organized within the month following the determination of the official winner.
- The competition can be done individually or in a team with a maximum of 3 team members. It will be your responsibility to create your teams on Github Classroom. The first person to log in to the Classroom will have the opportunity to create the team. They will then need to inform their teammates of the team name so that they can join the correct team upon their first login to the Classroom.
- Team Creation Mistake: If you accidentally create a team, please contact us at this email address so that we can delete the team: **challenge@evidentscientific.com**.
- During the competition, to ensure fairness to all participants, no questions regarding the competition, whether related to tool installation or question content, will be answered via email. If a question contains an error, we encourage you to answer the question to the best of your ability and indicate on the question's notebook what the error is and how you resolved it. We will ensure fair evaluation for all teams by considering the errors in the questionnaire afterwards. Of course, we aim for the questionnaire to be error-free in an ideal world, but nothing is perfect, especially in engineering, as we know!
- Cheating: Any evidence of cheating will result in disqualification from the competition.
- Here's what is considered evidence of cheating:
    - An identical code snippet found in 2 different copies.
    - Code snippet directly copied from the internet.
    - Code snippet directly taken from ChatGpt.
    - An individual or team participating with 2 different GitHub accounts.
    - An individual who is currently employed or an intern at Evident.
    - Receiving privileged assistance from a person working at Evident.
    - Clear collaboration between 2 teams, even if the code is not identical. We will be able to determine if solutions have been exchanged between teams.
    - Failure to comply with the admission criteria for the competition, as stated in the accepted Terms and Conditions during registration.
    - Publishing the answers on the internet. If any team publicly shares the questionnaire answers, that team will be disqualified, and its members will never be able to participate in an Evident challenge again. The affected question(s) will be evaluated differently based on the severity of the publication to ensure fairness to all participants.

- Here's what is not considered cheating:
    - Using a Python library.
    - Multiple team members contributing to answering a single question of the challenge.
    - Consulting documentation on NDT
    - Consulting published patents related to the field of NDT.
    - Consulting existing SDKs in the field of NDT.
    - Reusing Python code authored by yourself that you already possess as part of another Python project.
    - Using a linter.
    - Using architecture validation tools such as SonarQube, for example.
    - Writing automated tests to validate your answers.
    - Using calculation tools such as Maple or WolframAlpha.
    - Using validation tools such as Postman or Postwomen.
    - Asking questions to ChatGpt.

We wish you a great challenge, have fun! 😊


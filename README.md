
# EvidentChallenge2023 organization on Github

Ceci est le'organisation qui a été créée pour l'édition 2023 du Evident Challenge. 

Bienvenue à tous!

***

This is the organisation that was created for the 2023 edition of the Evident Challenge. 

Welcome to all!

# Questionnaire repository

Ceci est le dépôt de code pour les questions de l'édition 2023. Plusieurs outils sont nécéssaire afin d'être en mesure de répondre aux questions. Nous vous invitons à bien lire les sections suivantes afin de compléter votre installation. 

**Aucun support de la part de Evident Scientific sera fournit pour des problèmes d'installation d'outils. Les membres de l'organisation du Evident Challenge ne consulterons pas et ne commenterons pas les merge request/pull request d'aucune équipe afin d'être équitable envers tous. Et cela même si vous les ajoutez comme reviewer. Il est autorisé de créer et d'utiliser les merge request/pull request entre les membres de votre équipe. Veuillez consulter attentivement la date et l'heure limite afin d'effectuer le commit final sur Github classroom. Après ce délais, aucune équipe de pourra envoyer du nouveau code dans le repository de leur assignement.**

***

This is the code repository for the 2023 edition questions. Several tools are needed in order to be able to answer the questions. Please read the following sections to complete your installation. 

**No support from Evident Scientific will be provided for tool installation issues. The members of the Evident Challenge organization will not consult or comment on any team’s merge request/pull request to be fair to all. And this even if you add them as a reviewer. It is allowed to create and use merge request/pull request between your team members. Please carefully check the cut-off date and time to perform the final commit on Github classroom. After this time, no team will be allowed to send new code in the repository of their assignment.**


## Procédure d'installation des outils nécéssaires pour répondre aux questions - How to install the necessary tools to answer the questions

### Git for Windows

L'outil git est nécéssaire afin d'aller récupérer le code sur le dépôt github.
\*Pour l'installer : https://git-scm.com/downloads

***

The git tool is needed to get the code from the github repository.
\*To install: https://git-scm.com/downloads


### VSCode

\*Installer VSCode : https://code.visualstudio.com/download

***

\*Install VSCode: https://code.visualstudio.com/download

### Python 3.11.1

*Installer Python : https://www.python.org/downloads/
*Installer l'extension de python dans VSCode : https://marketplace.visualstudio.com/items?itemName=ms-python.python

Comment utiliser Python dans VSCode: https://code.visualstudio.com/docs/python/python-tutorial

***

*Install Python: https://www.python.org/downloads/
*Install the python extension in VSCode: https://marketplace.visualstudio.com/items?itemName=ms-python.python

How to use Python in VSCode: https://code.visualstudio.com/docs/python/python-tutorial

### PIP

PIP est un gestionnaire de paquet pour Python et sera nécéssaire afin d'Aller chercher les dépendences que le projet nécéssite.

Installer PIP => 

Windows : https://www.dataquest.io/blog/install-pip-windows/

macOS : https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

Tel que le tutoriel pour Windows le démontre, ne pas oublier d'aller ajouter Python à vos variables d'environnement si cela n'est aps déjà fait.

***

PIP is a package manager for Python and will be needed in order to Fetch the dependencies that the project needs.

\*Install PIP => 

Windows : https://www.dataquest.io/blog/install-pip-windows/

macOS : https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

As Windows tutorial shows, don’t forget to add Python to your environment variables if it’s not already done.

### Jupyter Notebook

\*Installer l'extension de Jupyter dans VSCode : https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

Comment débuter avec Jupyter Notebook dans VSCode : https://code.visualstudio.com/learn/educators/notebooks

***

\*Install the Jupyter extension in VSCode: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

Getting Started with Jupyter Notebook in VSCode: https://code.visualstudio.com/learn/educators/notebooks

### Exécuter un notebook truc - Running a notebook tip

Si vous êtes sur Windows, VSCode vous indiquera probablement qu'il doit installer ipkernel, dite oui.

***

If you are on Windows, VSCode will probably tell you that it should install ipkernel, say yes.

### Auto pep-8

Pep8 est la norme d'écriture de fichier python. Il existe un plugin dans VSCode vous permettant d'utiliser Pep8. Nous vous encourageons à l'installer.

***

Pep8 is the python file writing standard. There is a plugin in VSCode that allows you to use Pep8. We encourage you to install it.

## Comment démarrer le projet - How to start the project

### Installer les dépendences et démarrer l'environnement virtuel - Install dependencies and start virtual environment

Utiliser le script suivant =>

&nbsp;&nbsp;&nbsp;&nbsp; Windows : ActiverEnvironnementVirtuel.bat

&nbsp;&nbsp;&nbsp;&nbsp; MAC : TODO

**_ATTENTION : Si vous obtenez une erreur de droit style "UnauthorizedAccess" lorsque vous tenter de démarrer l'environnement virtuel, tenter d'utiliser un invite de commande au lieu du powershell._**

***

Use the following script =>

&nbsp;&nbsp;&nbsp;&nbsp; Windows : ActiverEnvironnementVirtuel.bat

&nbsp;&nbsp;&nbsp;&nbsp; MAC : TODO

**_CAUTION: If you get a "UnauthorizedAccess" style error when trying to start the virtual environment, try using a command prompt instead of the powershell._**


### Arrêter l'environnement virtuel - Stop virtual environment

Utiliser le script suivant =>

&nbsp;&nbsp;&nbsp;&nbsp; Window : DésactiverEnvironnementVirtuel.bat

&nbsp;&nbsp;&nbsp;&nbsp; MAC : TODO

***

Use the following script =>

&nbsp;&nbsp;&nbsp;&nbsp; Window : DésactiverEnvironnementVirtuel.bat

&nbsp;&nbsp;&nbsp;&nbsp; MAC : TODO


### Autres commandes utiles - Other useful commands__

Pour rouler le test coverage (L'environnement virtuel doit être lancé d'abord):

    coverage run -m --source=src pytest -v

---

Pour rouler les test (L'environnement virtuel doit être lancé d'abord):

    pytest

---

Pour rouler pylint (L'environnement virtuel doit être lancé d'abord):

    pycodestyle --first --exclude='*/exported_*' --ignore=E501,W504 {LE PATH DE VOTRE REPO}\src

Pour info sur les normes PEP8 : https://www.python.org/dev/peps/pep-0008/


***


To run the test coverage (The virtual environment must be launched first):

    coverage run -m --source=src pytest -v

---

To run the tests (The virtual environment must be launched first):

    pytest

---

To run pylint (The virtual environment must be launched first):

    pycodestyle --first --exclude='*/exportd_*' --ignore=E501,W504 {YOUR REPO PATH}\src


For PEP8 info: https://www.python.org/dev/peps/pep-0008/


## Trucs - Tips :
  
* Utiliser des path relatif pour les imports
* Toujours nommer vos classe de test et module de test avec le préfix "test_" sinon l'engin de tests ne découvrira pas vos tests.
* Ajouter un fichier vide __init__.py dans TOUS les nouveau dossier où vous ajouter des classe de code (cela indique que ca devient un module et permet ainsi de faire fonctionner les imports - si un import ne fonctionne pas, validez que vous n'avez pas oublié d'ajouter ce fichier vide) 
* Démarrer l'environnement virtuel à l'aide du script dédié à cet effet avant de rouler les commande pour éxécuter les test et le linter sur votre poste.

***

* Use relative path for imports
* Always name your test class and module with the prefix "test_" otherwise the test machine will not discover your tests.
* Add an empty __init__.py file to ALL new folders where you add code classes (this indicates that this becomes a module and this allows to run the imports - if an import does not work, validate that you have not forgotten to add this empty file) 
* Start the virtual environment using the dedicated script before rolling the commands to run the tests and linter on your computer.


# Débuter le défit - Start the challenge

Pour débuter le défit, nous vous invitons à consulter le notebook suivant : 

[ÉnoncéPrincipal_MainStatement.ipynb](source/questions/CommentPrincipal_MainStatement.ipynb)

**Bon défit à tous, amusez-vous bien!!!**

***

To start the challenge, we invite you to consult the following notebook: 

[ÉnoncéPrincipal_MainStatement.ipynb](source/questions/CommentPrincipal_MainStatement.ipynb)

**Good challenge to all, have fun!!!**

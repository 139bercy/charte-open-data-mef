# Contributions

Tout d'abord, merci de prendre de votre temps pour contribuer !

Toutes les contributions sont bienvenues :

- Ajoutez une étoile au projet,
- Parlez-en autour de vous,
- Faites référence au projet dans vos propres travaux.

## J'ai une question

Avant de soumettre quoi que ce soit, consultez d'abord la documentation.

Si vous ne trouvez pas ce que vous cherchez :

- Vérifiez que vous utilisez une version à jour,
- Vérifiez qu'une [issue](https://github.com/139bercy/charte-open-data-mef/issues) n'a pas déjà été ouverte sur le sujet
- Si oui, n'hésitez pas à y ajouter un commentaire,
- Si non, ouvrez une [issue](https://github.com/139bercy/charte-open-data-mef/issues) ou contactez-nous !

Vous pouvez également signaler les autres projets qui l'ont mieux résolu et qui pourraient servir d'inspiration.

## Je propose des changements

### Installation

Vérifiez que vous avez bien une version de Python à jour et que toutes les dépendances sont bien installées (cf. README.md)

### Commits

Les commits suivent la spécification [conventional commits](https://www.conventionalcommits.org/fr/v1.0.0/).

**Attention** : Les montées de version restent une tâche à la charge de l'administrateur.

### Pre-commit hooks

Pour garantir un formatage uniforme, un certain nombre de `pre-commits` hooks ont été ajoutés :

- `mdformat` : contrôle du formatage des fichiers _markdown_
- `commitizen` : contrôle du formatage des commits au format pré-cité

Pour les installer :

```
$ pre-commit install --install-hooks && pre-commit autoupdate
```

### Périmètre de la gestion sémantique de version

Un utilitaire de gestion sémantique de version a été ajouté, qui ne prend pour objet que le contenu textuel dans le dossier `./src`, soit les politiques d'usage de la plateforme.

Les fonctionnalités permettant de générer des documents à des formats divers (`pdf`, `docx`, etc.), autres ajout de code de traitement, pré-commits, etc, ne rentrent pas dans ce cadre.

À des fins documentaires, vous trouverez la liste des commandes dans le fichier `Makefile`.

**Attention** : La gestion sémantique de version reste une tâche d'administration.

## Pull request

1. Clonez le dépôt et créez une nouvelle branche :

```bash
   git clone https://github.com/139bercy/charte-open-data-mef.git
   cd charte-open-data-mef
   git checkout -b [nom_de_la_branche]
```

2. Installez les dépendances :

[commande_pour_installer_les_dépendances]

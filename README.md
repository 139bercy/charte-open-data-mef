# Politique d'usage de la plateforme Open Data des ministères économiques et financiers `data.economie.gouv.fr`

## Présentation

La présente charte est destinée aux agents du ministère de l'Économie et des Finances chargés de la publication et de la maintenance des données ouvertes au sein de leur direction et à ce titre amenés à contribuer à la plateforme [data.economie.gouv.fr](https://data.economie.gouv.fr).

Ce document établit un cadre de référence stratégique pour la publication et la gestion des données ouvertes au sein des ministères économiques et financiers français.

Il définit une gouvernance structurée centrée sur la mission d'Administration ministérielle des données, des algorithmes et des codes sources (AMDAC) tout en précisant les normes techniques de qualité (formats ouverts, l'encodage UTF-8 ou le référentiel de métadonnées).

L'objectif fondamental reste d'assurer la fiabilité et l'interopérabilité des ressources partagées sur la plateforme ministérielle de manière à garantir que les données publiées soient automatiquement et correctement intégrées au portail national.

En responsabilisant les producteurs de données sur la clarté des métadonnées et la sécurité des accès, ce document vise à renforcer la transparence publique et la confiance des réutilisateurs.

## Usage

Le document est téléchargeable [ici](https://github.com/139bercy/charte-open-data-mef/releases) au format `PDF` ainsi qu'au format `DOCX`.

La version de la `release` en cours est sur la branche `main`, la version de travail en cours de modification est sur la branche `develop`.

Les fichiers sources de chaque branche sont consultables dans le dossier [`src`](https://github.com/139bercy/charte-open-data-mef/tree/main/src/main.md).

## Choix du format

Les fichiers de travail sont au format [Markdown](https://docs.framasoft.org/fr/grav/markdown.html).

Ce format de fichier ouvert, à la syntaxe simple, permet d'effectuer l'essentiel des actions de traitement de texte tout en restant léger et compatible avec les systèmes de contrôle de version.

Le travail collaboratif en est rendu d'autant plus aisé.

En outre, sa portabilité permet un export simple vers des formats `HTML`, `PDF` ou `DOCX` ainsi qu'une intégration facilitée vers des outils en ligne de gestion documentaire ou un site Web dédié.

## Édition (mode développeur)

### Installation

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Copier le template d'environnement :

```bash
$ cp .env.example .env
```

Éditer le fichier `.env` pour y ajouter votre token GitHub :

```text
DATA_ECO_POLICIES_TOKEN=ghp_votre_token_ici
```

### Exports DOCX et PDF

La gestion et le formatage des fichiers nécessitent une version Python à jour.

**Attention** : Cette fonctionnalité nécessite :

- [Pandoc](https://pandoc.org/)
- [tmlgr (LaTeX)](https://tug.org/texlive/tlmgr.html)
- [Marianne](https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-de-l-identite-de-l-etat/typographie/)

```
$ make release
```

Le fichier est disponible en sortie dans le dossier `build` aux formats suivants :

- `data-economie-politique-d-usage-<version>-main.pdf`
- `data-economie-politique-d-usage-<version>-main.docx`

### Générer une table des matières

```
$ make toc
```

## Contribuer

Se reporter à la documentation sise dans le dossier `.github` à la racine du dépôt.

## Contact

- [contact.dataeconomie@finances.gouv.fr](mailto:contact.dataeconomie@finances.gouv.fr)

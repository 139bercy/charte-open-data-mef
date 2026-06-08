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

## Résumé

### Avant publication

- Contacter la mission AMDAC pour obtenir un compte (agents MEF uniquement)
- Valider l'absence de données sensibles ou confidentielles
- En cas de doute, saisir le DPO ou contacter la mission AMDAC
- **Rappel** : tout jeu publié en public est automatiquement moissonné par data.gouv.fr

### Format des fichiers

- Formats autorisés : `CSV`, `JSON`, `XML`, `TXT` (formats ouverts)
- Formats à éviter : `docx`, `xlsx`, `PDF`, `zip`, `rar`
- Encodage : **UTF-8** obligatoire
- CSV : séparateur **point-virgule** (`;`), jamais de virgule
- Header en première ligne, sans espaces (privilégier `_`)
- Pas de colonnes/lignes vides, pas de cellules fusionnées

### Normalisation des valeurs

- Dates : **ISO 8601** → `AAAA-MM-JJ HH:MM:SS`
- Cellules vides : remplacer par `NA`, `NC` ou `NULL` (documenter dans les métadonnées)
- Unités de mesure : cohérentes et documentées
- Pas de formules dans les cellules (types simples uniquement)
- Pas de séparateurs de milliers

### Identifiant et nom du jeu de données

- Définir avant publication, **jamais modifier après mise en production**
- Utiliser le **tiret court** (`-`), pas le tiret bas
- Préfixe commun pour un même ensemble de datasets
- Environnements : `test-<nom>`, `preprod-<nom>`, `<nom>` = production
- Accès restreint : `<env>-restreint-<nom>`, `<env>-interne-<nom>`
- Utiliser la même nomenclature d'une année sur l'autre pour faciliter la recherche
- Exemple : `plf-2025-depenses-comptes-speciaux`

### Versionnement (SemVer 2.0.0) à indiquer dans le titre

- Format : `<majeure>.<mineure>.<patch>`
- Majeure = changement de schéma structurel
- Mineure = ajout de colonnes ou de données compatibles
- Patch = correction d'erreurs
- Documenter les changements : `CHANGELOG.txt` en pièce jointe ou en description
- Activer `Mettre à jour la date après un traitement des données` dans les infos du jeu
- Exemple : `Prix des contrôles techniques - v2.0.3`

### Jeux millésimés

- Privilégier **un seul jeu avec historique** + champ `année`
- Ne créer un jeu par année que si le schéma change radicalement
- Pour les fichiers > 5 Go : garder `n` années en base, années précédentes en pièce jointe

### Métadonnées obligatoires

| Champ                     | Détail                                 |
| ------------------------- | -------------------------------------- |
| **Titre**                 | 5 à 10 mots, explicite                 |
| **Description**           | 300 à 500 caractères                   |
| **Producteur**            | Direction responsable                  |
| **Contact**               | Email fonctionnel (BALF privilégiée)   |
| **Mots-clés**             | 3 à 7 termes                           |
| **Licence**               | Par défaut `Licence Ouverte v2.0`      |
| **Fréquence**             | Hebdo / mensuel / trimestriel / annuel |
| **Couverture spatiale**   | Zone géographique                      |
| **Couverture temporelle** | Période couverte                       |
| **Thématique**            | Catégorie taxonomie portail            |

### Import

- Importer en **source** (pas en pièce jointe) → accès API, export, exploration
- Onglet `Traitement` : typer chaque champ, définir les facettes
- Limite : **500 colonnes** maximum

______________________________________________________________________

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

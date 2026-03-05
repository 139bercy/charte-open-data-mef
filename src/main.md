# Charte Open Data des ministères économiques et financiers

## Table

- [Charte Open Data des ministères économiques et financiers](#charte-open-data-des-minist%C3%A8res-%C3%A9conomiques-et-financiers)
  - [Table](#table)
  - [Introduction](#introduction)
    - [Objectif du document](#objectif-du-document)
    - [Importance de la normalisation](#importance-de-la-normalisation)
  - [Gouvernance de l'Open Data](#gouvernance-de-lopen-data)
    - [Au sein des ministères économiques et financiers](#au-sein-des-minist%C3%A8res-%C3%A9conomiques-et-financiers)
    - [Articulation entre **data.economie.gouv.fr** et **data.gouv.fr**](#articulation-entre-dataeconomiegouvfr-et-datagouvfr)
    - [Principes FAIR, Open Data by default, Open Data by design](#principes-fair-open-data-by-default-open-data-by-design)
    - [Formation des agents](#formation-des-agents)
  - [Politique d'utilisation de la plateforme](#politique-dutilisation-de-la-plateforme)
    - [Accès et autorisation](#acc%C3%A8s-et-autorisation)
    - [Responsabilité des producteurs de données](#responsabilit%C3%A9-des-producteurs-de-donn%C3%A9es)
  - [Format et structure des fichiers de données](#format-et-structure-des-fichiers-de-donn%C3%A9es)
    - [Format des fichiers](#format-des-fichiers)
    - [Séparateurs](#s%C3%A9parateurs)
    - [Normalisation des valeurs](#normalisation-des-valeurs)
    - [Taille des jeux de données](#taille-des-jeux-de-donn%C3%A9es)
    - [Gestion des discussions](#gestion-des-discussions)
  - [Structure des jeux de données](#structure-des-jeux-de-donn%C3%A9es)
    - [Conventions de nommage](#conventions-de-nommage)
    - [Identifiants et noms des jeux de données](#identifiants-et-noms-des-jeux-de-donn%C3%A9es)
    - [Versionnement des jeux de données](#versionnement-des-jeux-de-donn%C3%A9es)
    - [Gestion des sources](#gestion-des-sources)
    - [Jeux de données millésimés](#jeux-de-donn%C3%A9es-mill%C3%A9sim%C3%A9s)
  - [Gestion des métadonnées](#gestion-des-m%C3%A9tadonn%C3%A9es)
    - [Modèle de documentation](#mod%C3%A8le-de-documentation)
    - [Métadonnées requises](#m%C3%A9tadonn%C3%A9es-requises)
    - [Catégories et mots-clés](#cat%C3%A9gories-et-mots-cl%C3%A9s)
    - [Point de contact](#point-de-contact)
  - [Opérations courantes](#op%C3%A9rations-courantes)
    - [Ouverture d'un jeu de données](#ouverture-dun-jeu-de-donn%C3%A9es)
    - [Modification de l'identifiant technique d'un jeu de données](#modification-de-lidentifiant-technique-dun-jeu-de-donn%C3%A9es)
    - [Suppression d'un jeu de données](#suppression-dun-jeu-de-donn%C3%A9es)
    - [Tester un jeu de données en accès restreint](#tester-un-jeu-de-donn%C3%A9es-en-acc%C3%A8s-restreint)
    - [Répondre à une discussion](#r%C3%A9pondre-%C3%A0-une-discussion)
  - [Monitoring](#monitoring)
    - [Suivi du remplissage des métadonnées](#suivi-du-remplissage-des-m%C3%A9tadonn%C3%A9es)
  - [Ressources](#ressources)
    - [Testes juridiques](#testes-juridiques)
    - [Documentation technique](#documentation-technique)
    - [Métadonnées](#m%C3%A9tadonn%C3%A9es)
    - [Acculturation à la donnée](#acculturation-%C3%A0-la-donn%C3%A9e)
  - [Annexe](#annexe)
    - [Conversion d'un fichier Excel en CSV](#conversion-dun-fichier-excel-en-csv)

## Introduction

### Objectif du document

Le présent document vise à établir des directives d'usage claires pour la plateforme Open Data du ministère de l'Économie et des Finances, **data.economie.gouv.fr**.

L'objectif est de fournir aux producteurs de données des directions un cadre de référence pour la publication, la gestion et l'utilisation des jeux de données ministériels.

Ces normes et bonnes pratiques ont pour finalité d'offrir à nos réutilisateurs – internes et externes – une interface cohérente avec nos activités tout en garantissant un certain niveau de qualité.

### Importance de la normalisation

Cet effort de normalisation présente plusieurs avantages :

- **Qualité** : garantir un niveau de pertinence et de fiabilité des données utilisées,
- **Accessibilité** : une plateforme bien structurée et documentée facilite la recherche, la découverte et l'utilisation des données,
- **Interopérabilité** : adopter des standards et des référentiels pour les données ainsi que les métadonnées facilite leur utilisation intégrée,
- **Confiance** : des pratiques transparentes renforcent la confiance des utilisateurs et valorisent notre mission de service public.

## Gouvernance de l'Open Data

### Au sein des ministères économiques et financiers

Dans le cadre de la mise en place d'une politique de la donnée voulue comme ambitieuse, la [circulaire n°6264/SG](https://www.legifrance.gouv.fr/circulaire/id/45162) publiée le 27 avril 2021 crée un nouveau rôle – l'Administrateur ministériel des données, des algorithmes et des codes sources (AMDAC) – chargé de coordonner la circulation, l'ouverture et l'exploitation des données publiques, des algorithmes et des codes sources.

Au niveau ministériel, cette politique est coordonnée par l'AMDAC au sein du Bercy Hub (amd@finances.gouv.fr) et cadrée par la feuille de route de la donnée 2024-2026, co-construite avec les directions tout au long de l'année 2023.

La gouvernance de l'Open Data et la gestion de la plateforme Open Data ministérielle **data.economie.gouv.fr** font, au sein des ministères économiques et financiers, l'objet d'une mission dédiée.

Au sein des directions, l'Administrateur directionnel des données est chargé de la stratégie et de la gouvernance des données, comprenant le plus souvent l'Open Data. Suivant leur structure, l'Open Data peut faire l'objet d'une mission dédiée.

N'hésitez pas à mobiliser ces acteurs pour le cadrage, la réalisation ou le suivi de vos projets data lorsque vous contactez nos équipes.

Un annuaire directionnel des référents Open Data est mis à votre disposition en accès restreint sur la plateforme.

- `interne-restreint-correspondants-open-data-mef`

### Articulation entre **data.economie.gouv.fr** et **data.gouv.fr**

Le site **data.gouv.fr** est le portail national des données publiques ouvertes de l'administration.

La plateforme **data.economie.gouv.fr** est la plateforme des données ouvertes publiées par les ministères économiques et financiers.

Le portail **data.gouv.fr** récupère quotidiennement les données de la plateforme **data.economie.gouv.fr** par voie de moissonnage, rendant ainsi inutile toute opération manuelle de publication sur **data.gouv.fr**.

Le portail **data.gouv.fr** propose une fonctionnalité de discussion. Les équipes Open Data du Bercy Hub sont notamment chargées de ventiler les notifications. Les métiers souhaitant répondre peuvent demander à être rattachés à l'organisation MEFSIN sur **data.gouv.fr** sur demande à **contact.dataeconomie@finances.gouv.fr**

**Attention** : Chaque jeu de données publié et en accès public sur la plateforme **data.economie.gouv.fr** est moissonné et rendu accessible sur le portail **data.gouv.fr**. Il convient donc de ne pas rendre accessible des données de test et/ou des données confidentielles.

### Principes FAIR, Open Data by default, Open Data by design

Les principes FAIR donnent quelques principes d'organisation des données à avoir en mémoire lorsqu'une démarche d'ouverture est entamée :

- **Faciles** à trouver pour les humains et les machines, en fournissant notamment des identifiants uniques et des métadonnées complètes ;
- **Accessibles** : faciliter l'accès au données en favorisant un stockage ergonomique et pérenne ;
- **Interopératbles** : favoriser les échanges entre les SI via des standards et des formats ouverts ;
- **Réutilisables** : décrire précisément les données et définir leurs condtions de réutilisation pour augmenter l'impact des données.

De manière générale, il est recommandé lors des travaux initiaux présidant à la constitution d'un jeu de données d'avoir pour objectif de les ouvrir, une démarche d'**Open Data par défaut** qui est par ailleurs une obligation pour les administrations publiques depuis la promulgation de la Loi pour une république numérique le 7 octobre 2016.

Penser les données ouvertes dès le début de leur cycle de vie permet d'adresser d'emblée les principaux risques

### Formation des agents

Un cycle de formation en quatre modules est proposé à la demande. Les agents métier ayant vocation à publier des données sur la plateforme sont fortement incités à y participer.

- **Module 1** : La fresque de la donnée ouverte
- **Module 2** : Les fondamentaux de l'Open Data
- **Module 3** : La qualité de la donnée
- **Module 4** : La valorisation de la donnée

## Politique d'utilisation de la plateforme

### Accès et autorisation

L'accès à la plateforme **data.economie.gouv.fr** n'est autorisé qu'aux agents habilités des ministères économiques et financiers, après demande auprès de l'administrateur de la plateforme :

- contact.dataeconomie@finances.gouv.fr

La gestion des identités et des accès est effectuée par les administrateurs de la plateforme, qui attribuent les droits appropriés en fonction des responsabilités de chaque utilisateur.

Ceux-ci sont priés de se conformer aux politiques et procédures de sécurité de l'organisation lors de l'accès à la plateforme, notamment :

- les comptes doivent être personnels (pas de boîte à lettres fonctionnelle),
- les comptes ne doivent pas être partagés entre utilisateurs.

### Responsabilité des producteurs de données

Les producteurs de données sont responsables de la qualité et de l'intégrité des jeux de données qu'ils publient sur la plateforme. Ceci inclut la vérification de l'exactitude des données et des métadonnées, leur mise à jour éventuelle ainsi que la résolution rapide des problèmes de qualité signalés par les utilisateurs.

Les producteurs de données sont également tenus de garantir que les jeux de données rendus publics - hors usage restreint - ne contiennent pas d'informations sensibles ou confidentielles : un jeu de données rendu public est moissonné de manière programmatique par plusieurs plateformes, dont la plateforme Open Data **data.gouv.fr**.

Le délégué à la protection des données ministériel pourra être saisi en cas de doute sur la conformité des données publiées.

## Format et structure des fichiers de données

Le document brut ne contiendra ni colonnes ni lignes vides, ni cellules fusionnées, ni couleurs.

La première ligne du fichier sera le *header* contenant les en-têtes des colonnes. Celui-ci ne contiendra pas de cellules vides et doit être composé de chaînes de caractères valides et sans espaces (privilégier le `_`).

**Attention** : Dans les fichiers tabulaires de type `CSV` ou `XLSX`, la première ligne est considérée comme le `header` contenant les en-têtes des colonnes.

La plupart des erreurs constatées impliquant un header manquant sont dues à un formatage inadéquat du fichier source. Ce paramètre peut être modifié lors de l'import d'un fichier en mode "Source".

### Format des fichiers

Le format d'un fichier ainsi que la manière avec laquelle un fichier est structuré, ont une forte influence sur son accessibilité, sa lisibilité et sa réutilisation.

Principes généraux :

- **Encodage** : Les fichiers doivent être encodés au format Unicode `utf-8`,
- **Formats standardisés** : Nous privilégierons les formats standardisés et ouverts tels que `CSV`, `JSON`, `XML`, `TXT`,
- **Formats ouverts** : Nous chercherons à éviter :
  - les formats propriétaires (`docx`, `xlsx`),
  - le format `pdf`, qui est difficilement exploitable programmatiquement,
  - les formats compressés (`zip`, `tar.gz`).

### Séparateurs

Le format CSV (_Comma separated values_, soit valeurs séparées par des virgules) reste le format ouvert plébiscité pour l'affichage de données tabulaires.

Cependant, l'utilisation de la virgule comme séparateur pose de multiples problèmes d'interprétation, notamment parce qu'elle est utilisée en Europe comme séparateur pour les décimales là où le point est utilisé outre-Atlantique.

Afin d'éviter les décalages de colonnes ou la séparation intempestive de valeurs, il reste donc préférable d'utiliser en priorité le point virgule.

### Normalisation des valeurs

- Les noms des champs doivent respecter des conventions de nommage cohérentes (pas de majuscules, séparateurs identiques, etc.),
- Les champs `date` doivent suivre le standard ISO 8601 : `AAAA-MM-JJ HH:MM:SS.CCC`, (ex : `2025-01-01 12:00:00.123`) ;
- Les champs ne doivent pas abriter de formules et s'en tenir à des types simples (entiers, texte, date, flottant, etc.) ;
- Les séparateurs de milliers doivent être évités ;
- La cohérence des unités de mesure doit être assurée et documentée dans le champ lui-même ou en description ;
- Les cellules vides doivent être autant que possible remplacées par une valeur standardisée (`NA`, `NC`, `NULL`), qui doit également être documentée.

### Taille des jeux de données

L'indexation de la plateforme est optimisée pour un affichage par lignes. En conséquence, elle peut supporter en affichage tableau des fichiers faisant plusieurs millions de lignes.

En revanche, le nombre de colonnes est limité à 500 pour un jeu de données, comme le type de certains champs. Certaines opérations peuvent être faites par Opendatasoft au cas par cas, après demande aux administrateurs de la plateforme.

Source : https://userguide.opendatasoft.com/l/en/article/dbukdhmk5a-dataset-limits

De manière générale, il n'est pas recommandé de mettre en production des fichiers ayant un nombre trop important de colonnes, notamment pour des raisons de lisibilité, de maintenance et de traitement. La plateforme indiquera une erreur au-delà du seuil prescrit.

### Gestion des discussions

Les plateformes **data.gouv.fr** et **data.economie.gouv.fr** présentent toutes deux des fonctionnalités de gestion des discussions

## Structure des jeux de données

### Conventions de nommage

> Selon que notre idée est plus ou moins obscure, L’expression la suit, ou moins nette, ou plus pure. Ce que l’on conçoit bien s’énonce clairement, Et les mots pour le dire arrivent aisément. – Boileau, *Art Poétique*

Principes généraux :

- **Clarté et concision** : les noms des jeux de données ou des fichiers joints doivent éviter autant que possible les acronymes ou les abréviations obscures et ne pas faire plus de 170 signes,
- **Noms** : les noms utilisés pour les jeux de données, les titres et les champs doivent respecter autant que possible un vocabulaire commun et demeurer explicites à l'utilisateur non averti
- **Uniformité** : de manière à faciliter l'identification des jeux de données et leur regroupement, une structure de nommage cohérente devra être adoptée pour tous les jeux de données (cf. ci-dessous),
- **Encodage** : les jeux de données seront encodés au format `utf-8`, un format désormais courant, compatible ASCII et devenu un standard facilitant la compatibilité et les performances,
- **Mots-clés** : intégrer des mots-clés dans les noms des jeux de données permet d'améliorer leur référencement : qu'ils disent ce qu'ils font et qu'ils fassent ce qu'ils disent.

### Identifiants et noms des jeux de données

Par *identifiant*, nous entendons *identifiant technique*, soit non seulement l'identifiant unique d'un jeu de données sur **data.economie.gouv.fr**, mais également sur les plateformes qui réutilisent nos jeux de données par voie de moissonnage, comme **data.gouv.fr**.

- il doit être défini avant la publication,
- il ne doit pas contenir de notions techniques propres à la plateforme (ex : `copie`, `< nom du jeu de données >0`)
- il ne doit pas être changé après avoir été mis en production.

Par *nom du jeu de données*, nous entendons la chaîne de caractère identifiant le jeu de données sur la plateforme, soit ce qui est affiché à l'utilisateur, soit sur la page du jeu de données lui-même ou dans le moteur de recherche.

Quelques considérations :

- préférer le **tiret court (1/4 de cadratin)** au **tiret bas** pour les identifiants des jeux de données,
- nommer les identifiants techniques des jeux de données en fonction de leur environnement :
  - `test-<dataset_name>`,
  - `preprod-<dataset_name>`,
- les variables *environnement* à mentionner sont `test`et `preprod`, leur absence désigne la production,
- nommer les identifiants des jeux de données en fonction de leur périmètre de diffusion :
  - `<env>-restreint-<dataset_name>`,
  - `<env>-interne-<dataset_name>`.
- les noms des jeux de données sont écrits autant que possible en français courant,
- les variables _environnement_ et _périmètre de diffusion_ sont notées entre crochets dans les jeux de données.

*Exemple* :

- Identifiant technique : `test-interne-prix-des-carburants-v2`
- Nom du jeu de données : `[Test][Interne] Prix des carburants v2`

Si le jeu de données appartient à un même ensemble, il convient de donner à tous les jeux de données le même préfixe, en restant le plus explicite possible. Exemple :

- `plf-2025-autorisations-de-decouverts-des-comptes-speciaux-non-dotes`
- `plf25-depenses-2025-des-comptes-speciaux-non-dotes`

### Versionnement des jeux de données

De manière à assurer la traçabilité et la cohérence des jeux de données, un numéro de version doit être associé à chaque jeu de données publié sur la plateforme. À cette fin, nous préconisons, en matière de gestion sémantique de version, l'emploi du standard [SemVer 2.0.0](https://semver.org/lang/fr/) :

- `<majeure>.<mineure>.<patch>`.

Les producteurs sont tenus de documenter clairement, soit dans un fichier texte en pièce jointe type `CHANGELOG.txt`, soit en description, les modifications apportées à chaque version des jeux de données, y compris les mises à jour, les corrections d'erreurs et les ajouts de nouvelles données.

Outre la gestion sémantique de version, les mises à jour peuvent être horodatées en activant l'option `Mettre à jour la date après un traitement des données` dans les informations de chaque jeu de données au chemin suivant :

- `Informations > Standard > Informations générales > Afficher la date de modification`

### Gestion des sources

La plateforme **data.economie.gouv.fr** est la plateforme Open Data du ministère de l'Économie et des Finances. À ce titre, elle ne doit contenir que des jeux de données produits par les ministères économiques et financiers.

**Attention** : La plateforme **data.gouv.fr**, qui reprend par moissonnage le contenu de la plateforme **data.economie.gouv.fr**, ne peut pas être une source de données pour **data.economie.gouv.fr**.

### Jeux de données millésimés

Certains jeux de données sont millésimés et publiés annuellement.

Si leur schéma ne change pas, il reste préférable de ne constituer qu'un seul jeu de données contenant l'ensemble des données pour plusieurs années en ajoutant un champ spécifique pour l'année et en documentant les ajouts, Ce qui facilite considérablement les réutilisations et les comparaisons d'une année sur l'autre.

Si la structure des fichiers évolue de manière trop importante pour pouvoir envisager de conserver un historique dans un seul fichier, alors il est possible de créer un jeu de données par année et de créer sur la plateforme une `page` référençant chaque jeu de données et référencée sur chaque jeu de données.

Pour certains fichiers exceptionnellement volumineux (5 Go ou plus), il peut être envisagé de ne garder que `n` années d'historique en mettant les années précédentes en pièce jointe du même jeu de données. Cette pratique est contraire aux standards, mais conforme à la licence accordée avec Opendatasoft.

## Gestion des métadonnées

Les métadonnées sont des "données qui fournissent de nouvelles informations sur d'autres données". À ce titre, elles permettent de contextualiser un jeu de données : les champs dans lesquels apparaissent des termes métier donnent des indications sur le producteur, la fréquence des mises à jour, la licence, etc.

Le module de recherche (raccourci `Ctrl / Cmd + K`) se nourrit des métadonnées pour offrir plus de contexte aux recherches des utilisateurs. Remplir les métadonnées permet également d'étoffer considérablement l'indexation des jeux de données et de renforcer la pertinence du moteur de recherche.

Sur la plateforme ministérielle **data.economie.gouv.fr**, ces métadonnées, à remplir pour chaque jeu de données, se trouvent à plusieurs endroits :

- métadonnées des champs d'un document tabulaire, qui apparaissent dans l'onglet `Traitement` du backoffice,
- métadonnées `standard`, `admin` et `DCAT` de l'onglet `Informations` du backoffice.

**Attention** : Le remplissage des métadonnées répond aux mêmes critères de concision et de clarté que ceux décrits ci-dessus.

### Modèle de documentation

Le modèle de documentation [Datasheets for Datasets](https://arxiv.org/pdf/1803.09010) cadre la rédaction des métadonnées en fournissant une liste de questions utiles, sur la création des jeux de données, leur composition, leur collecte, les traitements opérés, ainsi que les modalités de diffusion ou de maintenance.

### Métadonnées requises

Les métadonnées à remplir en premier lieu sont les suivantes. Sur la plateforme, elles sont étalées sur trois catégories qui sont autant d'onglets : _standard_, _admin_, _DCAT_.

**Métadonnées descriptives**

- **le titre** : concis, il permet aux utilisateurs de comprendre le contenu du jeu de données (5 à 10 mots),
- **la description** : brève description du contenu et de l’objectif du jeu de données (300 à 500 caractères),
- **le producteur** : indique la direction responsable de la production du jeu de données (cf. note *Point de contact* ci-dessous),
- **contact** : coordonnées du responsable des données ou l'adresse email fonctionnelle du bureau responsable,
- **les mots-clés** : 3 à 7 termes, (cf. encadré ci-dessous)
- **Thème** (recommandé) : catégories thématiques selon la taxonomie du portail

**Métadonnées d'administation**

- **la date de publication** : renseigne sur la temporalité des données,
- **la licence** : fixe les conditions d'utilisation et de réutilisation des données. Par défaut `Licence Ouverte v2.0 (Etalab)`,
- **la date de mise à jour** : elle peut être réglée automatiquement à la mise à jour des données ou des métadonnées,
- **les références** : ou tout lien vers des sources externes ou documents connexes utiles.

**Géospatiales et temporelles**

- **la fréquence de mise à jour** : renseigne sur la périodicité des mises à jour (ex : hebdomadaire, mensuelle)
- **la couverture spatiale** : détermine la zone géographique couverte par le jeu de données (ex : France entière)
- **la couverture temporelle** : détaille la période temporelle couverte par le jeu de données (ex : 2012-2023)

### Catégories et mots-clés

Les mots-clés permettent d'optimiser les recherches faites sur la plateforme ou le référencement des jeux de données sur les moteurs de recherche en donnant des éléments de contexte supplémentaires. Les experts SEO recommandent d'ajouter aux pages entre 1 et 5 mots-clés.

Un bon mot-clé doit être recherché par les internautes et ne doit pas être trop concurrentiel.

Déterminez le sujet principal du jeu de données, le service qu'il peut offrir, sa thématique ou encore une question qui pourrait être facilement posée par son audience cible. Identifiez ensuite les mots-clés les plus pertinents.

Des outils comme [KeywordTool](https://keywordtool.io/fr) peuvent être utilisés pour faire les premières analyses sémantiques.

### Point de contact

La question peut se poser de renseigner comme `email de contact` l'adresse d'une boîte à lettres fonctionnelle (BALF) plutôt qu'un email en `finances.gouv.fr`.

Le point de contact personnel a un avantage : il permet de savoir qui est nommément responsable d’un jeu de données et savoir précisément à qui s’adresser.

Inconvénient : il est rarement mis à jour en cas de départ et devient alors obsolète très rapidement.

Une BALF est plus anonyme mais aussi plus stable dans le temps.

Nous pouvons ici faire valoir le bon sens et laisser le choix aux producteurs de données, pourvu que :

- le point de contact renseigné soit d'une granularité adaptée,
- soit directement relié à une personne physique responsable de la production et la mise à jour des données,
- permette un traitement des demandes des utilisateurs le plus rapide et le plus efficace possible.

En cas de doute, il est recommandé de privilégier la BALF.

## Opérations courantes

### Ouverture d'un jeu de données

Un jeu de données doit être importé sur la plateforme comme source plutôt qu'en pièce jointe, à la fois pour le rendre accessible programmatiquement (API), l'exporter facilement dans divers formats et pouvoir l'explorer facilement.

Les fichiers compressés (`.zip`, `.tar.gz`, etc.) sont difficiles à utiliser, ne donnent aucune information sur leur contenu et ne sont pas recommandés. Le format `.rar` est quant à lui propriétaire et ne doit pas être utilisé.

Dans l'onglet `Traitement`, typer le type de champ et définir certains champs comme "facette" permet de faciliter l'affichage, à l'utilisateur de filtrer le jeu de données et de faire des exports ciblés.

Par sécurité, les jeux de données publiés sont par défaut en usage restreint. Les producteurs de données sont par conséquent responsables de leur ouverture, qui nécessite une action consciente :

> *dataset* -> Sécurité -> Sécurité par défaut -> Accès limité aux utilisateurs et groupes autorisés

De manière à assurer la continuité d'activité d'un jeu de donnée et sa pérénité dans le temps, n'hésitez pas à donner dans l'onglet `Sécurité` les droits d'accès à votre groupe de rattachement.

Tout jeu de données ouvert est ensuite moissonné par les plateformes **data.gouv.fr** et peut potentiellement entrer dans la chaîne de dépendance de systèmes d'information tiers.

Les jeux de données de `test` ou de `preprod` ne doivent être ouverts qu'à un public restreint en accordant aux personnes habilitées les droits adaptés, en lecture et/ou en écriture.

N'hésitez pas à solliciter l'équipe d'administration à ce sujet.

### Modification de l'identifiant technique d'un jeu de données

**Attention** : Le changement d'identifiant technique sur **data.economie.gouv.fr** est une opération qui provoque des effets de bord difficiles à appréhender. Elle ne doit en aucun cas être réalisée sans l'appui d'un administrateur.

### Suppression d'un jeu de données

**Attention** : La suppression d'un jeu de données public non restreint est une opération administrateur, quelle que soit la plateforme **data.economie.gouv.fr** ou **data.gouv.fr**.

Adressez la demande à l'équipe d'administration qui la traitera dans les plus brefs délais, en fournissant les liens pointant vers les jeux de données à supprimer.

Un certain nombre de jeux de données sont réutilisés par des systèmes d'information tiers et entrent dans la chaîne logistique informationnelle.

Une suppression sans étude d'impact peut occasionner une perte d'accès à l'information pour les utilisateurs ainsi qu'une interruption dans la continuité des données.

Un jeu de données supprimé ainsi que ses métadonnées peuvent ne pas être récupérables facilement.

Le titre du jeu de données devra utiliser le formatage strict `[DEPRECIE][SUPPR :: YYYY-MM-JJ] <titre du jeu de données>` et être conservé au moins un mois avant expiration de la référence.

L'ajout de la date d'extinction sera prochainement prise en charge pour provoquer la suppression du jeu de donneés programmatiquement.

### Tester un jeu de données en accès restreint

Les jeux de données en accès restreint ne sont accessibles de manière programmatique qu'après authentification. Après avoir [généré une clé API](https://data.economie.gouv.fr/account/api-keys/), vous pouvez intégrer la clé au `header` de la requête comme ceci :

```python
import os

import requests

KEY = os.environ["KEY"]
HEADERS = {"Authorization": f"Apikey {KEY}"}
print(HEADERS)
DATASET_NAME = "test-my-dataset"

url = f"https://**data.economie.gouv.fr**/api/explore/v2.1/catalog/datasets/"
params = {"where": f"dataset_id='{DATASET_NAME}'", "include_app_metas": True}

response = requests.get(url, headers=HEADERS, params=params)
print(response.json())
```

**Attention** : une clé API ne doit jamais être publiée, il reste préférable de passer par des variables d'environnement.

### Répondre à une discussion

Comme évoqué plus haut, les deux plateformes **data.gouv.fr** comme **data.economie.gouv.fr** proposent une fonctionnalité de discussion permettant aux réutilisateurs des jeux de données de faire part aux métiers de leurs remarques sur les données, questionnements ou encore suggestions de montée en qualité.

Il est recommandé de laisser les utilisateurs passer par cette fonctionnalité et de leur répondre sans donner l'adresse de boîtes aux lettres fonctionnelles ou autres boîtes aux lettres personnelles : rester sur un seul canal respecte le principe de transparence, favorise le partage de connaissances et la réduction du spam.

Lorsqu'un message laissé via le formulaire de contact vous est transmis et que vous souhaitez lui répondre directement, il est préférable de mettre **contact.dataeconomie@finances.gouv.fr** en copie ou de renvoyer le message à transmettre avec un commentaire adapté.

Réponse devra être donnée à un commentaire dans les 7 jours à partir de la réception par le métier de la demande.

## Monitoring

### Suivi du remplissage des métadonnées

Un jeu de données mis à jour à une fréquence bi-hebdomadaire peut vous renseigner sur le taux de remplissage de vos métadonnées :

- https://**data.economie.gouv.fr**/explore/dataset/admin-qualite-des-jeux-de-donnees-publies

Le `quality_score` est indicatif.

______________________________________________________________________

## Ressources

### Testes juridiques

\*\*Loi pour une république numérique : https://www.economie.gouv.fr/files/files/PDF/DP_LoiNumerique.pdf

### Documentation technique

**Publier un jeu de données** : https://userguide.opendatasoft.com/fr/articles/2248514

\centering ![](./src/media/faq-publish-dataset.png){width=50px} \raggedright \flushleft

**Remplir les métadonnées** : https://userguide.opendatasoft.com/fr/articles/2031938

\centering ![](./src/media/faq-fill-metadata.png){width=50px} \raggedright \flushleft

### Métadonnées

**DCAT** : https://doc.data.gouv.fr/moissonnage/dcat/

\centering ![](./src/media/faq-dcat.png){width=50px} \raggedright \flushleft

**Datasheets for datasets** : https://open.datactivist.coop/docs/datasheets-datasets

\centering ![](./src/media/faq-datasheets-for-datasets.png){width=50px} \raggedright \flushleft

### Acculturation à la donnée

Lab Archipel - DATAcculturation : https://www.youtube.com/watch?v=_yxlo41dBuA

\centering ![](./src/media/faq-lab-archipel-dataculturation.png){width=50px} \raggedright \flushleft

Open Data France : https://opendatafrance.fr/les-ressources/

\centering ![](./src/media/faq-opendatafrance-resources.png){width=50px} \raggedright \flushleft

[Datactivist - Blog](https://open.datactivist.coop/docs) : https://open.datactivist.coop/docs

______________________________________________________________________

## Annexe

### Conversion d'un fichier Excel en CSV

**Préparation du fichier**

- Supprimer les cellules fusionnées, incompatibles avec le format CSV
- Éliminer les formules complexes pour ne conserver que les valeurs calculées
- Vérifier que les en-têtes de colonnes ne sont présents que sur la première ligne
- Supprimer les feuilles multiples et consolider les données sur une seule feuille

**Conversion du fichier**

- Dans Excel, "Enregistrer sous" et sélectionner "CSV (séparateur: point-virgule)"
- Vérifier l'encodage UTF-8 lors de l'enregistrement
- Contrôler que le séparateur choisi (virgule ou point-virgule) ne crée pas d'erreurs de restitution.

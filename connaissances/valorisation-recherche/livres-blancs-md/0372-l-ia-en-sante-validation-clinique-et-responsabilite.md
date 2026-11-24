---
sous_titre: Savoir comment valider un algorithme médical, clarifier les responsabilités et préparer la réglementation avant de le déployer auprès de patients africains.
meta_description: IA en santé : validation clinique, responsabilité et réglementation d'un algorithme médical avant déploiement, pour les chercheurs africains.
mots_cles: IA en santé, validation clinique, responsabilité, algorithme
---

# L'IA en santé : validation clinique et responsabilité

## Résumé

Un algorithme qui lit une radiographie, prédit un risque ou aide à poser un diagnostic peut sauver des vies, notamment là où les médecins sont rares. Il peut aussi nuire si ses limites sont mal connues. Ce livre blanc s'adresse aux chercheurs. Il explique pourquoi une bonne performance en laboratoire ne suffit pas, comment concevoir une validation clinique rigoureuse, comment qualifier le dispositif au regard de la réglementation, comment partager les responsabilités entre développeur, établissement, soignant et fournisseur, et comment organiser le transfert vers un déploiement sûr. Il propose une méthode en dix étapes et un plan d'action adapté aux systèmes de santé africains.

## 1. Le constat

L'intelligence artificielle appliquée à la santé progresse rapidement : analyse d'images médicales, dépistage de la rétinopathie, détection de la tuberculose sur radiographie, interprétation d'électrocardiogrammes, prédiction du risque de complications, aide à la décision en soins primaires, triage par messagerie, suivi des patients chroniques. Dans les pays où le nombre de spécialistes par habitant est très faible, ces outils suscitent un espoir légitime.

Mais plusieurs difficultés séparent la promesse de la pratique.

**La performance publiée n'est pas la performance réelle.** Un algorithme entraîné et évalué sur les données d'un hôpital peut perdre beaucoup de précision dans un autre établissement, avec d'autres appareils, d'autres populations, d'autres maladies. Ce phénomène de décalage entre données d'entraînement et données d'usage est la première cause d'échec.

**Les données d'entraînement sont rarement représentatives.** Des jeux de données issus de pays à revenu élevé peuvent mal fonctionner sur des patients africains, par la diversité des populations, des pathologies, des conditions d'acquisition des images, de la qualité des équipements.

**La validation est coûteuse et longue.** Une étude clinique sérieuse demande un protocole, une autorisation éthique, un recrutement, une analyse statistique indépendante. Peu de laboratoires de recherche en intelligence artificielle ont l'expérience nécessaire.

**La réglementation est exigeante et évolutive.** Un logiciel destiné à aider au diagnostic ou à orienter un traitement peut être considéré comme un dispositif médical, avec des obligations de qualité, de documentation, de surveillance après mise sur le marché. Beaucoup de pays africains construisent leur cadre, et leurs exigences varient.

**Les responsabilités sont floues.** En cas d'erreur, qui répond : le chercheur qui a conçu l'algorithme, l'entreprise qui le commercialise, l'établissement qui l'utilise, le médecin qui a suivi ou ignoré la recommandation ? Faute de clarté, les soignants se méfient et les assureurs hésitent.

## 2. Ce que montrent les expériences

### Le chemin du dispositif médical

Les sociétés issues de laboratoires dans le domaine de la santé savent que le développement est long et coûteux, plus encore pour les produits qui touchent directement au patient. L'expérience des dispositifs médicaux enseigne plusieurs repères. D'abord, les dossiers réglementaires sont lourds : des centaines de pages, des mois ou des années de préparation, des coûts importants, avec des voies de classification selon le niveau de risque. Ensuite, la réglementation exige un système de gestion de la qualité du fabricant, qui s'impose à l'entreprise licenciée et non au laboratoire. Enfin, le temps entre l'idée et l'autorisation est souvent de plusieurs années. Cela explique pourquoi les équipes avisées se concentrent d'abord sur des applications de moindre risque, ou sur des fonctions d'aide à la décision qui laissent au soignant la décision finale.

### La validation en plusieurs niveaux

Une validation sérieuse suit plusieurs étapes :

- **La validation technique** : performance sur des données de test indépendantes, mesure de la sensibilité, de la spécificité, de la valeur prédictive, de la calibration, de la robustesse à des variations (appareils, bruit, populations).
- **La validation externe** : test sur des données d'autres établissements, d'autres pays, d'autres populations, sans réentraînement.
- **La validation clinique rétrospective puis prospective** : l'algorithme est évalué sur des cas réels, d'abord en arrière-plan sans influencer les soins, puis intégré au parcours, avec comparaison à la pratique habituelle.
- **L'évaluation d'impact** : l'outil améliore-t-il les décisions, les délais, les résultats pour les patients, les coûts ? Un algorithme précis qui n'est pas utilisé ou qui n'améliore rien a peu de valeur.
- **La surveillance continue** : la performance évolue avec le temps, les équipements, les populations. Un suivi après déploiement est indispensable.

### Les enseignements de la valorisation en sciences de la vie

Les établissements qui créent des entreprises dans les sciences du vivant insistent sur la rigueur : ne pas sous-estimer les exigences réglementaires, s'entourer tôt de compétences en qualité et en affaires réglementaires, démontrer la valeur auprès de cliniciens et d'acheteurs. Ils soulignent aussi l'importance de la propriété intellectuelle et de la clarté des droits avant d'attirer des investisseurs, et de l'équipe : la meilleure technologie ne suffit pas sans dirigeants capables de la porter. Dans le domaine des algorithmes, la propriété intellectuelle se construit souvent autour du droit d'auteur, du secret sur les modèles et les données, et, quand c'est possible, de brevets sur les applications techniques précises.

> À retenir : en santé, la confiance se gagne par la preuve. Un algorithme médical doit démontrer qu'il est sûr, efficace et équitable dans les conditions où il sera utilisé, par des études indépendantes et transparentes, avant d'être déployé.

### La responsabilité, un partage à écrire

Plusieurs niveaux de responsabilité coexistent. Le fabricant ou fournisseur répond de la conformité du produit, de sa documentation, de la surveillance de ses performances et de l'information sur ses limites. L'établissement de santé répond du choix de l'outil, de la formation du personnel, de l'intégration dans les parcours, de la gouvernance des données. Le professionnel de santé reste responsable de ses décisions : un outil d'aide ne le dispense pas de son jugement. Le chercheur doit documenter honnêtement les limites et éviter les promesses excessives. Les contrats doivent préciser ces partages, les obligations de signalement d'incidents, les assurances, la gestion des mises à jour et le sort des données. Les principes d'éthique de l'intelligence artificielle en santé publiés par des organisations internationales de santé insistent sur la transparence, l'équité, la supervision humaine et la responsabilité.

### Les données de santé

Les données de santé sont parmi les plus sensibles. Leur usage pour entraîner et valider des algorithmes exige consentement ou base légale appropriée, autorisation éthique, sécurité, minimisation et, souvent, restrictions de transfert à l'étranger. Un projet qui contourne ces exigences met en danger les patients et se fragilise juridiquement.

## 3. Méthode pas à pas

**Étape 1. Définir précisément l'usage clinique.** Quelle décision l'algorithme soutient-il ? Pour quel patient, quel soignant, quel niveau de soins ? Quelle est la pratique actuelle ? Quel serait le bénéfice ? Quelles erreurs seraient les plus graves ? Plus l'usage est précis, plus la validation est claire.

**Étape 2. Classer le risque et identifier le cadre réglementaire.** Déterminez si le logiciel est un dispositif médical selon la réglementation applicable, à quelle classe de risque, et quelles autorités sont concernées. Consultez tôt l'autorité nationale du médicament et des dispositifs ou des experts réglementaires.

**Étape 3. Constituer des données représentatives et éthiques.** Obtenez les autorisations éthiques, le consentement ou l'autorisation légale, la pseudonymisation, un stockage sécurisé. Vérifiez la diversité des données : sites, appareils, âges, sexes, pathologies, qualité d'image.

**Étape 4. Développer avec une traçabilité rigoureuse.** Documentez les données, le code, les versions, les choix de conception, les tests. Cette traçabilité est la base du futur dossier réglementaire.

**Étape 5. Évaluer techniquement et valider en externe.** Utilisez des jeux de test indépendants, séparés dès le départ. Testez sur des sites et populations différents sans réentraînement. Publiez les performances par sous-groupes pour détecter les inégalités.

**Étape 6. Protéger avant de publier.** Si le projet comporte une invention technique, déclarez-la au bureau de valorisation avant toute publication, et ne comptez jamais sur un délai de grâce. Un brevet OAPI couvre les 17 États membres de l'organisation, pas le monde. Organisez le droit d'auteur, le secret sur les modèles et les données, et les accords de confidentialité.

**Étape 7. Mener une étude clinique prospective.** Associez des cliniciens et des statisticiens, rédigez un protocole, obtenez l'accord du comité d'éthique, déterminez les indicateurs de succès avant de commencer, enregistrez l'étude si les règles le prévoient. Évaluez l'impact réel sur les décisions et les résultats.

**Étape 8. Clarifier les responsabilités par contrat.** Entre le laboratoire, l'établissement partenaire, l'entreprise éventuelle et les utilisateurs : rôles, assurances, gestion des incidents, mise à jour, propriété et usage des données, limites d'utilisation. Prévoyez des avis aux utilisateurs clairs sur ce que l'outil ne doit pas faire.

**Étape 9. Choisir la voie de transfert et la structure.** Licence à un fabricant de dispositifs ou de logiciels médicaux existant, société dérivée avec un responsable qualité et réglementaire, partenariat avec un système de santé. Dans tous les cas, le fabricant doit disposer d'un système de qualité.

**Étape 10. Déployer progressivement et surveiller.** Commencez par un site pilote, formez les soignants, instaurez un circuit de signalement des erreurs, suivez la performance dans le temps, planifiez les mises à jour et les audits.

### Commencer par les usages à moindre risque

Une stratégie prudente consiste à débuter par des usages où l'algorithme assiste sans décider : priorisation de listes de lecture pour les radiologues, contrôle de la qualité des images, aide à la saisie, détection de cas à revoir. Ces applications démontrent la valeur, construisent la confiance des soignants et génèrent des données de performance réelles, avant d'aborder des fonctions de diagnostic plus exposées. Elles permettent aussi de rôder les circuits de signalement et de formation, indispensables pour la suite.

## 4. Erreurs à éviter

- **Annoncer des performances sans validation externe.** C'est l'erreur la plus fréquente et la plus risquée.
- **Entraîner et tester sur les mêmes données ou sur des données trop proches.** Les résultats sont alors artificiellement bons.
- **Ignorer la diversité des patients.** Un algorithme performant sur une population peut être dangereux sur une autre.
- **Négliger l'éthique et les données.** Utiliser des données de santé sans base légale expose à des sanctions et détruit la confiance.
- **Sous-estimer la réglementation.** Un produit déployé sans autorisation peut être retiré, et les promoteurs poursuivis.
- **Laisser croire que l'algorithme remplace le soignant.** Un outil d'aide doit être présenté et conçu comme tel, avec supervision humaine.
- **Oublier la surveillance.** Les performances se dégradent sans suivi.
- **Publier avant de protéger.** Un article détaillé peut empêcher le dépôt d'un brevet.
- **Négliger l'intégration au travail réel.** Un outil qui ralentit le soignant ou exige des manipulations compliquées ne sera pas utilisé.
- **Rester flou sur la responsabilité.** Sans cadre contractuel, le premier incident provoque un blocage.

## 5. Application au contexte africain

### Des besoins immenses et des conditions particulières

Dans de nombreux pays africains, le nombre de radiologues, d'ophtalmologues, de pathologistes et de cardiologues est très inférieur aux besoins. Un outil d'aide à la lecture d'images, de dépistage ou de triage peut étendre l'accès aux soins. Mais les conditions d'usage sont particulières : équipements de génération variée, images de qualité inégale, pannes d'électricité, connexions intermittentes, soignants polyvalents et débordés, dossiers médicaux souvent papier. Un algorithme doit être validé et conçu pour ces conditions, et testé avec elles.

### Le cadre réglementaire

Plusieurs pays africains disposent d'autorités de réglementation des produits de santé qui évaluent des dispositifs médicaux, et certains ont commencé à encadrer les logiciels médicaux. L'Agence africaine du médicament, créée au niveau continental, vise à harmoniser et à renforcer la réglementation des produits médicaux, ce qui devrait à terme faciliter la reconnaissance entre pays. Les lois sur la protection des données personnelles et les règles d'éthique de la recherche s'appliquent aux données de santé. Les chercheurs doivent consulter tôt leur autorité nationale, car les exigences évoluent et diffèrent d'un pays à l'autre.

### Les institutions et partenaires

Les facultés de médecine, les hôpitaux universitaires, les instituts de santé publique, les comités nationaux d'éthique, les ministères de la santé, les assureurs, les organisations internationales de santé et les entreprises de dispositifs médicaux sont les partenaires clés. Les bureaux de valorisation aident à structurer les droits et les licences, avec l'appui des offices de propriété intellectuelle, dont l'OAPI et l'ARIPO. Les partenariats Sud-Sud pour valider un algorithme dans plusieurs pays sont particulièrement précieux.

### Un cas type

Une équipe d'une université d'Afrique centrale, associée à un hôpital universitaire, développe un algorithme d'aide à la détection de la tuberculose sur radiographie thoracique. Elle constitue un jeu de données avec autorisation éthique et pseudonymisation, et déclare l'invention avant publication. La validation externe, menée dans deux autres pays avec des appareils différents, révèle une baisse de performance sur des images de mauvaise qualité ; l'équipe améliore la détection de la qualité d'image et intègre un message invitant à refaire la radiographie. Une étude prospective évalue l'impact sur le délai de diagnostic dans trois centres de santé. Le produit est présenté comme aide à la décision, avec confirmation par un soignant. Un contrat précise les responsabilités entre l'hôpital, l'université et une jeune entreprise titulaire de la licence, qui met en place un système de qualité et assure le suivi des performances.

### Équité et confiance

Les équipes africaines ont une occasion de montrer l'exemple en publiant les performances par sous-groupes, en associant les patients et les soignants à la conception, en documentant clairement les limites et en refusant de déployer un outil non validé. Cette exigence construit la confiance des autorités, des soignants et des patients, et distingue les projets sérieux des initiatives opportunistes.

## 6. Plan d'action

| Étape | Qui | Quand | Résultat attendu |
|---|---|---|---|
| Définir l'usage clinique et le risque | Chercheurs, cliniciens | Mois 1 à 2 | Cahier des charges clinique, classe de risque |
| Consulter l'autorité et le comité d'éthique | Chercheurs, juristes | Mois 1 à 4 | Cadre réglementaire et autorisations identifiés |
| Constituer des données représentatives | Chercheurs, hôpitaux | Mois 3 à 12 | Jeu de données éthique, diversifié, documenté |
| Protéger avant publication | Bureau de valorisation | Avant toute diffusion | Dépôts effectués, secrets organisés |
| Valider techniquement et en externe | Équipe, sites partenaires | Mois 9 à 18 | Performances par sous-groupes publiées |
| Mener l'étude clinique prospective | Cliniciens, statisticiens | Mois 15 à 30 | Preuve d'impact sur les décisions et résultats |
| Contractualiser responsabilités et transfert | Bureau de valorisation, hôpital, entreprise | Mois 18 à 30 | Licence et contrats de déploiement signés |
| Déployer et surveiller | Entreprise, hôpitaux | En continu | Suivi de performance, incidents traités |

## Conclusion

L'intelligence artificielle peut aider à rapprocher les soins de ceux qui en manquent, à condition de mériter la confiance. Pour un chercheur, cela signifie accepter la lenteur de la validation, la rigueur de l'éthique, l'exigence de la réglementation et la clarté sur les responsabilités. Ces contraintes ne sont pas des obstacles administratifs : elles protègent des patients et garantissent que les algorithmes tiennent leurs promesses. Les équipes africaines qui s'y engagent bâtissent des outils adaptés à leurs réalités, reconnus par leurs autorités et utiles à leurs soignants. C'est ainsi qu'une innovation devient, sans compromis sur la sécurité, un progrès de santé publique.

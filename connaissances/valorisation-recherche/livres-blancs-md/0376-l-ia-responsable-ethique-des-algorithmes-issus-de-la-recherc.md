---
sous_titre: Évaluer les biais, la transparence et l'impact social de votre système d'IA avant de le publier, de le licencier ou de le déployer auprès d'utilisateurs réels.
meta_description: IA responsable : méthode pour évaluer biais, transparence et impact social d'un algorithme issu de la recherche avant sa diffusion en Afrique.
mots_cles: IA responsable, éthique, biais, transparence, impact social
---

# L'IA responsable : éthique des algorithmes issus de la recherche

## Résumé

Un modèle d'intelligence artificielle développé dans un laboratoire peut en quelques semaines se retrouver dans un hôpital, une banque, une école ou un service public. Le chercheur qui l'a conçu n'a pourtant pas toujours été formé pour mesurer ce que le système fera aux personnes qui le subiront. Ce livre blanc s'adresse aux chercheurs et propose une démarche concrète pour examiner un algorithme avant sa diffusion : comprendre d'où viennent les biais, documenter le fonctionnement du système, tester son effet sur différents groupes, associer les futurs usagers et préparer la suite avec le bureau de valorisation. Il montre aussi pourquoi cette rigueur est un atout pour obtenir des licences, des financements et la confiance des partenaires, en particulier dans les contextes africains où les données et les usages sont spécifiques.

## 1. Le constat

Les algorithmes issus de la recherche circulent plus vite que jamais. Un article accompagné d'un code publié en accès ouvert peut être repris par une entreprise en quelques jours. Un prototype de démonstration devient un service pilote avant même qu'une évaluation sérieuse ait été menée. Dans ce contexte, la responsabilité du chercheur ne s'arrête plus à la qualité scientifique de la publication.

Trois constats se dégagent.

**Les erreurs d'un algorithme ne se répartissent pas au hasard.** Un modèle entraîné sur des données qui sous-représentent certaines régions, langues, couleurs de peau, âges ou niveaux de revenus fonctionne bien en moyenne et mal pour ceux qui sont absents des données. Les exemples abondent dans le monde : outils de reconnaissance faciale moins fiables pour certaines populations, systèmes de reconnaissance vocale peu performants sur des accents ou des langues peu dotées, modèles de scoring qui reproduisent des inégalités passées. Les langues africaines, les contextes cliniques africains et les profils de revenus informels sont encore peu présents dans les grands jeux de données mondiaux. Un modèle importé sans adaptation risque donc de se tromper plus souvent sur les populations locales, et un modèle développé localement peut reproduire d'autres biais s'il s'appuie sur des données collectées auprès d'un public restreint, par exemple les citadins connectés.

**Les systèmes sont souvent opaques, y compris pour ceux qui les construisent.** Un réseau de neurones profond ne livre pas ses raisons. Si personne ne sait dire pourquoi un patient a été classé à risque ou une demande de crédit refusée, la personne concernée ne peut ni contester ni corriger. L'opacité est un problème d'éthique, mais aussi de crédibilité commerciale : un industriel ou un hôpital hésite à adopter ce qu'il ne peut pas expliquer à ses clients ou à son régulateur.

**Le cadre juridique et institutionnel se renforce.** L'Union européenne a adopté un règlement sur l'intelligence artificielle fondé sur les niveaux de risque. L'UNESCO a publié une recommandation sur l'éthique de l'IA, adoptée par ses États membres. L'Union africaine a élaboré une stratégie continentale sur l'intelligence artificielle, et plusieurs pays africains ont lancé des stratégies nationales ou des travaux de régulation. Les bailleurs de fonds et les revues scientifiques demandent de plus en plus de garanties sur l'éthique et la gouvernance des données. Un chercheur qui ignore ces exigences se prive de financements et de partenaires.

## 2. Ce que montrent les expériences

**La documentation systématique.** Des équipes de recherche ont pris l'habitude de publier avec chaque modèle une fiche descriptive : objectif, données d'entraînement, performances par sous-groupe, limites connues, usages déconseillés. Ces fiches, parfois appelées fiches de modèle ou fiches de données, ne coûtent presque rien et évitent les mauvais usages. Elles rassurent aussi les licenciés potentiels.

**L'évaluation par sous-groupes.** Les erreurs graves se révèlent souvent quand on mesure la performance séparément pour des groupes définis par le sexe, l'âge, la région, la langue ou le type d'équipement utilisé. Une moyenne de précision de 90 % peut cacher une précision beaucoup plus faible pour un groupe minoritaire.

**La participation des usagers.** Les projets qui réunissent dès le début les personnes concernées, soignants, agriculteurs, enseignants, agents publics, repèrent plus tôt les usages inattendus et les barrières pratiques. Un outil de diagnostic qui suppose une connexion stable, une langue d'interface unique ou un équipement coûteux sera abandonné dans de nombreux centres de santé de district, quelle que soit sa performance en laboratoire.

**L'audit externe.** Certaines équipes confient leur système à un groupe indépendant qui cherche à le mettre en défaut. Cette pratique, empruntée à la cybersécurité, révèle des failles que les concepteurs ne voient plus.

**Un cas type.** Une équipe universitaire ouest-africaine développe un modèle de repérage de maladies de cultures à partir de photographies de feuilles. Les premiers essais donnent d'excellents résultats, mais les images viennent presque toutes d'une seule station expérimentale, avec la même lumière et les mêmes variétés. En déployant l'outil chez des producteurs, la précision chute fortement. L'équipe organise alors une collecte participative dans plusieurs régions, publie une fiche de limites et fait tester l'application par des conseillers agricoles. La version suivante est plus fiable, et une organisation de producteurs accepte de l'adopter.

**Un second cas type.** Une jeune équipe de recherche en traitement du langage met au point un assistant vocal en langue locale pour informer les agricultrices sur les prix et la météo. Les premiers enregistrements proviennent d'étudiants de la capitale, avec une prononciation standard. Sur le terrain, les productrices parlent avec des variantes régionales, et l'outil les comprend mal. Plutôt que de cacher le problème, l'équipe publie les taux d'erreur par région, organise des séances d'enregistrement avec des coopératives et rémunère les participantes. Elle négocie aussi avec les coopératives un partage des retombées en cas de commercialisation. Cette transparence a deux effets : la qualité du modèle progresse, et un opérateur de télécommunications accepte de signer un accord pilote parce qu'il voit des garanties.

**Le rôle des revues et des bailleurs.** De plus en plus de revues demandent une déclaration sur l'éthique des données et sur les risques d'usage détourné. Plusieurs programmes de financement internationaux exigent un plan de gestion des données et une analyse d'impact. S'y préparer dès le montage du projet fait gagner du temps et améliore les dossiers.

> À retenir : un système d'IA n'est responsable que s'il a été testé sur les personnes et dans les conditions où il sera réellement utilisé. Une bonne performance moyenne ne prouve rien sur chaque groupe.

## 3. Méthode pas à pas

**Étape 1. Définir l'usage prévu et les usages exclus.** Écrivez en quelques phrases ce que le système doit faire, pour qui, dans quel contexte, et ce qu'il ne doit pas faire. Précisez les décisions qu'il peut éclairer et celles qui doivent rester humaines.

**Étape 2. Classer le niveau de risque.** Posez-vous la question suivante : si le système se trompe, quelles sont les conséquences pour une personne ? Un outil de recommandation de lectures n'a pas la même gravité qu'un outil de tri de patients ou d'attribution d'aides. Plus le risque est élevé, plus l'évaluation doit être poussée et plus un contrôle humain est nécessaire.

**Étape 3. Documenter les données.** Notez l'origine des données, la période de collecte, le consentement obtenu, les groupes représentés et absents, les pratiques d'annotation, les limites. Vérifiez que la collecte respecte la loi nationale sur les données personnelles et les règles d'éthique de votre établissement.

**Étape 4. Mesurer les biais.** Choisissez des critères pertinents pour votre contexte et calculez les performances par sous-groupe : taux de faux positifs, de faux négatifs, de refus. Examinez aussi les variables indirectes qui peuvent servir de substituts à des caractéristiques sensibles, comme le lieu de résidence ou le type de téléphone.

**Étape 5. Rendre le système explicable à la mesure du risque.** Pour les usages à fort enjeu, privilégiez des modèles dont on peut expliquer les décisions, ou ajoutez des outils d'explication validés avec les utilisateurs. À défaut, limitez l'usage du système à un rôle d'aide à la décision.

**Étape 6. Tester en conditions réelles.** Faites un essai pilote limité, avec un suivi des erreurs, des retours des usagers et des effets inattendus. Prévoyez un moyen simple de signaler un problème.

**Étape 7. Prévoir le contrôle humain et la voie de recours.** Définissez qui peut annuler une décision automatisée, comment une personne peut la contester et dans quel délai.

**Étape 8. Évaluer l'impact social et environnemental.** Examinez qui gagne et qui perd si l'outil est adopté : emplois transformés, accès aux services, dépendance envers un fournisseur étranger, consommation d'énergie pour l'entraînement et l'hébergement.

**Étape 9. Choisir la licence et les conditions d'usage.** Le choix entre code ouvert, licence restreinte ou licence commerciale a des conséquences éthiques. Certaines licences interdisent des usages jugés dangereux. Avant toute publication du code ou des modèles, consultez le bureau de valorisation : protéger ce qui peut l'être, par un brevet ou un droit d'auteur, doit se faire avant la divulgation, car on ne peut pas compter sur un délai de grâce pour réparer une publication trop précoce.

**Étape 10. Organiser la maintenance et le suivi.** Un modèle vieillit : les données changent, les usages aussi. Décidez qui surveille la performance, qui met à jour et à quelle fréquence, et comment retirer le système si nécessaire.

**Quelques questions simples à se poser avant chaque diffusion.** Qui pourrait être lésé par une erreur du système, et le sait-on ? Quelles données manquent, et pourquoi ? Une personne peut-elle comprendre ce qui s'est passé et obtenir un recours ? Qui répond du système dans deux ans ? Que se passe-t-il si un tiers réutilise le modèle pour un autre usage ? Si l'une de ces questions reste sans réponse, la diffusion peut attendre quelques semaines. Ce délai est presque toujours moins coûteux qu'une crise de confiance.

**Le rôle du collectif.** Aucune équipe ne voit tous ses angles morts. Organisez des revues croisées avec des collègues d'autres disciplines : un juriste, un sociologue, un clinicien, un enseignant. Leur regard sert aussi à préparer le dialogue avec les futurs licenciés, qui poseront les mêmes questions.

## 4. Erreurs à éviter

- **Croire que l'éthique se règle à la fin.** Corriger un biais découvert après le déploiement coûte beaucoup plus cher que de l'éviter dans la conception.
- **Se contenter d'une performance moyenne.** Examinez toujours les sous-groupes.
- **Confondre anonymisation et absence de risque.** Des données qui paraissent anonymes peuvent être réidentifiées par recoupement, surtout dans de petites communautés.
- **Utiliser des données collectées sans base légale claire.** Une collecte faite sans consentement valable peut rendre le système inutilisable commercialement.
- **Promettre ce que le système ne sait pas faire.** Une communication enthousiaste attire l'attention, mais un usage hors du domaine de validité cause des dommages.
- **Négliger les langues et les contextes locaux.** Un modèle formé uniquement sur des données d'autres continents peut ne pas fonctionner pour vos usagers.
- **Oublier la dépendance.** Un système qui exige un service étranger payant ou une connexion permanente peut devenir inutilisable pour les institutions publiques.
- **Ne pas désigner de responsable.** Si personne ne répond des effets du système après le départ du doctorant qui l'a programmé, les problèmes resteront sans suite.
- **Publier sans réfléchir à la protection.** Un code mis en ligne avant tout dépôt ou toute décision de licence peut éliminer les possibilités de valorisation et entraîner une réutilisation sans contrôle.

## 5. Application au contexte africain

Le contexte africain combine des opportunités et des contraintes particulières.

**Des besoins prioritaires.** Santé de proximité, agriculture, éducation, services financiers inclusifs, gestion des risques climatiques : les applications possibles sont nombreuses, et les usagers sont souvent peu familiers des outils numériques. L'explicabilité et l'accompagnement humain sont donc essentiels.

**Des données rares et précieuses.** Les jeux de données sur les langues africaines, sur les maladies tropicales ou sur les conditions agricoles locales sont encore limités. Des initiatives communautaires de collecte de corpus de langues, des réseaux de chercheurs en apprentissage automatique et des programmes de formation se développent sur le continent. Les chercheurs gagnent à s'y associer, tout en veillant à la gouvernance de ces données : qui les détient, qui peut les utiliser, comment les bénéfices sont partagés.

**Un cadre en construction.** La stratégie continentale de l'Union africaine sur l'IA, la Convention de Malabo sur la cybersécurité et les données personnelles, les lois nationales sur les données (au Kenya, au Nigeria, au Rwanda, en Afrique du Sud, au Sénégal, en Côte d'Ivoire et ailleurs) et les stratégies numériques nationales fixent progressivement les règles. Les autorités de protection des données et les comités d'éthique de la recherche constituent les interlocuteurs naturels. Il est prudent de contacter l'autorité nationale avant un déploiement à grande échelle.

**Des dispositifs d'appui.** Les offices de transfert et les cellules de valorisation des universités, les incubateurs, les conseils en propriété intellectuelle agréés auprès de l'OAPI et les organisations de recherche régionales peuvent conseiller sur la protection du code, des modèles et des bases de données. Un brevet OAPI couvre les 17 États membres de l'organisation, et non le monde entier : si l'enjeu commercial est mondial, il faut prévoir une stratégie par territoires. Le droit d'auteur protège le code sans formalité, mais ne dispense pas d'un contrat clair avec les contributeurs.

**Une éthique enracinée localement.** Les notions de consentement individuel, de bénéfice communautaire et de responsabilité envers la collectivité varient selon les contextes. Plutôt que d'appliquer mécaniquement une grille importée, associez des représentants des communautés concernées, des juristes, des spécialistes des sciences humaines et des usagers. Cette approche n'affaiblit pas la rigueur. Elle la rend adaptée.

**Un avantage compétitif.** Des entreprises et des investisseurs internationaux cherchent des partenaires capables de démontrer des pratiques sérieuses. Un chercheur africain qui présente un modèle documenté, évalué par groupes et soumis à un audit offre une garantie rare.

## 6. Plan d'action

| Étape | Qui | Quand | Résultat attendu |
|---|---|---|---|
| Rédiger la note d'usage prévu et d'usages exclus | Chercheur responsable du projet | Avant tout partage du code | Note d'une page validée par l'équipe |
| Classer le niveau de risque et décider du contrôle humain | Équipe et comité d'éthique | Début du projet | Niveau de risque documenté |
| Documenter les données et vérifier la base légale | Chercheur, délégué à la protection des données | Avant l'entraînement | Fiche de données complète |
| Mesurer les performances par sous-groupe | Équipe technique | Avant la publication | Tableau de résultats par groupe |
| Tester avec de vrais usagers sur un pilote | Équipe, partenaires de terrain | 3 à 6 mois avant le déploiement | Retours et corrections |
| Consulter le bureau de valorisation sur la protection et la licence | Chercheur, office de transfert | Avant toute divulgation | Décision de protection et type de licence |
| Publier la fiche du modèle et les limites connues | Équipe | À la diffusion | Documentation publique |
| Mettre en place le suivi et la maintenance | Établissement, partenaire licencié | Après le déploiement | Responsable désigné et calendrier de revue |

## Conclusion

Un algorithme issu de la recherche porte une double promesse : un progrès scientifique et un service rendu à des personnes réelles. Pour tenir la seconde promesse, il faut accepter d'examiner ses angles morts avant que d'autres ne les découvrent à leurs dépens. Les chercheurs africains ont une occasion rare : construire des systèmes adaptés à leurs langues, à leurs contextes et à leurs priorités, avec une exigence de qualité qui inspire confiance aux usagers, aux autorités et aux investisseurs. Évaluer les biais, documenter, tester sur le terrain et prévoir la suite ne ralentit pas l'innovation. C'est ce qui lui permet de durer.

---
sous_titre: Choisir en connaissance de cause entre licence libre, double licence et licence propriétaire pour un logiciel issu de la recherche.
meta_description: Licence logicielle universitaire : open source, double licence ou commerciale, critères de choix et étapes pour un logiciel de recherche.
mots_cles: licence logicielle, open source, double licence, GPL, MIT
---

# La licence d'un logiciel universitaire : libre, double ou commerciale

## Résumé

Les laboratoires produisent des logiciels en quantité : codes de simulation, outils d'analyse de données, applications pour l'agriculture, la santé ou l'éducation. Leur sort dépend d'une décision souvent prise trop vite, parfois par défaut : sous quelle licence les diffuser ? Une licence libre favorise l'adoption et la reconnaissance scientifique, une licence commerciale permet de financer le développement et d'attirer des investisseurs, et la double licence cherche à combiner les deux. Ce livre blanc s'adresse aux universités et aux bureaux de valorisation. Il explique les grandes familles de licences, les questions de titularité à régler avant toute publication, les critères de choix, la méthode à suivre et les pièges à éviter, avant d'adapter le tout aux réalités africaines, où le logiciel est un levier d'innovation à fort impact et à faible coût d'entrée.

## 1. Le constat

Le logiciel occupe une place particulière dans la valorisation de la recherche. Il se copie sans coût, se diffuse sur internet en quelques minutes, se modifie facilement et s'intègre à des produits très variés. Un code publié par un chercheur peut être utilisé le lendemain par des milliers de personnes dans le monde, ou être récupéré par une entreprise qui en fera un produit sans jamais citer l'université. Cette facilité est une chance et un risque.

Dans la plupart des universités, la gestion du logiciel reste moins structurée que celle des brevets. Les chercheurs publient leur code sur une plateforme de partage au moment de la publication d'un article, choisissent une licence par habitude ou par imitation, et ne préviennent pas toujours leur établissement. Plusieurs problèmes en découlent.

**La question de la propriété.** Qui détient les droits sur le code ? Dans de nombreux systèmes, le droit d'auteur sur une œuvre créée par un agent dans le cadre de ses fonctions appartient à son employeur, ou lui est cédé selon la politique de l'établissement. Mais les situations sont multiples : doctorants, stagiaires, collaborateurs d'autres institutions, contributeurs externes, financements d'un bailleur qui impose des conditions. Si la titularité n'est pas claire, personne ne peut valablement concéder une licence.

**Le caractère irréversible.** Un code publié sous une licence libre ne peut plus être retiré de la circulation. Les personnes qui l'ont téléchargé conservent leurs droits d'usage selon les termes de la licence d'origine. L'établissement peut choisir une autre licence pour les versions futures, mais pas reprendre ce qu'il a déjà donné. Contacter le bureau de valorisation avant la première publication est donc essentiel.

**La confusion entre gratuité et absence de valeur.** Un logiciel libre n'est pas un logiciel sans valeur. De nombreuses entreprises prospères s'appuient sur des composants libres, offrent des services d'intégration, d'hébergement, de support ou de personnalisation, ou proposent une version avancée sous licence commerciale. Les universités qui ont créé des outils libres largement adoptés ont gagné en influence scientifique, en financements et en capacité à nouer des partenariats.

**Les dépendances cachées.** Un programme utilise presque toujours d'autres composants : bibliothèques libres, modules fournis par des partenaires, données sous licence. Chacun impose ses propres conditions. Certaines licences exigent que tout programme qui les intègre soit diffusé sous la même licence. Ignorer ces contraintes peut interdire de choisir la licence souhaitée, ou exposer à des réclamations.

Pour un bureau de valorisation, la question n'est donc pas de choisir une fois pour toutes entre « libre » et « propriétaire », mais d'arbitrer pour chaque logiciel selon son public, son potentiel, ses dépendances et la stratégie de l'établissement.

## 2. Ce que montrent les expériences

### Trois grandes familles de licences

**Les licences permissives.** Elles autorisent presque tout : utiliser, modifier, redistribuer, y compris dans un produit commercial fermé, à condition de conserver la mention du droit d'auteur et le texte de la licence. Les plus connues sont la licence MIT, les licences de type BSD et la licence Apache 2.0, cette dernière ajoutant une concession explicite de droits de brevets par les contributeurs. Elles maximisent l'adoption, y compris par des entreprises, et conviennent quand l'objectif prioritaire est de diffuser largement une méthode ou une norme.

**Les licences à réciprocité forte (copyleft).** La plus emblématique est la licence publique générale GNU (GPL). Elle autorise l'usage, la modification et la redistribution, mais exige que tout ouvrage dérivé distribué soit placé sous la même licence, avec accès au code source. Elle garantit que le logiciel et ses améliorations restent libres. Une variante dite AGPL étend cette obligation aux logiciels utilisés à distance comme services en ligne. Ces licences conviennent quand on veut éviter qu'un acteur privé s'approprie le code sans partager ses améliorations. Elles dissuadent aussi certaines entreprises, qui ne veulent pas ouvrir leur propre code.

**Les licences propriétaires ou commerciales.** Le code source reste fermé, l'utilisateur reçoit un droit d'usage limité, souvent payant, selon des conditions précises (nombre de postes, durée, territoire). Elles conviennent aux logiciels destinés à devenir un produit vendu ou intégré à un service payant, et aux cas où l'investisseur exige le contrôle exclusif du code.

### La double licence : un pont entre les deux mondes

La double licence consiste à offrir le même logiciel sous deux régimes. Le premier est une licence libre à réciprocité forte, accessible gratuitement à la communauté de recherche, aux utilisateurs académiques et aux développeurs qui acceptent de partager leurs modifications. Le second est une licence commerciale, payante, destinée aux entreprises qui veulent intégrer le logiciel à un produit fermé sans obligation de publier leur code. Ce modèle ne fonctionne que si le titulaire détient tous les droits sur le code, ce qui suppose que chaque contributeur ait cédé ou concédé ses droits à l'établissement par un accord de contribution. Sans cela, il ne peut pas offrir une licence commerciale sur du code appartenant à d'autres.

Plusieurs universités et projets de recherche utilisent ce modèle avec succès, notamment pour des bibliothèques et moteurs de calcul : la communauté bénéficie d'un outil gratuit, et les revenus des licences commerciales financent la maintenance et le développement. Le modèle suppose une équipe capable de répondre aux demandes d'entreprises et un produit suffisamment utile pour qu'elles préfèrent payer plutôt que de se conformer à la licence libre.

### Les accords de bonne réputation avec les start-ups open source

Certains établissements ont développé, pour les jeunes entreprises qui bâtissent leur activité sur un logiciel libre issu de l'université, des accords légers qui ne sont pas de véritables licences. L'université n'y perçoit ni redevance ni paiement initial, mais obtient une petite participation au capital ou un droit de participation aux levées de fonds, en échange de la reconnaissance du lien avec le laboratoire et d'un soutien. Cette formule évite de négocier une licence exclusive quand le code est de toute façon déjà public, tout en préservant un lien de long terme.

> À retenir : le choix d'une licence logicielle est une décision stratégique, pas une formalité technique. Elle dépend de l'objectif (adoption, revenus, contrôle), du public visé et de ce que l'établissement possède réellement.

### Les critères qui orientent le choix

L'expérience des bureaux de transfert montre que quelques questions suffisent à orienter la décision.

- **Le logiciel est-il un produit ou un outil de recherche ?** Un outil destiné à la communauté scientifique se prête bien à une licence libre. Un produit visant des clients payants appelle plutôt une licence commerciale ou double.
- **Quelle est la place du logiciel dans le projet d'entreprise ?** Si une start-up doit lever des fonds sur la base de ce code, les investisseurs voudront souvent une licence exclusive ou une propriété claire.
- **Les dépendances imposent-elles une licence ?** Un code qui incorpore des composants sous GPL ne peut généralement pas être distribué sous licence propriétaire.
- **Un financeur impose-t-il des conditions ?** Certains bailleurs exigent un accès ouvert ou une licence particulière. D'autres exigent l'inverse, pour des raisons de sécurité ou de souveraineté.
- **Quelle est la capacité de soutien ?** Un logiciel libre sans équipe pour répondre aux utilisateurs et corriger les erreurs se dégrade vite. Une licence commerciale suppose un service client et une maintenance.
- **Quel est le risque de captation ?** Une licence permissive laisse à une grande entreprise la liberté de reprendre le code sans rien rendre. Si ce risque est inacceptable, le copyleft protège davantage.

### Un cas type

Une équipe d'une université d'Afrique de l'Est a développé un logiciel d'analyse d'images satellitaires pour estimer les rendements agricoles. Le code a été écrit par des doctorants, avec le soutien d'un bailleur international qui encourage la diffusion ouverte. Le bureau de valorisation vérifie la titularité, fait signer aux contributeurs un accord de cession de droits, recense les composants libres utilisés et choisit la double licence : une licence copyleft pour la communauté scientifique et les organisations non gouvernementales, une licence commerciale pour les entreprises de conseil agricole qui souhaitent l'intégrer à leurs services. Un dépôt public permet la contribution de chercheurs extérieurs. Une jeune société, créée par deux anciens doctorants, reçoit une licence commerciale non exclusive pour proposer des services personnalisés aux coopératives, avec une redevance modeste et une participation de l'université à son capital.

## 3. Méthode pas à pas

**Étape 1. Déclarer le logiciel avant toute publication.** Remplissez un formulaire de déclaration auprès du bureau de valorisation : description, date de création, auteurs, financements, composants tiers utilisés, usages envisagés, publication prévue. Plus le contact est précoce, plus le choix reste ouvert. Un dossier simple se traite en quelques jours ; un dossier avec de nombreux contributeurs ou des financements croisés peut demander plus de temps.

**Étape 2. Établir la titularité.** Identifiez qui a écrit quoi : agents de l'établissement, doctorants, stagiaires, partenaires extérieurs, contributeurs occasionnels. Vérifiez les contrats de travail, la politique de propriété intellectuelle, les conventions de recherche et les conditions des financeurs. Faites signer, quand c'est nécessaire, des accords de cession ou de concession de droits. Cette clarification est le fondement de toute licence.

**Étape 3. Dresser l'inventaire des composants tiers.** Listez toutes les bibliothèques et modules intégrés, avec leur licence et leur version. Des outils d'analyse automatique existent pour cela. Repérez les licences à réciprocité forte, les licences non commerciales et les composants sans licence claire. Remplacez ou isolez ceux qui posent problème.

**Étape 4. Définir l'objectif stratégique.** Réunissez chercheurs et bureau de valorisation pour répondre à quelques questions : pour qui est ce logiciel, que voulons-nous qu'il devienne, quelles ressources avons-nous pour le soutenir, quel rôle pour une éventuelle start-up ? Notez la décision et ses raisons.

**Étape 5. Choisir le modèle de licence.** Appliquez les critères ci-dessus pour retenir l'une des options : licence permissive pour une diffusion maximale, licence copyleft pour garder les améliorations ouvertes, double licence pour concilier communauté et revenus, licence commerciale exclusive pour un produit confié à une entreprise. Évitez de rédiger une licence maison : préférez un texte reconnu, déjà compris par les juristes et les développeurs du monde entier.

**Étape 6. Organiser les contributions.** Si le projet accepte des contributions extérieures, mettez en place un accord de contribution (en anglais, contributor license agreement) qui précise les droits concédés par les contributeurs. C'est indispensable pour la double licence, et utile pour toute évolution future de la licence. Rédigez un guide de contribution et un code de conduite simples.

**Étape 7. Préparer le dépôt public ou le contrat de licence.** Pour une diffusion libre, ajoutez au dépôt le fichier de licence, les mentions de droit d'auteur dans les fichiers sources, un fichier d'explication (installation, usage, citation) et la liste des dépendances. Pour une licence commerciale, préparez un contrat type : périmètre, durée, redevances, support, garanties, responsabilité, propriété des améliorations.

**Étape 8. Penser à la marque et au nom.** Le droit d'auteur protège le code, pas le nom du logiciel. Si le logiciel a vocation à devenir un produit, déposez le nom comme marque et précisez dans la licence que le nom ne peut pas être utilisé pour des versions modifiées sans accord. Cette précaution évite les confusions.

**Étape 9. Examiner la protection par brevet si pertinent.** Le logiciel en tant que tel n'est pas brevetable dans de nombreux systèmes, dont celui de l'OAPI, mais une invention technique qui utilise un logiciel peut l'être. Si une demande de brevet est envisagée, elle doit être déposée avant la publication du code qui divulguerait l'invention, et la licence libre devra tenir compte des droits de brevet. Ne comptez jamais sur un délai de grâce : protégez avant de publier.

**Étape 10. Publier, soutenir, mesurer.** Une fois la licence choisie, diffusez le logiciel, annoncez-le dans les communautés concernées, répondez aux premières questions, publiez des versions régulières. Mesurez l'usage : téléchargements, citations, contributions, demandes commerciales. Réexaminez la stratégie chaque année, car un projet peut évoluer et justifier un autre modèle pour ses versions futures.

## 4. Erreurs à éviter

- **Publier le code avant de contacter le bureau de valorisation.** Le choix d'une licence devient alors irréversible pour les versions déjà diffusées, et les questions de propriété restent en suspens.
- **Choisir une licence par imitation.** Copier la licence d'un projet voisin, sans analyser ses dépendances ni ses objectifs, conduit à des conflits ou à des occasions manquées.
- **Mélanger des licences incompatibles.** Combiner un composant sous GPL avec du code destiné à une licence propriétaire expose l'établissement à des réclamations et empêche de commercialiser le produit.
- **Ignorer les contributeurs externes.** Sans accord de contribution, la double licence est impossible, et le moindre changement de licence suppose l'accord de chaque auteur.
- **Considérer « libre » comme « sans modèle économique ».** Le libre peut très bien s'accompagner de services, de support, d'hébergement, de versions avancées ou de formations payantes.
- **Négliger la maintenance.** Un logiciel publié sans équipe pour le soutenir devient vite obsolète et nuit à la réputation du laboratoire.
- **Promettre une exclusivité sur du code déjà libre.** Une licence exclusive n'a plus de sens pour une version déjà publiée sous licence ouverte. L'investisseur doit le comprendre, et la valeur se situe alors dans les améliorations, les services et le savoir-faire.
- **Oublier les conditions des financeurs.** Un bailleur peut imposer une licence ouverte, interdire certains usages ou exiger la déclaration du logiciel. Ces obligations s'imposent à l'établissement.

## 5. Application au contexte africain

### Un levier à fort impact et à faible coût

Pour les universités africaines, le logiciel est un moyen peu coûteux de produire un impact visible : applications de santé mobile, outils de gestion agricole, plateformes d'éducation en ligne, systèmes d'information géographique, modèles climatiques, traitement des langues africaines. Beaucoup de ces outils répondent à des besoins locaux que les grands éditeurs ne couvrent pas. Une licence libre permet une adoption rapide par des ministères, des organisations non gouvernementales, des coopératives et des écoles qui n'ont pas de budget de licences. Une licence commerciale ou une double licence permet de financer la maintenance auprès d'acteurs plus solvables.

### Le cadre juridique

Le logiciel est protégé par le droit d'auteur dans tous les États membres de l'OAPI, en application de l'annexe consacrée à la propriété littéraire et artistique de l'accord de Bangui, ainsi que dans les pays qui ont adhéré aux conventions internationales sur le droit d'auteur. La protection naît de la création, sans dépôt obligatoire, mais un enregistrement ou un dépôt auprès de l'organisme national de droit d'auteur facilite la preuve de l'antériorité. Un brevet OAPI ne couvre que les 17 États membres, et le logiciel en tant que tel n'est en général pas considéré comme une invention brevetable. Quant aux licences libres, leur valeur contractuelle repose sur les principes du droit d'auteur et sur le droit des contrats de chaque pays. Il est prudent de s'appuyer sur un juriste local pour vérifier leur application.

### Les politiques d'établissement

Peu d'universités africaines ont une règle claire sur les logiciels de recherche. Il est utile d'inclure dans la politique de propriété intellectuelle une section dédiée : qui est titulaire, quelle déclaration préalable, quelle licence par défaut selon la catégorie (outil de recherche, produit commercial, matériel pédagogique), quel partage des revenus avec les auteurs, quel rôle pour le bureau de valorisation. Certaines universités fixent une licence libre par défaut pour les logiciels financés par des fonds publics, avec la possibilité de dérogation motivée. D'autres créent un bureau dédié aux programmes open source, qui soutient les chercheurs dans l'animation de la communauté.

### Les partenaires et les communautés

Les réseaux de développeurs africains, les pôles d'innovation numérique, les incubateurs et les associations de logiciel libre constituent des relais précieux pour faire vivre un projet. Les programmes internationaux de coopération universitaire et les bailleurs favorisent souvent la diffusion ouverte. Les centres d'appui à la technologie et à l'innovation de l'OMPI peuvent conseiller sur le droit d'auteur et les licences. Les projets régionaux de valorisation de la recherche rassemblent des établissements qui peuvent mutualiser des modèles de licences et des formations.

### Un exemple type

Une école d'ingénieurs d'Afrique de l'Ouest développe un logiciel de traduction automatique entre le français et plusieurs langues nationales. Les données d'entraînement viennent de partenariats avec des radios locales et des associations. Le bureau de valorisation vérifie les droits sur les données, publie le code du moteur sous une licence permissive pour encourager son usage dans l'éducation et les médias, et réserve la version optimisée destinée aux opérateurs de téléphonie à une licence commerciale. Les contributeurs externes signent un accord de contribution. Une petite société locale propose le soutien technique et l'adaptation aux besoins des clients, et reverse une redevance à l'école.

## 6. Plan d'action

| Étape | Qui | Quand | Résultat attendu |
|---|---|---|---|
| Déclarer le logiciel au bureau de valorisation | Chercheur responsable | Avant toute publication | Dossier ouvert, publication suspendue le temps de l'analyse |
| Établir la titularité et signer les cessions nécessaires | Bureau, juriste, auteurs | Semaines 1 à 3 | Droits clairement attribués à l'établissement |
| Inventorier les composants tiers et leurs licences | Développeurs, bureau | Semaines 1 à 3 | Liste des dépendances et des contraintes |
| Définir l'objectif stratégique du logiciel | Chercheurs, bureau, direction | Semaine 3 à 4 | Décision écrite : adoption, revenus ou produit |
| Choisir la licence (permissive, copyleft, double, commerciale) | Bureau, juriste | Semaine 4 à 5 | Modèle de licence arrêté et motivé |
| Mettre en place l'accord de contribution et le guide | Bureau, développeurs | Semaine 5 à 6 | Règles pour les contributeurs externes |
| Préparer le dépôt public ou le contrat de licence commerciale | Développeurs, juristes | Semaines 5 à 8 | Documents prêts, fichiers de licence en place |
| Déposer la marque et examiner un brevet éventuel | Bureau, conseil en PI | Avant la publication | Nom protégé, inventions techniques préservées |
| Publier, animer la communauté, suivre l'usage | Équipe projet | Après publication, puis chaque année | Adoption mesurée, stratégie revue annuellement |

## Conclusion

Il n'existe pas de licence idéale pour tous les logiciels universitaires. Il existe une démarche : établir la propriété, connaître ses dépendances, clarifier l'objectif, choisir un modèle reconnu et soutenir le projet dans la durée. Une licence libre bien choisie peut donner à une équipe africaine une visibilité mondiale et des partenaires inattendus. Une licence commerciale ou double peut financer la maintenance et faire naître une entreprise locale. Dans les deux cas, la décision se prend avant la première publication, avec le bureau de valorisation, pas après. Les établissements qui structurent cette réflexion transforment leurs codes en actifs durables au service de la science et de la société.

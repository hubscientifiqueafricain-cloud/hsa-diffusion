---
sous_titre: Concevoir et financer des infrastructures de calcul partagées qui permettent aux laboratoires africains de transformer leurs données en résultats valorisables, sans dépendre de capacités étrangères.
meta_description: Calcul haute performance et cloud pour la recherche : comment des infrastructures mutualisées soutiennent la valorisation en Afrique.
mots_cles: calcul haute performance, cloud, infrastructures, mutualisation
---

# Les plateformes de calcul et le cloud pour la recherche

## Résumé

La recherche moderne produit et traite d'immenses volumes de données : génomique, climat, imagerie médicale, agronomie, langues, finance, ingénierie. Sans capacité de calcul, ces données restent inexploitées ou partent vers des plateformes étrangères, avec les résultats et la valeur qui les accompagnent. Ce livre blanc s'adresse aux décideurs publics. Il explique pourquoi le calcul est une infrastructure de valorisation, quels modèles de mutualisation ont fonctionné ailleurs, comment concevoir une plateforme nationale ou régionale, quelles erreurs éviter et comment articuler calcul haute performance, cloud public, cloud souverain et formation. Il propose une trajectoire réaliste, par étapes, adaptée aux contraintes d'énergie, de connectivité et de budget des pays africains, avec un accent sur l'usage réel par les chercheurs et par les entreprises issues de la recherche.

## 1. Le constat

Un laboratoire qui veut entraîner un modèle de prévision climatique, analyser des séquences génétiques de plusieurs milliers d'individus, simuler la propagation d'une maladie ou traiter des images satellitaires de cultures a besoin de puissance de calcul et de stockage. Les besoins varient : calcul haute performance pour les simulations lourdes, processeurs graphiques pour l'apprentissage profond, stockage de données volumineuses, outils d'analyse accessibles à distance.

En Afrique, la situation est contrastée. Quelques centres de calcul nationaux ou universitaires existent, notamment en Afrique du Sud, en Égypte, au Maroc, au Kenya, au Rwanda, au Sénégal ou en Tunisie. Mais beaucoup de chercheurs n'ont accès qu'à des ordinateurs individuels, à des serveurs vieillissants ou à des crédits ponctuels sur des plateformes étrangères. Les conséquences pour la valorisation sont nettes.

**Les projets s'arrêtent à la limite de la machine.** Un chercheur qui ne peut pas exécuter son analyse complète en un temps raisonnable se contente d'un échantillon, publie un résultat partiel ou renonce. Les travaux restent à l'état de preuve de principe.

**Les données et les résultats partent ailleurs.** Quand le calcul se fait sur des plateformes étrangères, les données, les modèles entraînés et parfois les droits sur les outils d'analyse suivent. L'institution africaine perd une partie de son contrôle sur son patrimoine scientifique et sur la valeur qui pourrait en découler.

**La fragmentation coûte cher.** Chaque université achète son petit serveur, souvent sous-utilisé, mal entretenu, sans administrateur dédié. Les coûts de maintenance, d'énergie et de sécurité sont multipliés, et la capacité totale reste faible.

**Les entreprises issues de la recherche ne peuvent pas passer à l'échelle.** Une jeune entreprise qui a développé un modèle dans un laboratoire doit pouvoir le faire tourner sur de vraies données, le tester et l'héberger. Sans infrastructure accessible à un coût raisonnable, elle se tourne vers des fournisseurs étrangers, souvent en devises, ou elle abandonne.

Les décideurs publics se demandent alors s'il faut investir dans des centres de calcul nationaux, miser sur le cloud commercial ou combiner les deux. La réponse dépend des usages, des moyens, des compétences disponibles et des enjeux de souveraineté. Une chose est certaine : sans pilotage, les investissements en matériel se dégradent vite, car la technologie vieillit en quelques années et l'entretien manque.

## 2. Ce que montrent les expériences

**La mutualisation nationale.** Plusieurs pays ont créé des centres de calcul partagés, ouverts à l'ensemble des universités et des centres de recherche, avec des règles d'accès, des programmes de formation et des équipes techniques. L'exemple du centre de calcul haute performance sud-africain, qui fédère des utilisateurs de nombreuses institutions, montre l'intérêt d'une structure nationale dotée d'une mission claire et d'un financement stable. D'autres pays africains ont développé des centres universitaires ouverts à des partenaires.

**Les infrastructures européennes et mondiales.** En Europe, des réseaux de calcul scientifique permettent aux chercheurs de postuler à des heures de calcul sur des machines puissantes, selon des critères d'excellence. Des initiatives de cloud scientifique fédèrent des services d'hébergement, d'analyse et de partage de données. Ces modèles montrent que l'accès par appel à projets et la fédération de ressources limitent les coûts et favorisent la collaboration.

**Le modèle hybride.** Les institutions qui réussissent combinent une capacité de calcul locale pour les besoins réguliers et sensibles, et des ressources de cloud public pour les pics de demande ou les outils spécialisés. Cette approche permet d'optimiser les coûts et de garder la maîtrise des données les plus stratégiques.

**La formation comme condition.** Les centres qui investissent dans la formation des utilisateurs, des administrateurs et des ingénieurs de recherche, par exemple à travers des écoles d'été, des programmes de certification et des stages, voient leur taux d'utilisation augmenter. Des réseaux communautaires de calcul en Afrique ont organisé des ateliers qui ont formé des centaines de jeunes chercheurs.

**Un cas type.** Un ministère de l'enseignement supérieur d'un pays d'Afrique de l'Est finance une salle de serveurs dans une université. Deux ans plus tard, la moitié des machines est inactive : le personnel manque, la climatisation est instable, les chercheurs ne savent pas comment demander de l'accès et les coupures de courant interrompent les calculs. Le ministère change d'approche. Il confie la gestion à une petite équipe nationale, finance un onduleur et une alimentation solaire d'appoint, publie des règles d'accès simples, lance un appel trimestriel de projets et organise des formations. La charge de la plateforme passe en un an de très faible à pleinement utilisée, et trois entreprises issues de laboratoires commencent à louer des heures de calcul.

**Un second cas type.** Un consortium de laboratoires de santé de trois pays voisins veut analyser des données génomiques. Chaque pays hésite à envoyer ses données à l'étranger. Le consortium met en place un nœud de calcul régional hébergé dans une université, avec un accord de gouvernance des données : chaque pays garde la maîtrise de ses jeux de données, l'analyse se fait sur place avec des outils partagés, et seuls les résultats agrégés sont publiés. Le modèle respecte les lois nationales et ouvre la voie à des partenariats avec l'industrie pharmaceutique.

> À retenir : une infrastructure de calcul ne vaut que par ses utilisateurs. La pérennité vient de l'équipe technique, de l'énergie, de la formation et d'un modèle de financement qui couvre les coûts récurrents, pas seulement l'achat initial.

## 3. Méthode pas à pas

**Étape 1. Mesurer la demande réelle.** Enquêtez auprès des universités, des centres de recherche, des start-ups et des administrations. Quels types de calcul, quels volumes de données, quelles échéances, quelles contraintes de confidentialité ? Ne dimensionnez pas sur des intentions vagues.

**Étape 2. Inventorier l'existant.** Recensez les serveurs, les centres de données, les liaisons réseau, les licences logicielles et les compétences. Un inventaire révèle souvent des capacités sous-utilisées qu'on peut fédérer.

**Étape 3. Choisir une architecture adaptée.** Combinez trois niveaux : un noyau national ou régional de calcul haute performance, des nœuds universitaires pour les besoins courants, et un accès négocié à des services de cloud pour les pointes et les outils spécialisés. Évaluez les coûts complets, énergie et personnel compris.

**Étape 4. Sécuriser l'énergie et le réseau.** Un centre de calcul sans alimentation fiable et sans connexion à un réseau académique à haut débit ne fonctionnera pas. Prévoyez des onduleurs, de l'énergie solaire ou un second raccordement, et une liaison avec le réseau national ou régional de la recherche et de l'enseignement.

**Étape 5. Mettre en place une gouvernance claire.** Définissez qui décide de l'accès, selon quels critères, avec quelles priorités. Un comité scientifique et technique, une charte d'utilisation et des indicateurs publics renforcent la confiance et évitent les captations.

**Étape 6. Encadrer les données.** Établissez des règles sur la classification des données, le stockage, la sécurité, la durée de conservation, le partage et le respect des lois sur les données personnelles. Précisez qui détient les droits sur les résultats et les outils développés. Pour les travaux susceptibles de donner lieu à une invention ou à un logiciel valorisable, prévoyez un lien avec le bureau de valorisation avant toute publication, car on ne peut pas compter sur un délai de grâce pour réparer une divulgation trop précoce.

**Étape 7. Construire le modèle économique.** Combinez financement public pour l'investissement de base, tarifs différenciés selon les utilisateurs (gratuit ou subventionné pour la recherche publique, payant pour les entreprises), contrats avec des partenaires et bailleurs. Prévoyez le renouvellement du matériel tous les quatre à six ans.

**Étape 8. Investir dans les personnes.** Recrutez et formez des administrateurs système, des ingénieurs de recherche, des spécialistes en calcul scientifique. Créez des parcours de carrière attractifs pour ne pas perdre ces profils au profit du secteur privé ou de l'étranger.

**Étape 9. Accompagner les utilisateurs.** Proposez des guides, des modèles de projets, des formations, une assistance et des exemples d'usage. Un guichet d'accueil réduit fortement l'obstacle de départ.

**Étape 10. Ouvrir aux entreprises issues de la recherche.** Offrez aux jeunes entreprises un accès à des conditions préférentielles pendant la phase de développement, avec des règles transparentes pour éviter la concurrence déloyale.

**Étape 11. Évaluer et ajuster.** Suivez le taux d'utilisation, le nombre de projets, de publications, de brevets, de licences et d'entreprises soutenues, la satisfaction des utilisateurs et le coût par heure de calcul. Publiez ces indicateurs.

## 4. Erreurs à éviter

- **Acheter du matériel avant de définir les usages.** Une machine puissante sans utilisateurs formés reste un investissement dormant.
- **Oublier les coûts récurrents.** L'énergie, la climatisation, la maintenance, les licences et le personnel dépassent souvent le prix d'achat sur la durée de vie.
- **Négliger la sécurité.** Une plateforme partagée est une cible. Les droits d'accès, les sauvegardes et la surveillance doivent être pensés dès le départ.
- **Dépendre d'un seul fournisseur.** Une stratégie qui repose sur un unique fournisseur étranger expose à des hausses de prix, à des interruptions et à des contraintes juridiques.
- **Ignorer la question des données sensibles.** Certaines données, de santé ou stratégiques, ne devraient pas quitter le territoire sans cadre juridique clair.
- **Construire en silo ministériel.** Enseignement supérieur, numérique, énergie, finances et santé doivent coordonner leurs plans.
- **Réserver l'accès aux grands laboratoires.** Un système d'accès équitable, fondé sur la qualité des projets, évite que les jeunes équipes soient exclues.
- **Ne pas mesurer.** Sans indicateurs, on ne sait ni justifier le financement ni corriger les défauts.
- **Sous-estimer la formation.** Beaucoup d'infrastructures sont sous-utilisées parce que les chercheurs ne savent pas s'en servir.

## 5. Application au contexte africain

**Une carte de capacités à fédérer.** Les pays qui disposent déjà de centres de calcul peuvent accueillir des utilisateurs d'autres pays par des accords bilatéraux ou régionaux. Les réseaux nationaux et régionaux de la recherche et de l'éducation, qui relient les universités à haut débit, constituent l'épine dorsale de cette coopération. Les organisations régionales et l'Union africaine peuvent soutenir la création de nœuds régionaux, avec des règles communes d'accès et de gouvernance des données.

**L'énergie comme contrainte et comme opportunité.** Dans de nombreux pays, l'accès à une électricité stable est la première difficulté. Les centres de données alimentés partiellement par l'énergie solaire, avec des stockages d'appoint, et conçus pour l'efficacité énergétique, répondent à la fois aux contraintes locales et aux engagements climatiques.

**Le cadre juridique des données.** La Convention de Malabo, les lois nationales sur les données personnelles et les règles sectorielles encadrent l'hébergement et le transfert. Les décideurs doivent préciser les catégories de données qui doivent rester sur le territoire et celles qui peuvent circuler. Le cloud souverain ou régional, opéré sous juridiction africaine, répond aux besoins de confiance pour les données publiques et de santé.

**La valorisation en ligne de mire.** Les offices de transfert et les cellules de valorisation doivent être associés dès la conception : un logiciel, un modèle entraîné ou une base de données de recherche peuvent être protégés par le droit d'auteur, le secret ou, selon les cas, un brevet. Un brevet déposé auprès de l'OAPI couvre les 17 États membres, pas les autres pays ; la stratégie doit tenir compte des marchés visés. Les plateformes de calcul peuvent même intégrer des services d'appui à la protection et à la licence.

**Les partenariats.** Des partenariats avec des universités étrangères, des programmes de coopération scientifique, des banques de développement, des fournisseurs de cloud commerciaux (sous conditions de transfert de compétences et de souveraineté sur les données) et des opérateurs de télécommunications peuvent financer et déployer des capacités. Le principe directeur est de négocier des accords qui renforcent les compétences locales, plutôt que de seulement louer de la puissance.

**La formation continentale.** Les écoles d'été, les programmes de master en calcul scientifique et en science des données, les bourses de stage dans des centres reconnus et les communautés d'utilisateurs forment la base humaine sans laquelle aucune infrastructure ne décolle.

**Penser à la valeur ajoutée des données locales.** Les jeux de données africains, qu'ils portent sur la santé, l'agriculture, les langues ou le climat, ont une valeur croissante pour l'entraînement de modèles. Une plateforme nationale peut devenir le point d'entrée contrôlé de cet actif : elle catalogue les jeux de données, définit les conditions d'accès pour les chercheurs et les entreprises, négocie le partage des retombées avec les détenteurs et veille à ce que les résultats servent aussi les besoins locaux. Cette politique de données, qui complète la politique d'infrastructure, est l'un des leviers les plus puissants pour éviter que le continent n'exporte ses données brutes et n'importe ensuite, à prix élevé, des services qui en sont issus.

**Mesurer le coût réel de l'inaction.** Un décideur peut comparer le coût d'une plateforme au montant que le pays dépense déjà, de façon dispersée, en abonnements étrangers, en achats de serveurs isolés et en séjours de chercheurs à l'étranger pour accéder à des machines. Cette comparaison, souvent favorable à la mutualisation, aide à convaincre les ministères des finances de consentir un investissement initial.

## 6. Plan d'action

| Étape | Qui | Quand | Résultat attendu |
|---|---|---|---|
| Enquêter sur les besoins et inventorier l'existant | Ministère de l'enseignement supérieur, agences de recherche | 0 à 4 mois | Cartographie de la demande et des capacités |
| Définir l'architecture hybride et le budget récurrent | Ministères du numérique, des finances et de l'énergie | 4 à 8 mois | Schéma directeur chiffré |
| Sécuriser énergie et liaison réseau | Opérateurs, réseau national de la recherche | 6 à 18 mois | Site alimenté et connecté |
| Créer la gouvernance et la charte d'accès | Comité scientifique et technique | 6 à 12 mois | Règles publiques d'attribution |
| Recruter et former l'équipe technique | Établissement hôte, partenaires | 6 à 18 mois | Équipe opérationnelle et plan de carrière |
| Ouvrir un premier appel à projets | Plateforme | 12 mois | Premiers projets de recherche hébergés |
| Définir les règles sur les données et la valorisation | Autorité de protection des données, offices de transfert | 8 à 14 mois | Charte de données et circuit de déclaration d'invention |
| Ouvrir l'accès aux jeunes entreprises et évaluer | Plateforme, incubateurs | 18 à 30 mois | Tableau de bord d'impact publié |

## Conclusion

Le calcul est devenu une infrastructure aussi essentielle pour la recherche que les laboratoires ou les bibliothèques. Un pays qui ne dispose d'aucune capacité de calcul accessible voit ses données, ses talents et ses résultats migrer vers d'autres. À l'inverse, des plateformes mutualisées, bien gouvernées, alimentées de façon fiable et portées par des équipes formées donnent aux laboratoires les moyens de transformer leurs données en connaissances, puis en produits et en entreprises. Les décideurs publics qui investissent maintenant, par étapes, dans l'infrastructure, les compétences et la gouvernance poseront les bases d'une valorisation de la recherche durable et maîtrisée par les Africains.

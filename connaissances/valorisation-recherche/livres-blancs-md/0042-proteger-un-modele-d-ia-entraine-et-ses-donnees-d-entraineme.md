---
sous_titre: Combiner droit d'auteur, secret d'affaires, contrats et brevet pour protéger les poids, les données et le code d'un modèle d'IA issu de la recherche.
meta_description: Protéger un modèle d'IA entraîné et ses données d'entraînement : droit d'auteur, secret, licence et brevet pour startups et incubateurs.
mots_cles: modèle d'IA, données d'entraînement, secret, licence
---

# Protéger un modèle d'IA entraîné et ses données d'entraînement

## Résumé

Un modèle d'intelligence artificielle issu d'un laboratoire ou d'un incubateur est un actif composite : du code, des paramètres appris (les poids), des jeux de données d'entraînement, une documentation, parfois une interface. Aucun outil juridique ne couvre à lui seul tous ces éléments. Ce livre blanc, destiné aux incubateurs et aux startups, présente une cartographie simple : ce que protège le droit d'auteur, ce que permet le secret d'affaires, ce qu'un contrat de licence ou de données peut verrouiller, et ce que le brevet peut apporter. Il propose une méthode pour inventorier ses actifs, choisir une stratégie adaptée au modèle économique, rédiger des licences cohérentes et éviter les erreurs qui font fuir les investisseurs : droits flous sur les données, composants sous licence incompatible, divulgation prématurée.

## 1. Le constat

Les jeunes entreprises d'IA, dont celles qui naissent dans les universités africaines, partagent une inquiétude : « que se passe-t-il si quelqu'un copie mon modèle ? ». La réponse est plus compliquée qu'on ne le croit, car le droit n'a pas été écrit pour ces objets. Plusieurs idées reçues circulent.

**Première idée reçue : un modèle serait protégé comme un logiciel.** Le code qui sert à entraîner et à faire fonctionner un modèle est bien protégé par le droit d'auteur, comme tout programme. Mais les poids, c'est-à-dire les millions de valeurs numériques issues de l'entraînement, ne sont pas écrits par un auteur humain au sens classique. Leur statut juridique est discuté et varie d'un pays à l'autre. On ne peut donc pas compter uniquement sur le droit d'auteur pour les protéger.

**Deuxième idée reçue : les données seraient la propriété de celui qui les a collectées.** Ce n'est pas aussi simple. Des faits bruts ne sont pas protégés en eux-mêmes. Une base de données peut l'être dans certains systèmes, par un droit spécifique ou par le droit d'auteur sur son organisation, mais pas partout. Dans beaucoup de cas, ce sont les contrats, la confidentialité et les mesures de sécurité qui font la valeur et la protection d'un jeu de données. Il faut aussi tenir compte des droits des tiers sur les données : droits des personnes concernées, droits des auteurs des contenus, conditions imposées par le fournisseur des données.

**Troisième idée reçue : il faudrait tout breveter.** Le brevet peut protéger un procédé technique nouveau et inventif, mais il impose de divulguer l'invention, il coûte cher à déposer et à maintenir, et il est territorial. Il ne s'applique pas à un algorithme pris isolément, dans de nombreux pays. Pour beaucoup de startups, ce n'est pas la première priorité.

**Quatrième idée reçue : si le modèle est publié, il est perdu.** Là encore, la réalité est nuancée. Beaucoup de projets réussis publient une partie de leurs travaux sous licence ouverte, et gagnent de l'argent sur les services, le support, les données propriétaires, l'intégration ou la version commerciale. Le choix entre ouverture et fermeture est une décision de modèle économique, pas un réflexe.

À cela s'ajoute un risque que l'on découvre souvent trop tard : la chaîne des droits. Un modèle bâti sur des composants dont les licences sont incompatibles, sur des données dont l'usage n'était pas autorisé, ou sur du code écrit par des étudiants et des consultants sans contrat, peut s'avérer invendable le jour où un investisseur ou un client vérifie. Un investisseur examine d'abord la liste de propriété intellectuelle et les licences. Toute incohérence éveille des soupçons.

## 2. Ce que montrent les expériences

### Les quatre couches d'un actif d'IA

Les équipes qui structurent bien leur propriété intellectuelle raisonnent par couches.

**Le code.** Il comprend les scripts d'entraînement, l'architecture, les outils de prétraitement, l'interface. Il est protégé par le droit d'auteur dès sa création, sans formalité, dans les pays membres de la convention de Berne, c'est-à-dire presque partout. Cette protection est utile contre la copie pure et simple, mais elle est étroite : elle n'empêche pas quelqu'un de réécrire un code différent qui fait la même chose.

**Les poids et la configuration du modèle.** Ils résultent d'un entraînement coûteux en temps, en données et en puissance de calcul. Plusieurs outils peuvent les couvrir ensemble : le secret d'affaires, tant que les poids ne sont pas divulgués et que des mesures raisonnables de confidentialité sont prises ; le contrat, par exemple des conditions d'accès par interface sans remise des poids ; et selon les pays, le droit d'auteur ou un droit sur les bases de données, dont l'application aux poids reste incertaine. Plus la valeur du modèle est élevée, plus il faut protéger ses poids par des mesures concrètes : contrôle d'accès, chiffrement, journalisation, clauses de confidentialité.

**Les données d'entraînement.** Les jeux de données peuvent être des données propres à l'équipe, des données obtenues d'un partenaire, des données publiques ou libres, des données synthétiques. Leur protection passe par le secret d'affaires, la sécurité informatique, le contrat de licence ou de partage et, dans certains systèmes, le droit des bases de données. Leur utilisation est encadrée par le droit de la protection des données personnelles, par le droit d'auteur sur les contenus collectés et par les conditions d'utilisation des plateformes d'où elles proviennent.

**Les inventions techniques.** Un procédé d'entraînement original, une architecture adaptée à un dispositif précis, un prétraitement qui améliore une mesure physique, une méthode qui commande un équipement peuvent être brevetables s'ils sont nouveaux, inventifs et appliqués à un problème technique. Les demandes qui visent un algorithme sans lien avec un effet technique sont régulièrement refusées. Il faut aussi se demander si l'on pourra détecter une contrefaçon : si l'étape brevetée se déroule à l'intérieur du système d'un concurrent, il sera difficile de la prouver, et le secret peut être préférable.

### Le secret d'affaires : puissant mais exigeant

Le secret d'affaires ne demande aucun dépôt, mais il exige un comportement. En cas de litige, le tribunal regarde les efforts faits pour garder l'information secrète. Si l'entreprise n'a pas pris de mesures sérieuses, la protection s'affaiblit ou disparaît. Les mesures usuelles sont les suivantes : accords de confidentialité pour toute personne ayant accès, politique de conservation des documents, sécurité physique et informatique (mots de passe, contrôle d'accès aux dépôts de code et de données, journalisation), marquage des documents confidentiels, procédure de départ des collaborateurs. Le secret protège tant que l'information n'est pas découverte légitimement : une rétro-ingénierie licite ne peut pas lui être opposée.

### La licence : l'outil qui fait vivre l'actif

Une licence organise l'usage d'un actif sans en céder la propriété. Pour un modèle d'IA, plusieurs formules coexistent :

- **L'accès par interface, sans remise des poids.** Le client utilise le modèle comme un service, aux conditions du contrat. L'entreprise garde la maîtrise de ses poids et de ses données.
- **La licence commerciale classique.** Elle fixe le périmètre d'usage, la durée, le territoire, la rémunération, les limites (usages interdits, nombre d'utilisateurs, revente).
- **La licence ouverte.** Les licences permissives imposent peu d'obligations. Les licences dites « copyleft » imposent de redistribuer les travaux dérivés sous les mêmes conditions et peuvent contenir des clauses de brevet. Une licence virale intégrée à un produit propriétaire peut obliger à publier son propre code. Il faut donc éviter ce type de licence dans un produit que l'on veut garder fermé, ou isoler soigneusement le composant concerné.
- **Les licences à usage limité,** qui autorisent la recherche ou un usage non commercial mais réservent l'exploitation commerciale à un accord séparé. Elles sont fréquentes pour les modèles issus de la recherche et conviennent bien aux universités qui veulent diffuser tout en gardant une porte ouverte aux partenariats commerciaux.
- **Les licences de données,** qui précisent ce que l'on peut faire des données, avec qui les partager et si les modèles entraînés en héritent.

### Penser le modèle économique avant de choisir la protection

Une startup qui vend un service d'IA à des clients et garde ses poids secrets n'a pas les mêmes besoins qu'une université qui publie un modèle de recherche pour être citée et attirer des partenaires. Les bureaux de transfert expérimentés recommandent de combiner plusieurs outils : droit d'auteur pour le code, secret pour les poids et les jeux de données, contrats pour l'accès, brevet pour une invention technique clé, marque pour le nom et l'identité. L'ordre de priorité dépend du marché, de la durée de vie du modèle (très courte dans un domaine qui évolue vite) et du budget.

> À retenir : on ne protège pas un modèle d'IA avec un seul outil. On protège un ensemble d'actifs avec une combinaison cohérente : droit d'auteur, secret, contrats et, quand c'est pertinent, brevet. Le plus coûteux est de découvrir trop tard que la chaîne des droits est brisée.

## 3. Méthode pas à pas

**Étape 1. Inventorier les actifs.** Dressez un tableau avec une ligne par composant : code d'entraînement, code d'inférence, architecture, poids, jeux de données bruts, jeux de données nettoyés, annotations, documentation, interface, marque, nom de domaine. Pour chacun, notez qui l'a créé, quand, avec quels moyens, et sous quel contrat.

**Étape 2. Retracer l'origine des droits.** Pour chaque composant, répondez à trois questions : qui détient les droits (l'établissement, l'entreprise, les auteurs, un partenaire, un tiers) ? Existe-t-il un contrat écrit (contrat de travail, convention de stage, contrat de consultant, accord de consortium, licence de données) ? Sous quelles conditions l'usage est-il autorisé ? Les étudiants et consultants sans contrat posent un risque particulier : sans accord écrit, la propriété du code et des données reste floue.

**Étape 3. Clarifier la relation avec l'université.** Un modèle né d'un laboratoire appartient souvent, au moins en partie, à l'établissement, qui détient les droits sur les créations de ses employés dans le cadre de leur mission. La startup a donc besoin d'une licence de l'université, qui doit couvrir non seulement les brevets éventuels mais aussi le code, le savoir-faire et les données. Négociez-la tôt. Une université ne peut pas céder à l'avance ses droits sur les améliorations futures ; un droit de première offre inscrit dans la licence est une solution courante.

**Étape 4. Vérifier les licences des composants.** Listez toutes les bibliothèques, modèles préentraînés et jeux de données utilisés, avec leur licence. Repérez les licences virales, les restrictions d'usage commercial, les clauses d'attribution. Remplacez les composants incompatibles avec votre modèle économique.

**Étape 5. Vérifier la légitimité des données.** Pour chaque jeu de données, vérifiez la base légale de la collecte, le consentement des personnes lorsque ce sont des données personnelles, les conditions des plateformes d'où proviennent les données collectées et les droits d'auteur des contenus. Documentez la provenance. Un modèle entraîné sur des données illégitimes expose à des demandes de retrait, voire de destruction du modèle.

**Étape 6. Choisir la stratégie par actif.** Pour chaque composant, décidez : à garder secret, à publier sous licence ouverte, à licencier commercialement, à breveter, à ne pas protéger. Écrivez la logique en une page : pourquoi ce choix correspond au modèle économique.

**Étape 7. Mettre en place les mesures de secret.** Rédigez des accords de confidentialité types, restreignez l'accès aux poids et aux données, tenez un registre des accès, formez les équipes. Si vous souhaitez participer à un concours de pitch ou à une démonstration, ne divulguez que les bénéfices et les résultats, pas l'architecture exacte ni les paramètres.

**Étape 8. Évaluer l'opportunité d'un brevet.** Si une innovation technique précise mérite protection, consultez un mandataire avant toute publication ou mise en ligne. Un dépôt de code sur une plateforme publique avant la demande de brevet est une divulgation qui peut faire perdre le droit. Ne comptez jamais sur un délai de grâce : protéger avant de publier. Un brevet de l'Organisation africaine de la propriété intellectuelle couvre les dix-sept États membres de cette organisation, pas le reste du monde.

**Étape 9. Rédiger les contrats.** Préparez des conditions générales d'utilisation, une licence type pour les clients, un modèle de contrat de partage de données, des clauses sur la propriété des améliorations, sur la confidentialité, sur la responsabilité et sur l'usage des sorties du modèle. Faites relire par un juriste.

**Étape 10. Tenir un dossier de preuves.** Conservez des cahiers de développement datés, les historiques de versions, les journaux d'entraînement, les contrats signés. En cas de diligence d'un investisseur ou de litige, ce dossier fait gagner des semaines.

## 4. Erreurs à éviter

- **Publier les poids ou le code sans décision stratégique.** Une fois diffusés sous licence ouverte, ils ne se reprennent pas.
- **Compter sur un seul outil juridique.** Le droit d'auteur seul, ou le brevet seul, laisse des trous.
- **Négliger les contrats avec les collaborateurs.** Étudiants, stagiaires, consultants et prestataires doivent signer des accords écrits de cession ou de licence et de confidentialité.
- **Intégrer une licence virale dans un produit fermé.** C'est l'une des causes les plus fréquentes de blocage lors d'une levée de fonds.
- **Utiliser des données sans en avoir le droit.** Le risque juridique, réputationnel et commercial est considérable.
- **Divulguer l'architecture dans un concours ou un article avant protection.** Présentez le bénéfice, pas la recette.
- **Oublier que les startups dépendent de la licence de l'université.** Sans elle, la société ne possède rien au premier jour.
- **Faire déposer une demande au nom d'un fondateur.** Si un fondateur dépose à son nom, la société n'a pas le droit d'utiliser l'invention sans transfert ou licence.
- **Ignorer la sécurité informatique.** Le secret d'affaires s'évanouit si les poids se retrouvent sur un serveur sans protection.
- **Laisser des outils d'IA externes lire des informations confidentielles.** Vérifiez les conditions d'usage et préférez des versions validées.

## 5. Application au contexte africain

**Un contexte juridique hétérogène.** Les pays africains sont membres de la convention de Berne, donc le droit d'auteur sur le code existe presque partout, sans formalité. Les lois sur le droit d'auteur ont été modernisées dans plusieurs pays, comme en Côte d'Ivoire, avec un texte de 2016. Les organismes de gestion collective existent surtout pour la musique et les œuvres artistiques ; ils sont peu mobilisés pour le code. Pour les brevets, l'Organisation africaine de la propriété intellectuelle (OAPI) délivre un titre valable dans dix-sept États, l'ARIPO couvre d'autres pays, et les offices nationaux s'appliquent ailleurs. Les règles sur les programmes d'ordinateur et les méthodes mathématiques sont à vérifier auprès de l'office concerné.

**La protection des données personnelles.** De nombreux pays africains ont adopté des lois de protection des données. La convention de l'Union africaine sur la cybersécurité et la protection des données personnelles, dite convention de Malabo, fournit un cadre régional. Des pays comme la Côte d'Ivoire, le Nigeria, le Kenya, l'Afrique du Sud ou le Sénégal disposent d'autorités de protection. Une startup qui entraîne un modèle sur des données de santé, d'agriculture ou de téléphonie doit en tenir compte dès la conception.

**Le rôle des incubateurs et des universités.** Un incubateur qui accompagne des startups d'IA peut proposer un kit de démarrage : modèle de licence, accord de confidentialité, grille d'inventaire des actifs, liste de contrôle des licences de composants, liste de mandataires et de juristes. Les universités peuvent préparer une licence standard pour les startups issues de leurs laboratoires, avec des conditions adaptées : paiements différés, prise de participation modeste, jalons réalistes. Les expériences étrangères montrent que les jeunes entreprises préfèrent un financement différé à un paiement initial lourd.

**La question des données locales.** Les langues africaines, les maladies tropicales, les cultures et les sols sont peu représentés dans les grands jeux de données mondiaux. Les chercheurs qui constituent de tels jeux détiennent un actif rare. Ils doivent décider s'ils les partagent en accès ouvert, sous licence limitée ou sous contrat, et garantir que les communautés concernées bénéficient d'un retour. L'équilibre entre science ouverte et protection des actifs se règle au cas par cas, avec le principe « aussi ouvert que possible, aussi fermé que nécessaire ».

**Les financements et les concours.** Les concours d'innovation, les programmes d'accélération et les fonds de maturation sont des occasions de visibilité, mais aussi de divulgation. Préparez un résumé non confidentiel, n'exposez pas l'architecture exacte, et déposez avant si un brevet est envisagé.

**Les ressources de formation.** Les cours à distance de l'Académie de l'OMPI, les ateliers des offices nationaux, les centres d'appui à la technologie et à l'innovation et les réseaux d'incubateurs proposent des formations. Un fondateur qui consacre quelques jours à ces bases évite des erreurs coûteuses.

## 6. Plan d'action

| Étape | Qui | Quand | Résultat attendu |
|---|---|---|---|
| Inventaire des actifs (code, poids, données, marque) | Fondateurs, incubateur | Semaines 1 à 2 | Tableau des composants et de leurs auteurs |
| Retracer l'origine des droits et signer les contrats manquants | Fondateurs, juriste | Semaines 2 à 4 | Cession ou licence écrites pour chaque contributeur |
| Négocier la licence avec l'université | Fondateurs, bureau de valorisation | Mois 1 à 3 | Licence couvrant code, savoir-faire et données |
| Audit des licences de composants et des données | Équipe technique, juriste | Mois 1 à 2 | Liste des conflits et plan de remplacement |
| Choisir la stratégie par actif | Fondateurs, conseil | Mois 2 | Note d'une page : secret, licence, brevet ou ouverture |
| Mettre en place les mesures de secret et de sécurité | Équipe technique | Mois 2 à 3 | Accès restreints, accords de confidentialité, journalisation |
| Évaluer un dépôt de brevet avant toute publication | Mandataire, fondateurs | Avant tout concours ou article | Décision documentée, dépôt éventuel |
| Rédiger les licences et conditions d'utilisation | Juriste | Mois 3 à 4 | Contrats types prêts pour les premiers clients |
| Revue annuelle et préparation de la diligence investisseur | Fondateurs, conseil | Chaque année | Dossier de preuves à jour |

## Conclusion

Protéger un modèle d'IA, c'est assembler des outils, pas en choisir un. Le droit d'auteur couvre le code, le secret d'affaires protège les poids et les données tant qu'on les garde réellement, les contrats organisent l'usage et le brevet couvre, quand il est pertinent, l'innovation technique. Cette combinaison n'a de valeur que si la chaîne des droits est saine : contrats signés, licences compatibles, données légitimes. Les startups africaines qui font ce travail dès le départ gagnent la confiance des clients et des investisseurs, et gardent la maîtrise de ce qu'elles ont bâti. Prenez le temps de cartographier, de décider et d'écrire : c'est le meilleur investissement juridique d'une jeune entreprise d'IA.

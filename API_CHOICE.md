# API Choice

- Étudiant : nicknick

- API choisie : Cat Facts API

- URL base : https://catfact.ninja

- Documentation officielle / README : https://catfact.ninja/

- Auth : None

- Endpoints testés :
  - GET https://catfact.ninja/fact
  - GET https://catfact.ninja/facts

- Hypothèses de contrat (champs attendus, types, codes) :
L'API doit répondre avec un code HTTP 200 lorsque la requête est valide.  
La réponse JSON de l’endpoint /fact doit contenir un champ "fact" de type string contenant un fait sur les chats et un champ "length" de type integer indiquant la longueur du texte.

- Limites / rate limiting connu :
Aucune limite stricte documentée pour un usage simple. L'API est publique et gratuite mais peut limiter les requêtes en cas d'abus.

- Risques (instabilité, downtime, CORS, etc.) :
Comme toute API publique, il peut y avoir des périodes de maintenance ou d'indisponibilité. Le temps de réponse peut également varier selon la charge du serveur.

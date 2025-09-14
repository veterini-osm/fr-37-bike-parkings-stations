# Format des données

Le fichier `stationnement-cyclable-gares-serm.geojson` est généré à partir des données d'OpenStreetMap.
Toute réutilisation de ce fichier doit comprendre la mention [© OpenStreetMap](https://www.openstreetmap.org/copyright/) avec un lien vers la page <https://www.openstreetmap.org/copyright/>,
ou, sur un support papier, la mention `© OpenStreetMap — Licence ODbl` présente de façon visible.

Ce fichier GeoJSON comprend toutes les propriétés / tags des gares présents dans OpenStreetMap, et dont la documentation peut être trouvée sur le [Wiki OpenStreetMap](https://wiki.openstreetmap.org/).
Il possède également les propriétés suivantes, agrégées à partir des tags de stationnements cyclables et services vélos d'OpenStreetMap, dans un rayon de 200 mètres autour de ces gares.
(Le second niveau d'imbrication de la liste indique quels tags OpenStreetMap sont utilisés pour chaque propriété du fichier GeoJSON.)

- `bicycle_total_capacity` : Le nombre total de places de stationnement vélos, incluant les stationnements fermés, privés, sur inscription ou réservés à la clientèle d'un commerce.
- `bicycle_free_capacity` : Le nombre de places de stationnement vélos librement accessible.
    - `locked=no` ou `locked` indéfini dans OpenStreetMap
    - `fee=no` ou indéfini
    - `access` non défini ou valeur différente de `members`, `customers`, `private` et `no`
- `bicycle_locked_capacity` : Le nombre de places dans un abri ou box fermé.
    - `locked=yes`
- `bicycle_charging_capacity` : Le nombre de places disposant d'une recharge pour vélos à assistance électrique.
    - Somme des valeurs de `capacity:charging` sur des parkings vélos (`amenity=bicycle_parking`)
- `bicycle_good_capacity` : Le nombre de places dont le type d'accroche est de bonne qualité.
    - Somme des tags `capacity` sur des objets dont le tag `bicycle_parking` a une des valeurs `stands`, `bollard`, `two-tier`, `lockers`, `safe_loops` ou `wide_stands`...
    - ...et des tags de capacité spécifique par type d'accroche (par exemple `capacity:bollard=...`, `capacity:stands=...`), s'ils existent. Ces tags sont utilisés dans le cas d'abris avec plusieurs types d'accroche différents
- `bicycle_free_good_capacity` : Le nombre de places dont le type d'accroche est de bonne qualité et librement accessible.
    - Il s'agit de l'intersection des stationnements éligibles à `bicycle_good_capacity` et à `bicycle_free_capacity`
- `bicycle_has_tools` : `1` si la station est équipée d'outils d'auto-réparation pour vélos, `0` sinon
    - Présence du tag `service:bicycle:tools` avec la valeur `yes` ou `separate` sur n'importe quel objet autour de la gare
- `bicycle_has_pump` : `1` si la station est équipée de pompe pour vélos, `0` sinon
    - Présence du tag `service:bicycle:pump` avec la valeur `yes` ou `separate` sur n'importe quel objet autour de la gare

# Bicycle Parking Stations near Train Stations

🗺️ **Check out the map on [uMap](https://umap.openstreetmap.fr/fr/map/stationnement-velo-des-gares-du-serm-de-touraine-a_1258078)!** 🚆🚴
 
This repository produces daily aggregate data on bicycle parkings around train stations in Indre-et-Loire, France, and the surrounding 
[SERM de Touraine area](https://www.concertation-serm-touraine.fr/fr/le-serm-de-touraine).
A nightly CI job runs [an Overpass query](https://github.com/veterini-osm/fr-37-bike-parkings-stations/blob/c9744298086378a953f924b575dd9f299b6cbe63/main.py#L5),
to retrieve the total bicycle parking capacity, and other bicycle features around each train station.
The response is converted to a valid GeoJSON file and uploaded to [data.gouv](https://www.data.gouv.fr/datasets/stationnement-velos-autour-des-gares-du-futur-serm-rer-de-touraine-openstreetmap).

## Why a script? Isn't Overpass enough?

Advanced Overpass requests with `make` or `convert` can indeed produce aggregate data, and their responses are quite similar to GeoJSON.
However, uMap cannot parse those responses that are too far from conventional Overpass OSM responses, and are not valid GeoJSON either.

This script simply tweaks the Overpass response to produce a valid GeoJSON file and uploads it somewhere so that uMap can access it.
As a bonus side effect, aggregate data is available for anyone to use on data.gouv!
 
For more info, check out [this issue](https://github.com/drolbr/Overpass-API/issues/761).

## Aknowledgement

- [OpenStreetMap](https://www.openstreetmap.org/copyright): bicycle parking data, train stations, city boundaries & much more! For this project, I created and updated many bicycle parkings around train stations in Indre-et-Loire, France, on OpenStreetMap
- [Pikamap](https://pikamap.fr/article/overpass-surcharge-voici-une-instance-france-disponible-librement) (FR): for providing an alternative to the overcrowded Overpass Turbo instance (France only)

## Author

Vétérini – [an OpenStreetMap contributor](https://www.openstreetmap.org/user/V%C3%A9t%C3%A9rini)

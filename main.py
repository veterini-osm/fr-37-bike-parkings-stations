import json
import requests

APP_USER_AGENT = "https://github.com/veterini-osm/fr-cvl-37-bike-parkings-stations"
INPUT_URL = "https://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%0A%0A%28%0A%20%20area%28id%3A3600007408%29%3B%0A%20%20area%28id%3A3600272368%29%3B%0A%20%20area%28id%3A3606958705%29%3B%0A%20%20area%28id%3A3602154088%29%3B%0A%20%20area%28id%3A3600107629%29%3B%0A%29-%3E.searchArea%3B%0A%0A%2F%2F%20Get%20all%20stations%20or%20halts%20in%20the%20area%20%28except%20touristic%20trains%29%0A%28%0A%20%20nwr%5Brailway%3Dstation%5D%5Boperator%21%3D%22Train%20Touristique%20de%20la%20Vall%C3%A9e%20du%20Loir%22%5D%28area.searchArea%29%3B%0A%20%20nwr%5Brailway%3Dhalt%5D%5Boperator%21%3D%22A.E.C.F.M%22%5D%28area.searchArea%29%3B%0A%29-%3E.allStations%3B%0A%0A%2F%2F%20Exclude%20a%20few%20stations%20beyond%20the%20scope%20of%20SERM-T%0A%28%0A%20%20nwr.allStations%0A%20%20%5Bname%21%3D%22Chenonceaux%22%5D%0A%20%20%5Bname%21%3D%22La%20Chauss%C3%A9e-Saint-Victor%22%5D%0A%20%20%5Bname%21%3D%22M%C3%A9nars%22%5D%3B%0A%29%20-%3E.stations%3B%0A%0Aforeach%20.stations-%3E.station%20%7B%0A%20%20nwr%28around.station%3A200%29%5Bamenity%3Dbicycle_parking%5D%5Bbicycle_parking%21%3Dfloor%5D-%3E.bp%3B%0A%20%20nwr.bp%28if%3Ais_number%28t%5B%22capacity%22%5D%29%29-%3E.bpc%3B%0A%20%20nwr.bpc%5Blocked%3Dyes%5D-%3E.locked_bpc%3B%0A%20%20nwr.bpc%5Blocked%21%3Dyes%5D%5Bfee%21%3Dyes%5D%5Baccess%21%3Dcustomers%5D-%3E.free_bpc%3B%0A%20%20%28%0A%20%20%20nwr.bpc%5Bbicycle_parking%3Dstands%5D%3B%0A%20%20%20nwr.bpc%5B%22capacity%3Astands%22%5D%3B%0A%20%20%20nwr.bpc%5Bbicycle_parking%3Dbollard%5D%3B%0A%20%20%20nwr.bpc%5B%22capacity%3Abollard%22%5D%3B%0A%20%20%20nwr.bpc%5Bbicycle_parking%3D%22two-tier%22%5D%3B%0A%20%20%20nwr.bpc%5B%22capacity%3Atwo-tier%22%5D%3B%0A%20%20%20nwr.bpc%5Bbicycle_parking%3Dlockers%5D%3B%0A%20%20%20nwr.bpc%5B%22capacity%3Alockers%22%5D%3B%0A%20%20%20nwr.bpc%5Bbicycle_parking%3Dsafe_loops%5D%3B%0A%20%20%20nwr.bpc%5B%22capacity%3Asafe_loops%22%5D%3B%0A%20%20%20nwr.bpc%5Bbicycle_parking%3Dwide_stands%5D%3B%0A%20%20%20nwr.bpc%5B%22capacity%3Awide_stands%22%5D%3B%0A%20%20%29-%3E.good_bpc%3B%0A.station%20convert%20Feature%20%0A%20%3A%3Ageom%20%3D%20center%28geom%28%29%29%2C%0A%20%3A%3A%20%3D%20%3A%3A%2C%0A%20id%20%3D%20id%28%29%2C%0A%20bicycle_total_capacity%20%3D%20bpc.sum%28t%5B%22capacity%22%5D%29%2C%0A%20bicycle_free_capacity%20%3D%20free_bpc.sum%28t%5B%22capacity%22%5D%29%2C%0A%20bicycle_locked_capacity%20%3D%20locked_bpc.sum%28t%5B%22capacity%22%5D%29%2C%0A%20bicycle_good_capacity%20%3D%20good_bpc.sum%28t%5B%22capacity%22%5D%29%3B%0A%20out%20geom%3B%0A%7D%0Aout%20geom%3B"
OUTPUT_FILE = "output.geojson"

class InvalidJsonException(Exception):
    pass

def fetch_osm(url: str)  -> dict[str, any]:
    return requests.get(url, {"user-agent": APP_USER_AGENT}).json()

def osm_json_to_geojson(json_data: dict[str, any]) -> dict[str, any]:
    if (len(json_data) == 0):
        raise InvalidJsonException("Empty JSON")

    output_data = dict()
    output_data["type"] = "FeatureCollection"
    output_data["features"] = [{ "type": "Feature", "geometry": element["geometry"], "properties": element["tags"] } for element in json_data["elements"]]

    return output_data

def write_geojson(data: dict[str, any]) -> None:
    with open(OUTPUT_FILE, "w") as output_file:
        json.dump(data, output_file)


if __name__ == "__main__":
    osm_json = fetch_osm(INPUT_URL)
    geojson = osm_json_to_geojson(osm_json)
    write_geojson(geojson)


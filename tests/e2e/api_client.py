import requests
from building import config


def post_to_add_building(name, address, zipcode, city, province):
    url = config.get_api_url()
    r = requests.post(
        f'{url}/building',
        json={"name": name, "address": address, "zipcode": zipcode, "province": province, "city": city}
    )
    return r


def post_to_add_building_section(building_id, floor, room):
    url = config.get_api_url()
    r = requests.post(
        f'{url}/building/section',
        json={"building_id": building_id, "floor": floor, "room": room}
    )

    assert r.status_code == 201


def post_to_add_lead_data(building_section_id, location, sample_id, paint_colour, lead_concentration, calibration, standard_reading, lead_present, analysis, notes):
    url = config.get_api_url()
    r = requests.post(
        f'{url}/building/section',
        json={"building_section_id": building_section_id,
              "location": location,
              "sample_id": sample_id,
              "paint_colour": paint_colour,
              "lead_concentration": lead_concentration,
              "calibration": calibration,
              "standard_reading": standard_reading,
              "lead_present": lead_present,
              "analysis": analysis,
              "notes": notes}
    )

    assert r.status_code == 201

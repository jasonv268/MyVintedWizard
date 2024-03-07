import json
import numpy as np

from pathlib import Path

path_brand = Path("filters_manager/ressources/brand.json")
path_catalog = Path("filters_manager/ressources/catalog.json")
path_size = Path("filters_manager/ressources/size.json")
path_color = Path("filters_manager/ressources/color.json")
path_material = Path("filters_manager/ressources/material.json")
path_status = Path("filters_manager/ressources/status.json")
path_order = Path("filters_manager/ressources/order.json")


def get_dict(path):
    with open(path, 'r') as json_file:
        return json.load(json_file)


def get_brand_assoc():
    data = get_dict(path_brand)
    return {elt['id']: elt['title'] for elt in data}


def get_catalog_assoc():
    def get_catalog_rec(catalog):
        liste = {}
        for cata in catalog['catalogs']:
            liste = liste | get_catalog_rec(cata)
        return {str(catalog['id']): catalog['title']} | liste

    data = get_dict(path_catalog)
    dico = {}
    for cat in data[0:3]:
        dico = dico | get_catalog_rec(cat)

    return dico


def get_size_assoc():
    data = get_dict(path_size)
    dico = {}
    for elt in data:
        dico = dico | {size['id']: size['title'] for size in elt['sizes']}

    return dico


def get_color_assoc():
    data = get_dict(path_color)
    return {elt['id']: elt['title'] for elt in data}


def get_material_assoc():
    data = get_dict(path_material)
    return {mat['id']: mat['title'] for mats in [elt['materials'] for elt in data] for mat in mats}


def get_status_assoc():
    data = get_dict(path_status)
    return {elt['id']: elt['title'] for elt in data}


def get_order_assoc():
    data = get_dict(path_order)
    return {key: value for key, value in data.items()}


def format_for_choices(dico):
    return [(key, value) for key, value in dico.items()]


def reverse_dict(dico):
    return {value: key for key, value in dico.items()}

import re

import pandas as pd
from bs4 import BeautifulSoup
from stats_manager.utils.parsing.HtmlElement import HtmlElement


def format_price(string):
    val = (string.split(u'\xa0')[0]).replace(",", ".")
    return float(val)


def parse_page_articles(page: bytes) -> pd.DataFrame:
    """
    Parses data from an HTML page and return it as a DataFrame

    Args:
        page (bytes): utf-8 encoded HTML page

    Returns:
        pd.DataFrame: Parsed data

    """

    id_pattern = re.compile(r'^product-item-id-\d+$')
    username_pattern = re.compile(r'^product-item-id-\d+--owner$')
    price_pattern = re.compile(r'^product-item-id-\d+--price-text$')
    likes_pattern = re.compile(r'^product-item-id-\d+--favourite-count$')
    size_pattern = re.compile(r'^product-item-id-\d+--description-title$')
    brand_pattern = re.compile(r'^product-item-id-\d+--description-subtitle$')
    link_pattern = re.compile(r'^product-item-id-\d+--overlay-link$')

    # paths = {"id": ("div", {"data-testid": id_pattern}, ("data-testid", get_id)),
    #          "username": ("div", {"data-testid": username_pattern}, ("txt", None)),
    #          "price": ("h3", {"data-testid": price_pattern}, ("txt", format_price)),
    #          "likes": ("span", {"data-testid": likes_pattern}, ("txt", None)),
    #          "size": ("h4", {"data-testid": size_pattern}, ("txt", None)),
    #          "brand": ("h4", {"data-testid": brand_pattern}, ("txt", None)),
    #          "link": ("a", {"data-testid": link_pattern}, ("href", lambda x: x))}

    html_elements = [HtmlElement("id", "div", {"data-testid": id_pattern}, "data-testid", lambda x: x.split("-")[-1]),
                     HtmlElement("username", "div", {"data-testid": username_pattern}, "text", None),
                     HtmlElement("price", "p", {"data-testid": price_pattern}, "text", format_price),
                     HtmlElement("likes", "span", {"data-testid": likes_pattern}, "text", None),
                     HtmlElement("size", "p", {"data-testid": size_pattern}, "text", None),
                     HtmlElement("brand", "p", {"data-testid": brand_pattern}, "text", None),
                     HtmlElement("link", "a", {"data-testid": link_pattern}, "href", lambda x: x)]

    table = dict()
    for ele in html_elements:
        table[ele.get_name()] = []

    soup = BeautifulSoup(page, "html.parser")

    main_grid = HtmlElement("main_grid", "div", {"class": "feed-grid"})

    grid_items = HtmlElement("grid_items", "div", {"class": "feed-grid__item"})

    main_grid_soup = soup.find(main_grid.get_beacon(), main_grid.get_attr_to_value())
    grid_items = main_grid_soup.find_all(grid_items.get_beacon(), grid_items.get_attr_to_value())

    for item in grid_items:
        for ele in html_elements:
            table[ele.get_name()].append(get_value(item, ele))

    return pd.DataFrame(table)


def get_value(soup, html_element: HtmlElement):
    val = soup.find(html_element.get_beacon(), html_element.get_attr_to_value())

    if val is None:
        return "NotFound"

    match (html_element.get_data_to_be_collected()):
        case "text":
            value = val.text
        case data:
            value = val.attrs.get(data)

    if f := html_element.get_format_function():
        value = f(value)

    return value

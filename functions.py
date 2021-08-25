#-- Community Libraries --#
import requests as r
from bs4 import BeautifulSoup as bs
from classes import *


def get_meanings(soup):
    meanings = soup.find_all("span", class_="meaning-meaning")
    string = ""
    counter = 1
    for meaning in meanings:
        string += f"{counter}. {meaning.text.strip()}"
        counter+=1
        string += ", \n" if counter <= len(meanings) else ""
    return f"{string}"

def JSON(entries):
    output = "{\n\t\"entries\":[\n"
    counter = 0
    for entry in entries:
        output += entry.JSON()
        counter+=1
        output += ",\n" if counter < len(entries) else ""
    return f"{output}\n\t]\n}}"

def get_furigana(soups):
        furiganas = soups.find_all("span", class_="furigana")
        for furigana in furiganas:
            return furigana.text.strip()

def get_kanji(soups):
    kanji = soups.find("span", class_="text").text
    return kanji.strip()

def get_common(soup):
    try:
        common = soup.find("span", class_="concept_light-tag concept_light-common success label").text.strip()
    except:
        common = "nope"
    return True if common == "Common word" else False

def get_jlpt(soup):
    try:
        jlpt = soup.find("span", class_="concept_light-tag label").text.strip()
    except:
        jlpt = ""
    return jlpt

def get_classes(soup):
    try:
        classes = soup.find("div", class_="meaning-tags").text.strip()
    except:
        classes = ""
    return classes

def search(query):
    url = f"https://www.jisho.org/search/{query}"
    page = r.get(url)
    soups = bs(page.content, "html.parser")
    soups = soups.find(id="primary")
    return soups.find_all("div", class_="concept_light clearfix")

def parse_search(soups):
    entries = [] #define empty list

    for soup in soups: #for each html div from above, create dictionary_entry, add to empty entries list
        entries.append(dictionary_entry(
            get_furigana(soup),
            get_kanji(soup),
            get_common(soup),
            get_jlpt(soup),
            get_meanings(soup),
            get_classes(soup)
        ))
    
    return entries
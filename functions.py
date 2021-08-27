#-- Community Libraries --#
from profile import Profile
import requests as r
from bs4 import BeautifulSoup as bs
import cProfile, pstats, io
from classes import *

def profile(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable
        s = io.StringIO()
        sortby = "cumulative"
        ps=pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        f = open("debug.txt", "a")
        f.write(s.getvalue())
        f.close()
        return retval
    return inner

def get_meanings(soup):
    meanings = soup.find_all("span", class_="meaning-meaning")
    list_ = list(map(lambda x : x.text.strip(), meanings))
    output = ", \n".join(list_)
    return output

def JSON(entries):
    output = "{\n\t\"entries\":[\n"
    list_ = list(map(lambda x : x.JSON(), entries))
    output = ",\n".join(list_)
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

def search(session, query):
    url = f"https://www.jisho.org/search/{query}"
    page = session.get(url)
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
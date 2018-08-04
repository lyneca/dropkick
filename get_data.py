import requests as req
import sys
import re

def unwrap(thing):
    if thing:
        return format_dependencies(thing)
    else:
        return "None"

def format_dependencies(string):
    string = string.upper()

    string = " ".join(re.findall(r" OR |\w{4}\d{4}", string))
    string = re.sub(r" {2,}", " ", string)
    #  string = string.replace(" OR ", "|")
    #  string = string.replace(" AND ", "&")
    #  string = string.replace(" ", "")
    return string.split(" OR ")

def strip_html(text):
    return re.sub(r"<p.+?>|</p>", "", text.split("  ")[-1])

def get_part(content, part):
    result = re.findall(r"<span class=\"b-paragraph b-text--bold\">{}.+?</p>".format(part), content)
    if result:
        return strip_html(result[0])
    return None

def data_from_unit(code):
    code = code.lower()
    content = req.get("https://sydney.edu.au/courses/units-of-study/2018/{}/{}.html".format(code[:4], code)).content.decode()

    content = content.replace('\n', '')
    prereqs = get_part(content, "Pre-")
    coreqs = get_part(content, "Co-")
    prohibs = get_part(content, "Pro")
    assumed = get_part(content, "Assumed")

    print("Unit {}:".format(code.upper()))

    print("  Pre-requisites:", unwrap(prereqs))
    print("  Co-requisites: ", unwrap(coreqs))
    print("  Prohibitions:  ", unwrap(prohibs))
    print("  Ass. Knowledge:", unwrap(assumed))


while True:
    unit = input("Unit: ")
    print()
    data_from_unit(unit)
    print()

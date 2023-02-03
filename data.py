import re
import json
from itertools import cycle
def get_student(soup):
    """create list with each student result from html
    :param soup:
    :return: list with student grades and data
    """
    student = []
    soup = soup.select('tbody > tr ')
    table = soup[0]
    for td in table.findAll('td'):
        match = re.findall(f"(>.+<)", str(td))
        match = str(match)[3:(len(str(match)) - 3)]
        student.append(match)
    return student

def get_list(students):
    """create list with tuples for each student
    :param: students list with student results output from get_student"""
    keys =["Codul canditatului",
            "Scoala de provenienta",
            "Nota Lb. Romana",
            "Nota contestatie Lb.Romana",
            "Nota finala Lb. Romana",
            "Nota Matematica",
            "Nota contestatie Matematica",
            "Nota finala Matematica",
            "Denumire Lb. Materna",
            "Nota Lb. Materna",
            "Nota contestatie Lb.Materna",
            "Nota finala Lb. Materna",
            "Media finala"]
    result = list(zip(cycle(keys), students))
    return result

def write_output(data):
    """ creates json file output
     :param data: color codes list
     """
    with open('output_data.json', 'a', encoding='UTF-8') as json_file:
        json_object = json.dumps(data)
        json_file.write(f"\n{json_object}")
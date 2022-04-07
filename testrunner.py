from bs4 import BeautifulSoup
from copy import deepcopy
import requests
import mechanize

validfields = ["url", "text","password"]

validfields = ["url", "text","password"]


def sqltest(url):

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
        breakpoint()
        req = tempBr.form.click(type="submit")
        submitUrl = req.get_full_url()
        response = mechanize.urlopen(req)
        if response.geturl() != submitUrl:
            return True
        """response = tempBr.submit()
        if 300 <= response.getcode() < 400:
            return True"""
    """
    br.form
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    for form in soup.find_all('form'):

        print(form)
        submitUrl = form['action']
        submitMethod = form.get('method', 'GET')
        form.find_all('input')
        formData = {}
        for x in form.find_all('input'):
            if x.get('type', "text") in validfields and x.get('name'):
                formData[x['name']] = "' or 1=1 --"

        #if submitUrl.startswith('/') or not submitUrl.startswith("http"):
        #    submitUrl = url + submitUrl.lstrip('/')
        submitUrl = "/".join(url.split("/")[:3]) + "/" + submitUrl.lstrip('/')

        response = requests.request(submitMethod, submitUrl, data=formData, verify=False)
        breakpoint()
        print(response.status_code)
        if 300 <= response.status_code < 400:
            return True
            """
    return False


def xsstest(url):
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
           # breakpoint()
            req = tempBr.form.click(type="submit")
            submitUrl = req.get_full_url()
            response = mechanize.urlopen(req)
            if response.geturl() != submitUrl:
                return True
"""
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    form = soup.find('form')
    submitUrl = form['action']
    submitMethod = form.get('method', 'GET')
    form.find_all('input')
    with open("XSSstrings.txt") as fin:
        XSSstrings = fin.read().splitlines()

    for XSS in XSSstrings:

        formData = {}
        for x in form.find_all('input'):
            if x.get('type', "text") in validfields and x.get('name'):
                formData[x['name']] = XSS

        if submitUrl.startswith('/'):
            submitUrl = url.rstrip('/') + submitUrl

        response = requests.request(submitMethod, submitUrl, data=formData, verify=False)
        print(response.status_code)
        if XSS in response.text:

            return True
    return False
    """

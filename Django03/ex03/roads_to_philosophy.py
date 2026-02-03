import sys, requests
from bs4 import BeautifulSoup, NavigableString

def redirect(subject):
    url = "https://en.wikipedia.org/wiki/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0"
    }
    response = requests.get(url + subject, headers=headers)
    data = BeautifulSoup(response.content, 'html.parser')
    return data

def extract_brackets(paragraph):
    destruct = 0
    to_delete = []
    for tags in paragraph:
        if ("(" in tags.get_text()):
            destruct = 1
        if (destruct == 1):
            to_delete.append(tags)
        if (")" in tags.get_text()):
            break
    
    for d in to_delete:
        d.decompose()


def decompose(value, section):
    for remove in section.find_all(class_= value):
        remove.decompose()

def search_for_road(data):
    main_paragarph = data.find(id="mw-content-text")
    for remove in main_paragarph.find_all(role="note"):
        remove.decompose()
    for remove in main_paragarph.find_all(['table', 'style', 'semantics', 'math', 'figcaption', 'span']):
        remove.decompose()
    decompose("mw-empty-elt", main_paragarph)
    extract_brackets(main_paragarph.find(['p']))
    decompose("hatnote navigation-not-searchable", main_paragarph)
    decompose("mw-file-description", main_paragarph)
    decompose("thumbcaption", main_paragarph)
    decompose("oo-ui-buttonElement-button", main_paragarph)
    decompose("extiw", main_paragarph)
    for help in main_paragarph.find_all('a', href=lambda h: h and 'Help:' in h):
        help.decompose()
    for help in main_paragarph.find_all('a', href=lambda h: h and 'File:' in h):
        help.decompose()
    correction = main_paragarph.find(title="Wikipedia:Naming conventions (technical restrictions)")
    if (correction != None):
        correction.decompose()
    list = []
    for s in main_paragarph.find_all(['a', 'span']):
        if s.get('href') and '/wiki' in s.get('href'):
                list.append(s)
    ret = list[0].get('href').split("/")[2]
    if ret:
        return str(ret.strip("\n"))
    return None

def philosophy():
    try:
        args = sys.argv
        if len(args) != 2:
            raise Exception("One Argument is Required !")
        else:
            road = []
            subject = args[1]
            data_search = redirect(str(subject))
            is_available = data_search.find(string="Wikipedia does not have an article with this exact name.")
            if (is_available != None):
                raise Exception("It leads to a dead end !")
            topic = data_search.title.string.split('-')[0].strip()
            if (topic == "Philosophy"):
                print("Philosophy")
                print("0 roads from philosophy to philosophy !")
                return
            road.append(topic)
            search = search_for_road(data_search)
            number = 1
            while (search != None and search != "Philosophy"):
                if search in road:
                    raise Exception("It leads to an infinite loop !")
                road.append(search)
                data_search = redirect(search)
                search = search_for_road(data_search)
                number += 1
            number += 1
            road.append(search)
            for titles in road:
                print(titles)
            print(f"{number} roads from {topic} to philosophy !")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    philosophy()
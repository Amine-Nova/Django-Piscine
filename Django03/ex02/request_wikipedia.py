import requests
import dewiki
import json
import sys

def get_new_page(redirect):
    get_dict = redirect['parse']["wikitext"]['*']
    start = get_dict.find("[[")
    end = get_dict.find("]]")
    return get_dict[start + 2:end]

def get_data(input):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "parse",
        "page": input,
        "format": "json",
        "prop": "wikitext"
    }


    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.content
    data = json.loads(data)
    
    return data

def scrap_data(wiki_data, end_crt):
    # parse the {{....}}
    if (wiki_data != None):
        start = wiki_data.find("{")
        end = wiki_data.find(end_crt)
        if (start > end or start < 0 and end >= 0):
            wiki_data = wiki_data[:end - 1] + wiki_data[end + 2:]
        elif (start >= 0 and end >= 0):
            wiki_data = wiki_data[:start] + wiki_data[end + 2:]
            wiki_data = wiki_data.strip()
        elif (start >= 0 and end < 0):
            wiki_data = wiki_data[:start - 1] + wiki_data[start + 2:]
        else:
            pass
    return wiki_data
def scrap_data2(wiki_data):
    # parse the </ref>
    if (wiki_data != None):
        start = wiki_data.find("<")
        end = wiki_data.find(">")
        if (start > end):
            wiki_data = wiki_data[:end - 1] + wiki_data[end + 1:]
            wiki_data = wiki_data.strip()
        elif (start >= 0 and end >= 0):
            wiki_data = wiki_data[:start] + wiki_data[end + 1:]
            wiki_data = wiki_data.strip()
    return wiki_data

def wiki_search():
    try:
        args = sys.argv
        len_args = len(args)
        if (len_args != 2):
            raise Exception("The Number of Argument Are not Right!")
        data = get_data(args[1])
        if (data.get('parse') != None):
            if (data['parse']['wikitext']['*'].find("#REDIRECT") >= 0):
                data = get_data(get_new_page(data))
        elif (data['error']['code'].find("missingtitle") >= 0):
            raise Exception("Invalid Title")
        result = dewiki.from_string(data['parse']['wikitext']['*']).strip()
        result = scrap_data(result, "}\n\n")
        while (result != None and result.find("{") >= 0 or result != None and result.find("}") >= 0):
            result = scrap_data(result, "}")
        while (result != None and result.find("<") >= 0):
            result = scrap_data2(result)
        if (result != None and result.find("See also") >= 0):
            indice = result.find("See also")
            result = result[:indice]
    except Exception as e:
        print("Error:", e)
        return
    with open(args[1] + '.wiki', "w") as f:
        f.write(result.strip())

if __name__ == '__main__':
    wiki_search()


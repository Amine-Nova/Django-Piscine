import requests
import dewiki
import json

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

def scrap_data(wiki_data):
    pass

def wiki_search():
    # data = json.dumps(data)
    
    try:
        data = get_data("Micheal Jackson")
        if (json.dumps(data).find("#REDIRECT") >= 0):
            print(get_new_page(data))
            data = get_data(get_new_page(data))
        elif (json.dumps(data).find("missingtitle") >= 0):
            raise Exception("Invalid Title")
        result = dewiki.from_string(data)
    except Exception as e:
        print("Error:", e)

    print(result)
    result = scrap_data(data)
        

if __name__ == '__main__':
    wiki_search()


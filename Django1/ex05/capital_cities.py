import sys

def set_data(data):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    

def capital():
    if len(sys.argv) == 2:
        input = sys.argv[1].split(',')
        for i in input:
            set_data(i)



if __name__ == '__main__':
    capital()
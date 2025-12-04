import sys

def data():
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
    if len(sys.argv) == 2:
        input = sys.argv[1]
        if input in states:
            print(capital_cities[states[input]])
        else:
            print("Unknown state")


if __name__ == '__main__':
    data()
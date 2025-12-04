import sys

def state():
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
        value = None
        for k1, v1 in capital_cities.items():
            if v1 == input:
                value = k1
                break
        if value != None:
            for k2, v2 in states.items():
                if v2 == value:
                    print(k2)
                    break
        else:
            print("Unknown Capital")

    
if __name__ == '__main__':
    state()
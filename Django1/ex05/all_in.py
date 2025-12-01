import sys

def set_data(data):
    old = data
    data = data.title()
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
    get_state = None
    get_capital = None
    get_key = None
    if data in states:
        get_state = data
        get_key = states[data]
        get_capital = capital_cities[get_key]
        print(get_capital, "is the capital of", get_state)
        return
    elif data not in states and data != "":
        for k1, v1 in capital_cities.items():
            if data == v1:
                get_key = k1
                get_capital = v1
        for k2, v2 in states.items():
            if get_key == v2:
                get_state = k2
        if get_state == None or get_capital == None or get_key == None:
            print(old, "is neither a capital city nor a state")
            return
        else:
            print(get_capital, "is the capital of", get_state)
            return   
    
    

def capital():
    if len(sys.argv) == 2:
        input = sys.argv[1].split(',')
        for i in input:
            set_data(i.strip())



if __name__ == '__main__':
    capital()
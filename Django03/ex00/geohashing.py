import sys
from antigravity import geohash

def is_number(str):
    try:
        number = float(str)
        return True
    except ValueError:
        return False


def geohasing():
    try:
        args = sys.argv
        len_args = len(args)
        if (len_args != 4):
            if (len_args < 4):
                raise(Exception("Not Enough Arguments!"))
            else: 
                raise(Exception("Too Much Arguments!"))
        prec = args[3]
        print(prec)
        args.pop(0)
        args.pop(2)
        for arg in args:
            if (is_number(arg) == False):
                raise(Exception("Not a Number"))
        lat = float(args[0])
        long = float(args[1])
        geo = geohash(lat, long, "23-1-202649.09871")
        print(geo)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    geohasing()
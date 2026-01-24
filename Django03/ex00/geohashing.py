import sys
from antigravity import geohash
import pathlib

def is_number(str):
    try:
        number = float(str)
        return True
    except ValueError:
        return False


def geohasing():
    try:
        pathlib.Path("geohash.html").unlink(missing_ok=True)
        args = sys.argv
        len_args = len(args)
        if (len_args != 4):
            if (len_args < 4):
                raise(Exception("Not Enough Arguments!"))
            else: 
                raise(Exception("Too Much Arguments!"))
        prec = args[3]
        args.pop(0)
        args.pop(2)
        for arg in args:
            if (is_number(arg) == False):
                raise(Exception("Not a Number"))
        lat = float(args[0])
        long = float(args[1])
        if (lat < -90 or lat > 90):
            raise(Exception("Latitude out of range"))
        if (long < -180 or long > 180):
            raise(Exception("Longitude out of range"))
        geohash(lat, long, prec.encode())
        return
    except Exception as e:
        print(e)

if __name__ == '__main__':
    geohasing()
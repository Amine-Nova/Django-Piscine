def number_list():
    file = open("numbers.txt")
    data = file.read().split(',')

    for a in data:
        print(a)

if __name__ == '__main__':
    number_list()
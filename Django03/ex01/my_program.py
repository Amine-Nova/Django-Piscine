from local_lib.path import Path

def create():
    if (Path("folder").exists() == False):
        folder = Path("folder").mkdir()
    else:
        folder = Path("folder")
    path = folder / "file"
    path.write_text("Hello It's Amine Here")
    print((path).open('r').read())

if __name__ == '__main__':
    create()




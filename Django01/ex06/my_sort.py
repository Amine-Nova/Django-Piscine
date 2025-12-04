def sort():
    d = {
        "Hendrix": "1942",
        "Allman": "1946",
        "King": "1925",
        "Clapton": "1945",
        "Johnson": "1911",
        "Berry": "1926",
        "Vaughan": "1954",
        "Cooder": "1947",
        "Page": "1944",
        "Richards": "1943",
        "Hammett": "1962",
        "Garcia": "1942",
        "Beck": "1944",
        "Santana": "1947",
        "Ramone": "1948",
        "White": "1975",
        "Frusciante": "1970",
        "Thompson": "1949",
        "Burton": "1939",
    }
    year_sorted = sorted(d.items(), key=lambda a:a[1])
    alphabetic_sorted = sorted(d)

    print("----- Sorted By Year -----")
    for i in year_sorted:
        print(i[0])
    print("----- Sorted By Alphabetic Order -----")
    for i in alphabetic_sorted:
        print(i)


if __name__ == "__main__":
    sort()

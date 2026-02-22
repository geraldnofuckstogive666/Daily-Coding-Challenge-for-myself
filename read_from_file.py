#https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html


def main():
    names = {}

    with open('namelsts.txt', 'r') as open_file:
        for line in open_file:
            name = line.strip()
            names[name] = names.get(name, 0) + 1

    for name, count in names.items():
        print(f"{name}: {count}")



if __name__ == "__main__":
    main()
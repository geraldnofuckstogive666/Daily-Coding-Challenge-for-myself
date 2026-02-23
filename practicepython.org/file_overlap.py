#https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html


def get_num(filename):
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file if line.strip()]



def main():
    prime = get_num("prime_lists.txt")
    happy = get_num("happy_lists.txt")
    overlap = sorted(set(prime) & set(happy))
    print(*overlap)


if __name__ == "__main__":
    main()
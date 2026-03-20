#https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html


birthdays = {
    'Albert Einstein': '03/14/1879',
    'Isaac Newton': '01/04/1643',
    'Galileo Galilei': '02/15/1564',
    'Marie Curie': '11/07/1867',
    'Nikola Tesla': '07/10/1856',
    'Charles Darwin': '02/12/1809',
    'Stephen Hawking': '01/08/1942',
    'Ada Lovelace': '12/10/1815',
    'Alan Turing': '06/23/1912',
    'Johannes Kepler': '12/27/1571',
    'Michael Faraday': '09/22/1791',
    'James Clerk Maxwell': '06/13/1831',
    'Niels Bohr': '10/07/1885',
    'Dmitri Mendeleev': '02/08/1834',
    'Gregor Mendel': '07/20/1822',
    'Carl Sagan': '11/09/1934',
    'Richard Feynman': '05/11/1918',
    'Louis Pasteur': '12/27/1822',
    'Alexander Fleming': '08/06/1881',
    'Rosalind Franklin': '07/25/1920',
    'Tim Berners-Lee': '06/08/1955',
    'Katherine Johnson': '08/26/1918',
    'Jane Goodall': '04/03/1934'
}

def display_names(data):
    print(*data.keys(),sep="\n")


def get_birthday(data, name):
    return data.get(name)


def main():
    normalized_birthday = {name.lower(): date for name, date in birthdays.items()}
    print(f"Welcome to the birthday dictionary. We know the birthdays of:")
    display_names(birthdays)
    who = input("Whose birthday do you want to look up?\n").strip().lower()
    birthday = get_birthday(normalized_birthday, who)
    
    if birthday is None:
        print(f"{who.title()} is not on the birthday dictionary.")
        return
    
    print(f"{who.title()}'s birthday is {birthday}.")

if __name__ == "__main__":
    main()
#https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html


#part 1 - https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
#github - https://github.com/geraldnofuckstogive666/Daily-Coding-Challenge-for-myself/blob/main/practicepython.org/birthday_dictionaries.py
import sys
import json
from datetime import datetime


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

FILE_PATH = 'birthdays.json'


def display_names(data: dict[str, str]):
    print(*data.keys(),sep="\n")


def get_birthday(data, name):
    return data.get(name)


def is_datetime_format(date_string: str, format_code="%m/%d/%Y") -> bool:
  try:
    datetime.strptime(date_string, format_code)
    return True
  except ValueError:
    return False



def initialize_file(file_path, default_data):
    try:
        with open(file_path, 'x') as f:
            json.dump(default_data, f, indent=4)
    except FileExistsError:
        pass



def fetch_birthdays(file_path: str) -> dict[str, str]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def birthday_to_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent= 4)



def main():
    initialize_file(FILE_PATH, birthdays)  #this challenge

    data = fetch_birthdays(FILE_PATH)

    while True:
        try:
            add_count = int(input("How many do you want to add on the birthday dictionary? "))
            break
        except ValueError:
            continue

    while add_count > 0:
        name = input("Name: ").strip()
        
        if not name:
            print("Name cannot be empty.")
            continue
        
        birthday = input("Birthdate (MM/DD/YYYY): ")

        if is_datetime_format(birthday):
            data[name] = birthday
            add_count -= 1
        else:
            print("INVALID FORMAT. (MM/DD/YYYY)")
            
    
    birthday_to_json(FILE_PATH, data)



if __name__ == "__main__":
    main()
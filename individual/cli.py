'''
cli.py
Rui Shen 
April 16, 2025

NAME: cli.py - command-line interface exercise
SYNOPSIS: python3 cli.py characters by house
DESCRIPTION: Shows a list of the names of all the characters of a specified house from four houses 
including Gryffindor, Slytherin, Ravenclaw, and Hufflepuff.

'''
import argparse
import csv
def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Provides names of all the characters from a certain house in Harry Potter series')
    parser.add_argument('house', metavar='house', nargs=1, help='gives a list of characters from one of four houses in Harry Potter ')
    parser.add_argument('--other', '-o', action = 'store_true', help='list all characters but the ones from the specified house ')
    parser.add_argument("--shortenedList", "-s", action = 'store_true',help="print first ten characters in the list of characters from the specified house." )
    parsed_arguments = parser.parse_args()
    return parsed_arguments


def main():
    arguments = get_parsed_arguments()
    specified_house = arguments.house[0].lower()
    character_list = []
    with open('/Users/ruishen/Desktop/cs257_rui/cs257/data/Characters - Characters.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            house = row[4].strip().lower()
            name = row[1].strip()
            if arguments.other:
                if house != specified_house:
                    character_list.append(name)
            else:
                if house == specified_house:
                    character_list.append(name)
        if arguments.shortenedList:
            character_list = character_list[:10]
        for character in character_list:
            print(character)
            

if __name__ == '__main__':
    main()


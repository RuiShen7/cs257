'''
api.py
Rui Shen
April 11, 2025

'''
import sys
import argparse
import flask
import json
import csv

app = flask.Flask(__name__)

'''
REQUEST: /
RESPONSE:
    A greeting from this API to you.
'''
@app.route('/')
def hello():
    return 'Hello, Witches and Wizards.'

'''
REQUEST: /characters/{house}
RESPONSE:
    A list of characters who are from the house specified.
    Each actor is represented as a dictionary with keys "name".
    (the only value is gender now, but more can be added to depending on what we need later)
'''
@app.route('/characters/<house>')
def get_characters(house):
    ''' Returns the characters from the house specified and the gender of that character. '''
    characters_dictionary = {}
    lower_house = house.lower()
    with open( '/Users/ruishen/Desktop/cs257_rui/cs257/data/Characters.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            row_house = row[4].strip().lower()
            name = row[1].strip()
            gender = row[2].strip()
            if row_house == lower_house:
                characters_dictionary[name] = gender
    return json.dumps(characters_dictionary)


'''
REQUEST: /characters[?house={HOUSE}&amp;number={NUMBER}]
RESPONSE:
    A list of characters matching the specified GET parameters. 

      number, int: the number of characters the list will contain 
      house: reject any characters not from this house

    For example:

        /characters?number=10&amp;house=gryffindor

    will return a list of 10 Harry Potter characters from the house Gryffindor.

        /characters

    will return a list of all the characters.
'''
@app.route('/characters')
def get_movies():
    ''' Returns the list of characters that match GET parameters:
          number, int: the number of characters will be included in the output
          house: reject any characters not from this specified house
        If a GET parameter is absent, then the default house is none and the default number is 150, which means 
        all the characters would be presented since there are less than 150 characters in total.
    '''
    character_list = []
    house = flask.request.args.get('house', default='', type = str)
    number = flask.request.args.get('number', default=150, type=int)
    lower_house = house.lower()
    with open( '/Users/ruishen/Desktop/cs257_rui/cs257/data/Characters.csv') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            row_house = row[4].strip().lower()
            name = row[1].strip()
            if house and row_house!=lower_house:
                continue
            character_list.append(name)
            if len(character_list)>=number:
                break
    return json.dumps(character_list)

'''
REQUEST: /help
RESPONSE:
    direct to help.html and see the message
'''
@app.route('/help')
def get_help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)

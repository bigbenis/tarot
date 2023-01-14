from flask import Flask, render_template, url_for, g
from FDataBase import FDataBase
import random
import sqlite3
import os

# config
DATABASE = '/tmp/tarotcards.db'
DEBUG = True
SECRET_KEY = 'kjhH(*)&gh7F878Fi9hb^_'
USERNAME = 'admin'
PASSWORD = '1234'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "tarotcards.db")))

def connect_db():
    conn = sqlite3.connect((app.config['DATABASE']))
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


cards = ['Fool',
         'Magus',
         'Priestess',
         'Empress',
         'Emperor',
         'Hierophant',
         'Lovers',
         'Chariot',
         'Adjustment',
         'TheHermit',
         'Fortune',
         'Lust',
         'HangedMan',
         'Death',
         'Art',
         'Devil',
         'Tower',
         'Star',
         'Moon',
         'Sun',
         'Aeon',
         'Universe',
         'AceofDisks',
         'TwoofDisks',
         'ThreeofDisks',
         'FourofDisks',
         'FiveofDisks',
         'SixofDisks',
         'SevenofDisks',
         'EightofDisks',
         'NineofDisks',
         'TenofDisks',
         'KnightofDisks',
         'QueenofDisks',
         'PrinceofDisks',
         'PrincessofDisks',
         'AceofWands',
         'TwoofWands',
         'ThreeofWands',
         'FourofWands',
         'FiveofWands',
         'SixofWands',
         'SevenofWands',
         'EightofWands',
         'NineofWands',
         'TenofWands',
         'KnightofWands',
         'QueenofWands',
         'PrinceofWands',
         'PrincessofWands',
         'AceofCups',
         'TwoofCups',
         'ThreeofCups',
         'FourofCups',
         'FiveofCups',
         'SixofCups',
         'SevenofCups',
         'EightofCups',
         'NineofCups',
         'TenofCups',
         'KnightofCups',
         'QueenofCups',
         'PrinceofCups',
         'PrincessofCups',
         'AceofSwords',
         'TwoofSwords',
         'ThreeofSwords',
         'FourofSwords',
         'FiveofSwords',
         'SixofSwords',
         'SevenofSwords',
         'EightofSwords',
         'NineofSwords',
         'TenofSwords',
         'KnightofSwords',
         'QueenofSwords',
         'PrinceofSwords',
         'PrincessofSwords']

@app.route('/')
def index():
    return render_template('index.html', title="Thoth Tarot")


@app.route('/divination')
def threecards():
    divination = random.sample(cards, 3)

    return render_template('divination.html', title='Три карты', card1=divination[0], card2=divination[1],
                           card3=divination[2])


@app.route('/atu')
def atu():
    divination = random.sample(cards[0:21], 3)
    return render_template('atu.html', title='Старшие Арканы', card1=divination[0], card2=divination[1],
                           card3=divination[2])

@app.route('/lsd')
def lsd():
    divinaton = random.sample(cards, 3)
    return render_template('lsd.html', title='lsd',card1=divinaton[0], card2=divinaton[1], card3=divinaton[2])


@app.route('/test')
def test():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('test.html', cards=dbase.divination(), rand=random.randint(0, 77))


if __name__ == '__main__':
    app.run()
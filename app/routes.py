
from app import app
from flask import render_template, request
from .services import *
from random import randrange
from .forms import FindChar
#from .forms import "ClassForm"
import requests as r



@app.route('/')
def home():
    r_m = showChars()
    r_m.build_base()
    return render_template('index.html', r_m = r_m)

@app.route('/morty')
def morty():
    r_m = showChars()
    r_m.add_char(43)
    r_m.add_char(61)
    r_m.add_char(84)
    return render_template('morty.html', r_m = r_m)

@app.route('/rick')
def rick():
    r_m = showChars()
    r_m.add_char(1)
    r_m.add_char(15)
    r_m.add_char(760)
    r_m.add_char(22)
    return render_template('rick.html', r_m = r_m)

@app.route('/rando')
def rando():
    a = randrange(20, 800)
    b = randrange(20, 800)
    c = randrange(20, 800)
    d = randrange(20, 800)
    e = randrange(20, 800)
    r_m = showChars()
    r_m.add_char(a)
    r_m.add_char(b)
    r_m.add_char(c)
    r_m.add_char(d)
    r_m.add_char(e)
    return render_template('rando.html', r_m = r_m, a = a, b = b, c = c, d = d, e=e)

@app.route('/findchar', methods=['GET', 'POST'])
def findchar():
    form = FindChar()
    if request.method == 'POST':
        data = r.get(f'https://rickandmortyapi.com/api/character/{form.id.data}').json()
        c = Char(
            name =data['name'], status=data['status'],
            species=data['species'], gender=data['gender'],
            origin=data['origin'], image=data['image'], id=data['id']
        )

        return render_template('findchar.html', form=form, c=c)
    else:
        return render_template('findchar.html', form=form)

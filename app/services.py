import requests as r
from random import choice

class Char:
    def __init__(self, name, status, species, gender, origin, image, id):
        self.name = name
        self.status = status
        self.species = species
        self.gender = gender
        self.origin = origin
        self.episodes = []
        self.id = id
        self.image = image

class showChars:
    def __init__(self):
        self.chars = {}
    
    def add_char(self, id):
        response = r.get('https://rickandmortyapi.com/api/character/' + str(id) + "/")
        if response.status_code == 200:
            data = response.json()
        na = data['name']
        stat = data['status']
        spec = data['species']
        gen = data['gender']
        ori = data['origin']['name']
        img = data['image']
        n = Char(na, stat, spec, gen, ori, img, id)
        self.chars[data['id']] = n
        
    def build_base(self):
        self.add_char(1)
        self.add_char(2)
        self.add_char(3)
        self.add_char(4)
        self.add_char(5)
        self.add_char(6)
        self.add_char(7)
        self.add_char(8)
        self.add_char(9)
        self.add_char(10)
        self.add_char(11)

    def choose_rick(self):
        ricks = [1, 15, 19, 22, 48, 56, 69, 72, 74, 78, 82, 760, 86, 103, 119, 769, 770, 772, 773, 779]
        self.add_char(choice(ricks))
        
    def choose_morty(self):
        mortys = [2, 14, 21, 27, 42, 43, 44, 53, 61, 73, 77, 83, 759, 84, 85, 118]
        self.add_char(choice(mortys))
        

    def choose_summer(self):
        summers = [3, 629, 688]
        self.add_char(choice(summers))

    def choose_beth(self):
        beths = [4, 40, 628, 667, 691, 521]
        self.add_char(choice(beths))

    def choose_jerry(self):
        jerrys = [5, 689, 441, 442, 443, 444, 542]
        self.add_char(choice(jerrys))

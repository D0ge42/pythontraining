import sys
import requests
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QLayout
from PyQt5.QtGui import QPixmap, QIcon
from urllib.request import urlopen


pokemon_chosen = input("Search for a pokemon: ")
base_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_chosen}"

def link_to_img(url):
    url = get_pokemon_info_url()
    data = urlopen(url).read()
    pixmap = QPixMap()
    pixmap.loadFromData(data)
    icon = QIcon(pixmap)
    return icon

def get_pokemon_info_url():
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data["sprites"]["front_default"]

def get_pokemon_info_name():
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data["name"]

def get_pokemon_info_id():
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data["id"]
    
id = get_pokemon_info_id()
name = get_pokemon_info_name()


class Pokedex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.label = QLabel(f"#ID {id}",self)
        self.label1 = QLabel("#Name", self)
        self.label2 = QLabel()
        self.initUI()
        

    def initUI(self):

        self.label2.setPixMap(link_to_img())
        self.label.setGeometry(200,250,200,50)
        self.label1.setGeometry(200,300,200,50)
        self.label2.setGeometry(200,200,200,200)
        self.label.setStyleSheet("background-color: yellow;" "color: black;")
        self.label1.setStyleSheet("background-color: yellow;" "color: black;")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    poke = Pokedex()
    poke.show()
    sys.exit(app.exec_())


import sys
import requests
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QLayout, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from urllib.request import urlopen


pokemon_chosen = input("Search for a pokemon: ")
base_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_chosen}"

#Convert pokemon chosen to png
def pokemon_to_png():
    pokemon_chosen_to_png = f"pokemon/Pokemon Dataset/{pokemon_chosen}.png"
    return pokemon_chosen_to_png

#Return pokemon name
def get_pokemon_info_name():
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data["name"]
#Return pokemon id
def get_pokemon_info_id():
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data["id"]
    
id = get_pokemon_info_id()
name = get_pokemon_info_name()
pokemon_chosen_pix = pokemon_to_png()
print (pokemon_chosen_pix)

class Pokedex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,300,300)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Search", self)
        # self.label = QLabel(f"#ID {id}",self)
        # self.label1 = QLabel(f"#Name {name}", self)
        # self.label2 = QLabel(self)
        self.initUI()
        

    def initUI(self):

        self.line_edit.setPlaceholderText("Search...")
        self.line_edit.setGeometry(150, 150, 200, 40)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # pixmap = QPixmap(pokemon_chosen_pix)
        # self.label2.setPixmap(pixmap)
        # self.label.setGeometry(200,200,50,50)
        # self.label1.setGeometry(200,250,50,50)
        # self.label2.setGeometry(200,100,400,400)
        # self.label.setStyleSheet("background-color: yellow;" "color: black;")
        # self.label1.setStyleSheet("background-color: orange;" "color: black;")
        # self.label2.setScaledContents(True) 


        #vbox = QVBoxLayout()

        # vbox.addWidget(self.label2)
        # vbox.addWidget(self.label1)
        # vbox.addWidget(self.label)
        # vbox.addWidget(self.line_edit)
        # vbox.addWidget(self.button)

        #central_widget.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    poke = Pokedex()
    poke.show()
    sys.exit(app.exec_())


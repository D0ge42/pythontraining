import sys
import requests
from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame, QWidget, QApplication,QHBoxLayout, QMainWindow, QLabel, QLayout, QVBoxLayout, QLineEdit, QPushButton, QSizePolicy,QGroupBox, QGridLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from urllib.request import urlopen

pokemon_types_dic = {"normal": "#bab095","fire": "#fa6a02","water": "#0272fa",
                      "electric": "#fae102","grass": "#5df067" ,"ice": "#95fce8",
                      "fighting":"#eb092f","poison":"#a009eb","ground": "#e3ed6f",
                      "flying":"#a06fed","psychic": "#f760ac","bug":"#87ad4c",
                      "rock": "#ad974c","ghost": "#3a205e","dragon": "#481d8c",
                      "dark": "#8c461d","steel": "#a89fb3","fairy": "#f2affa"}


#Pokemon types count
def pokemon_types_count(base_url):
    types = get_pokemon_info_type(base_url)
    types_count = len(types)
    return types_count 

#Define first color type
def pokemon_color_type1(base_url):
    type = get_pokemon_info_type(base_url)
    color = pokemon_types_dic.get(type[0])
    return color

#Define second color type if pokemon has more than 1 type
def pokemon_color_type2(base_url):
    type = get_pokemon_info_type(base_url)
    color = pokemon_types_dic.get(type[1])
    return color

#Convert pokemon chosen to png
def pokemon_to_png(pokemon_chosen):
    pokemon_chosen_to_png = f"pokemon/Pokemon Dataset/{pokemon_chosen}.png"
    return pokemon_chosen_to_png

#Return pokemon name
def get_pokemon_info_name(base_url):
    response = requests.get(base_url)
    print(response.status_code)
    if response.status_code == 200:
        pokemon_data = response.json()
    return pokemon_data["name"]

#Return pokemon id
def get_pokemon_info_id(base_url):
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
    return pokemon_data["id"]

#Return pokemon height
def get_pokemon_info_height(base_url):
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
    return pokemon_data["height"]

#Return pokemon weight
def get_pokemon_info_weight(base_url):
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
    return pokemon_data["weight"]

#Return pokemon types
def get_pokemon_info_type(base_url):
    response = requests.get(base_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        type_names = [type_info['type']['name'] for type_info in pokemon_data['types']]
    return type_names

#Convert height to meters.
def height_converter(height):
    height = int(height)
    return height / 10

#Convert weight to kgs.
def weight_converter(weight):
    weight = int(weight)
    return weight / 10


class Pokedex(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1920,1080)


        #Initialize widgets
        self.line_edit = QLineEdit(self)
        self.button = QPushButton(self)
        self.pk_image = QLabel(self)
        self.pk_name = QLabel(self)
        self.pk_type = QLabel(self)
        self.pk_type2 = QLabel(self)
        self.info_box = QFrame(self)
        self.pk_height = QLabel(self)
        self.pk_weight = QLabel(self)

        #Set various text
        self.line_edit.setPlaceholderText("Search for a pokemon...")
        self.button.setText("Search")

        #Set widgets geometry
        self.line_edit.setGeometry((1920) // 2 - 200, 700, 400, 50 )
        self.button.setGeometry((1920) // 2 - 100, 770, 200, 50 )
        self.pk_name.setGeometry((1920) // 2 - 80, 200, 200, 50 )
        self.pk_image.setGeometry((1920) // 2 - 400, 300, 400, 400)
        self.info_box.setGeometry((1920) // 2 + 30, 450, 300, 200)
        self.pk_type.setGeometry((1920) // 2 + 20, 400, 150, 40)
        self.pk_type2.setGeometry((1920) // 2 + 190, 400, 150, 40)
        self.pk_height.setGeometry((1920) // 2 + 40, 460, 100, 20 )
        self.pk_weight.setGeometry((1920) // 2 + 200, 460, 150, 20 )

        #Set button connection
        self.button.clicked.connect(self.submit)


    def submit(self):
        #Base data
        pk_name_text = self.line_edit.text()
        base_url = f"https://pokeapi.co/api/v2/pokemon/{pk_name_text}"

        #Pokemon types handling
        if pokemon_types_count(base_url) == 1:
            
            self.pk_type2.setDisabled(True)
            self.pk_type.setGeometry((1920 // 2 + 40), 400, 280, 40)
            self.pk_type2.setGeometry((1920 // 2 + 20), 400, 0, 0)

            color = pokemon_color_type1(base_url) 
            pokemon_type = get_pokemon_info_type(base_url)
            self.pk_type.setText(f"<b>{pokemon_type[0]}<b>")
            self.pk_type.setStyleSheet(f"background-color: {color};"
                                   "font-size: 20px;" "border-radius: 2px;")
        elif pokemon_types_count(base_url) == 2:
            self.pk_type2.setDisabled(False)
            pokemon_type = get_pokemon_info_type(base_url)
            self.pk_type.setText(f"<b>{pokemon_type[0]}<b>")
            self.pk_type2.setText(f"<b>{pokemon_type[1]}<b>")

            self.pk_type.setGeometry((1920 // 2 + 20), 400, 150, 40)
            self.pk_type2.setGeometry((1920 // 2 + 190), 400, 150, 40)

            color = pokemon_color_type1(base_url)
            color2 = pokemon_color_type2(base_url)
            self.pk_type.setStyleSheet(f"background-color: {color};"
                                   "font-size: 20px;" "border-radius: 2px;")
            self.pk_type2.setStyleSheet(f"background-color: {color2};"
                                   "font-size: 20px;" "border-radius: 2px;")

        #Colors
        pokemon_color_type1(base_url)
        
        #Text name of the pokemon
        name = get_pokemon_info_name(base_url)
        self.pk_name.setText(f"<b>{name.capitalize()}<b>")
        self.pk_name.setStyleSheet("font-size: 40px")

        #Img to generate
        pokemon_img = pokemon_to_png(pk_name_text)
        pixmap = QPixmap(pokemon_img)
        scaled_pixmap = pixmap.scaled(self.pk_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.pk_image.setPixmap(scaled_pixmap)

        #Pokemon type
        pokemon_type = get_pokemon_info_type(base_url)
        pokemon_type_str = ', '.join(pokemon_type)
        self.pk_type.setAlignment(QtCore.Qt.AlignCenter)
        self.pk_type2.setAlignment(QtCore.Qt.AlignCenter)
       

        #Pokemon info box
        self.info_box.setFrameShape(QFrame.Box)
        self.info_box.setLineWidth(2)
        self.info_box.setStyleSheet("background-color: cyan;" "border-radius: 5px;")

        #Pokemon Height
        pokemon_height = get_pokemon_info_height(base_url)
        self.pk_height.setText(f"<b> Height: <b> {height_converter(pokemon_height)}m")

        #Pokemon Weight
        pokemon_weight = get_pokemon_info_weight(base_url)
        self.pk_weight.setText(f"<b> Weight: <b> {weight_converter(pokemon_weight)}kg")

#Stylesheet of main window
stylesheet =  """Pokedex {
    background-image: url("pokemon/Pokemon Dataset/pngegg(1).png"); 
    background-repeat: no-repeat; 
    background-position: center; 
    }
    """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    poke = Pokedex()
    poke.show()
    sys.exit(app.exec_())


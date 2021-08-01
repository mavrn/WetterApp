from PyQt5 import QtWidgets
from web_scraping_modules import get_content_from_url
from wetter_ui import Ui_Form
import sys

city_dict = {"Böblingen": "https://www.wetter.com/deutschland/boeblingen/DE0000510.html",
             "Ludwigsburg": "https://www.wetter.com/deutschland/ludwigsburg/DE0006439.html",
             "Stuttgart": "https://www.wetter.com/deutschland/stuttgart/DE0010287.html",
             "Hamburg": "https://www.wetter.com/deutschland/hamburg/DE0004130.html",
             "Berlin": "https://www.wetter.com/deutschland/berlin/DE0001020.html",
             "Köln": "https://www.wetter.com/deutschland/koeln/DE0005156.html",
             "Amsterdam": "https://www.wetter.com/niederlande/amsterdam/NL0NH0013.html",
             "New York": "https://www.wetter.com/usa/new-york-city/US0NY0993.html",
             "Los Angeles": "https://www.wetter.com/usa/los-angeles/US5368361.html",
             "Paris": "https://www.wetter.com/frankreich/paris/FR0IF0356.html",
             "London": "https://www.wetter.com/vereinigtes-koenigreich/london/GB0KI0101.html",
             "Tokyo": "https://www.wetter.com/japan/tokio/JP0TY0011.html",
             "Madrid": "https://www.wetter.com/spanien/madrid/ES0MA0079.html"}


def get_url():
    while True:
        city = input("Geben Sie eine Stadt ein: ").lower().capitalize()
        if city in city_dict:
            return city_dict.get(city)
        elif city == "Hilfe":
            for city in city_dict.keys():
                print("-" + city)
        else:
            print("Diese Stadt existiert noch nicht. Geben Sie \"Hilfe\" für eine Liste von unterstützten Städten ein.")


def strip_of_decimal(value):
    if "," in value:
        return value[:value.index(",")] + "°C"
    else:
        return value


content = get_content_from_url(get_url())
temp = strip_of_decimal(content.find("div", "text--white beta palm-inline-block").text)
temp_value = float(temp.strip("°C").replace(",", "."))
weather_desc = content.find("td", "text--center delta portable-pb desk-pb+ tdbl").text.strip()
graph_desc = content.find("div", "printable").find("p").text.strip()

app = QtWidgets.QApplication(sys.argv)
Widget = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Widget, temp_value)
ui.setText(temp, graph_desc, weather_desc)
Widget.show()
sys.exit(app.exec_())

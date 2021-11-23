import webbrowser
from Pasajero import *
from Usuario import *
import googlemaps
import requests
from pprint import pprint

api_file=open("Interfaz/API/aappii.txt", "r")
api_key=api_file.read()
api_file.close()
map_client=googlemaps.Client(api_key)

pasa=Pasajero()
us=Usuario()

class Ruta():
    #constructor
    def __init__(self):
        self.puntoInicial=""
        self.puntoFinal=""
        self.puntoParada=""
        self.latInicial=0
        self.latParada=0
        self.latFinal=0
        self.lonInicial=0
        self.lonParada=0
        self.lonFinal=0

    #setter del punto inicial del conductor
    def setPuntoInicial(self,puntoInicial):
        puntoInicial = puntoInicial
        response = map_client.geocode(puntoInicial)
        self.latInicial = response[0]["geometry"]["location"]["lat"]
        self.lonInicial = response[0]["geometry"]["location"]["lng"]
        self.puntoInicial=str(self.latInicial)+"%2C"+str(self.lonInicial)

    # agrega una parada a la ruta del conductor para que pueda recoger a las personas
    def setParada(self, parada):
        response = map_client.geocode(parada)
        self.latParada = response[0]["geometry"]["location"]["lat"]
        self.lonParada = response[0]["geometry"]["location"]["lng"]
        self.puntoParada=str(self.latParada)+"%2C"+str(self.lonParada)


    #getter punto inicial
    def getPuntoInicial(self):
        return self.puntoInicial
    def getParada(self):
        return self.puntoParada
    #getter punto final
    def getPuntoFinal(self):
        return self.puntoFinal

    #metodo para crear la ruta que va a tener el conductor hacia el trabajo
    def crearRutaFinal(self,puntoInicial):
        puntoInicial=puntoInicial
        response = map_client.geocode(puntoInicial)
        latInicial=response[0]["geometry"]["location"]["lat"]
        lonInicial=response[0]["geometry"]["location"]["lng"]
        webbrowser.open("https://www.waze.com/ul?ll=6.1997094%2C-75.5792681&navigate=no&zoom=17&from="+str(latInicial)+"%2C"+str(lonInicial))
        print("ya voy a abrir la ruta final",)
    #def crearRutaParada(self,latInicial,lonInial):
    def crearRutaParada(self):
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
        r = requests.get(url + "origins=" + self.getPuntoInicial()+ "&destinations="+self.getParada()+"&key=" + api_key)
        time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
        seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
        print("\n el viaje total del viaje es ", time)
        return str(time)
    def dibujarRutaParada(self):
        webbrowser.open("https://www.waze.com/ul?ll="+self.getParada()+"&navigate=no&zoom=17&from="+self.getPuntoInicial() )
import smtplib

from kivy.properties import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import Screen
from Vehiculo import Vehiculo
from kivy.core.window import Window
from Usuario import Usuario
from kivy.uix.button import Button
from Conductor import Conductor
from Pasajero import *
from Ruta import *
import mysql.connector
import webbrowser
mysqlcnx = mysql.connector.connect(user='root', password='Daviddegea22.',
                              host='127.0.0.1',
                              database='pricar',
                              autocommit=True)
mysqlcursor=mysqlcnx.cursor()
"""mysqlcursor.execute("select * from empleados;")
mysqlresultado = mysqlcursor.fetchall()"""

# import request
api_file = open("Interfaz/API/aappii.txt", "r")
api_key = api_file.read()

#Window.size = (260, 500)
Window.size=(400,850)
v = Vehiculo()

#clase invocada
us=Usuario()
pas=Pasajero()
rut=Ruta()
con=Conductor()



#WINDOWMANAGER
class WindowManager(ScreenManager):
    pass



#WIDGETS, POPUPS
"""popup para avisar que hubo un error en el login"""
class ErrorLogin(FloatLayout):
    pass
"""popup para editar perfil"""
class EditPerfil(FloatLayout):
    def moveTo(self):
        kiv.current = "editP"

    #aun no funciona este metodo
    def close(self):
        EditPerfil.exit()



#SCREEN, MAIN
"""Pantalla predeterminada"""
class Default(Screen):
    pass

"""Clase de la pantalla de login"""
class LogInScreen(Screen):
    user=ObjectProperty(None)
    password=ObjectProperty(None)
    def login(self):
        cuentaExistente=False
        mysqlcursor.execute("select * from empleados;")
        mysqlresultado = mysqlcursor.fetchall()
        for user in mysqlresultado:
            if self.user.text == user[2]:
                self.codigo=user[0]
                mysqlcursor.execute("select * from empleados where empleados.CodigoTrabajador="+self.codigo+";")
                mysqlresultado = mysqlcursor.fetchall()
                for password in mysqlresultado:
                    if self.password.text==password[0]:
                        us.setCode(password[0])
                        us.setName(password[1])
                        us.setMail(password[2])
                        us.setCellphone(password[3])
                        us.setAddres(password[5])
                        us.setPlaca(password[6])
                        us.setCarcap(password[7])
                        us.setPoints(password[9])
                        cuentaExistente=True
                        na=self.manager.get_screen("perfil")
                        na.ids.nameP.text=us.getName()
                        na.ids.mail.text=us.getMail()
                        na.ids.address.text=us.getAddress()
                        na.ids.cellphone.text=us.getCellphone()
                        na.ids.placa.text=us.getPlaca()
                        na.ids.carcap.text=str(us.getCarcap())
                        na.ids.point.text=str(us.getPoints())


        #falta ver como se conecta con la base de datos y que revise todo eso
        if cuentaExistente==False:
            print("Datos incorrectos")
            self.show_popup("Datos incorrectos")
            #falta poner el popup que diga que "llene los campos
        elif cuentaExistente==True:
            kiv.current = "menu"
            print("hola ",self.user.text)


    def show_popup(self, title):
        show = ErrorLogin()
        self.popupWindow = Popup(title=title,title_size=25, content=show,
                                 size_hint=(None, None), size=(350, 300))
        self.popupWindow.open()
"""Clase de la pantalla del menu"""
class MenuScreen(Screen):
    def updateData(self):
        #mysqlcursor.execute("select * from empleados where empleados.CodigoTrabajador=" + us.getCode()+ ";")
        na = self.manager.get_screen("perfil")
        na.ids.nameP.text = us.getName()
        na.ids.mail.text = us.getMail()
        na.ids.address.text = us.getAddress()
        na.ids.cellphone.text = us.getCellphone()
        na.ids.placa.text = us.getPlaca()
        na.ids.carcap.text = str(us.getCarcap())
        na.ids.point.text = str(us.getPoints())
    def checkStatusP(self):
        mysqlcursor.execute("select ViajeEncontradoP,BuscandoViajePasajero from empleados where empleados.CodigoTrabajador="+us.getCode()+";")
        mysqlresultado = mysqlcursor.fetchall()
        self.hayViaje=0
        self.hayBusqueda=0
        for x in mysqlresultado:
            self.hayViaje=x[0]
            self.hayBusqueda=x[1]
        if self.hayViaje==0 and self.hayBusqueda==0:
            kiv.current = "ridernoride"
        elif self.hayViaje==0 and self.hayBusqueda==1:
            kiv.current = "waitingfordriver"
        elif self.hayViaje==1 and self.hayBusqueda==0:
            kiv.current = "riderpicked"
        else:
            kiv.current="endtriprider"
    def checkStatusC(self):
        mysqlcursor.execute("select ViajeEncontradoC,BuscandoViajeConductor from empleados where empleados.CodigoTrabajador=" + us.getCode() + ";")
        mysqlresultado = mysqlcursor.fetchall()
        self.hayViaje = 0
        self.hayBusqueda = 0
        for x in mysqlresultado:
            self.hayViaje = x[0]
            self.hayBusqueda = x[1]
        if self.hayViaje == 0 and self.hayBusqueda == 0:
            kiv.current = "riderlocation"
        elif self.hayViaje == 0 and self.hayBusqueda == 1:
            kiv.current = "driverselection"
        elif self.hayViaje == 1 and self.hayBusqueda == 0:
            kiv.current = "drivercontact"
        else:
            kiv.current = "drivermoret"

"""Clase de la pantalla de perfil"""
class ProfileScreen(Screen):
    pass
"""Clase de la pantalla de editar perfil"""
class EditProfileScreen(Screen):
    nameP=ObjectProperty(None)
    email=ObjectProperty(None)
    cel=ObjectProperty(None)
    placa=ObjectProperty(None)
    direc=ObjectProperty(None)
    capve=ObjectProperty(None)
    def save(self):
        #que reciba los datos que ingresó el usuario, si no ingresó nada no se cambia nada
        if self.nameP.text!="":
            us.editName(self.nameP.text)
        if self.email.text!="":
            us.editMail(self.email.text)
        if self.direc.text!="":
            us.editAddress(self.direc.text)
        if self.cel.text!="":
            us.editCellphone(self.cel.text)
        if self.placa.text!="":
            us.editPlaca(self.placa.text)
        if self.capve.text!="":
            us.editCarcap(self.capve.text)
        print("se ha guardado correctamente")


"""en el menu, que revise que es, si esta buscnado viaje, si esta esperando conductor y cosas asi"""
"""clase para pasasjero sin viaje ni busqueda"""
class RiderWNRScreen(Screen):
    def paradaP(self):
        pas.seleccionarParadaPred(us.getCode(),us.getAddress())
    def paradaA(self):
        pas.seleccionarParadaAc(us.getCode())
"""clase para pasajero esperando al conductor, sin viaje con busqueda"""
class RiderWaitScreen(Screen):
    def cancelRide(self):
        mysqlcursor.execute("update empleados set BuscandoViajePasajero=False where empleados.CodigoTrabajador="+us.getCode()+";")
        print("viaje cancelado")
"""clase para pasajero buscando viaje"""
class RiderPScreen(Screen):
    comments = ObjectProperty(None)
    def sendComment(self):
        if self.comments.text!="":
            mysqlcursor.execute("select Correo from empleados where empleados.ViajeEncontradoC=True;")
            mysqlresultado = mysqlcursor.fetchall()
            self.cor=""
            for i in mysqlresultado:
                self.cor = i[0]
            sender=us.getMail()
            recipient=self.cor
            subject="Pricar"
            print(self.comments.text)
            message=self.comments.text
            email="subject:{}\n\n".format(subject,message)
            password_file=open("Interfaz/API/correo.txt","r")
            password=password_file.readline()
            password_file.close()
            s=smtplib.SMTP("smtp-mail.outlook.com",587)
            s.starttls()
            s.login(sender,password)
            s.sendmail(sender,recipient,email)
            print("se envio bien a ",recipient)
        else:
            print("no hay mensaje que enviar")
    def cancelRide(self):
        mysqlcursor.execute("update empleados set BuscandoViajePasajero=False where empleados.CodigoTrabajador="+us.getCode()+";")
        mysqlcursor.execute("update empleados set ViajeEncontradoP=False where empleados.CodigoTrabajador=" + us.getCode() + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoC=False where empleados.ViajeEncontradoC= True;")
        print("viaje cancelado")
"""clase para pasajero fin de viaje"""
class RiderEndRScreen(Screen):
    nameD = ObjectProperty(None)
    def endTrip(self, cali):
        mysqlcursor.execute("select PuntosDeBeneficio from empleados where empleados.Nombre='Fernando Alonso';")
        mysqlresultado = mysqlcursor.fetchall()
        self.puntoActuales=0
        for i in mysqlresultado:
            self.puntoActuales=i[0]
        puntosNuevos=self.puntoActuales+cali
        mysqlcursor.execute("update empleados set PuntosDeBeneficio=%i"%puntosNuevos+" where empleados.Nombre='Fernando Alonso';")
        mysqlcursor.execute("update empleados set BuscandoViajePasajero=False where empleados.CodigoTrabajador=" + us.getCode() + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoP=False where empleados.CodigoTrabajador=" + us.getCode() + ";")


"""Clase de la pantalla del conductor"""
class DriverLocationScreen(Screen):
    def paradaP(self):
        con.seleccionarParadaPred(us.getCode(),us.getAddress())
    def paradaA(self):
        pas.seleccionarParadaAc(us.getCode())
    def abrirRuta(self):
        rut.crearRutaFinal(us.getAddress())
"""Clase para conductor sin pasasjero"""
class DriverSelectionScreen(Screen):
    def quitarPasajero(self):
        mysqlcursor.execute(
            "select Nombre from empleados where empleados.BuscandoViajePasajero=True;")
        mysqlresultado = mysqlcursor.fetchall()
        for info in mysqlresultado:
            button = Button(text=info[0])
            self.ids.opciones.remove_widget(button)
    def agregarPasajero(self):
        mysqlcursor.execute(
            "select Nombre from empleados where empleados.BuscandoViajePasajero=True;")
        self.mysqlresultado = mysqlcursor.fetchall()
        tmp=0
        for info in self.mysqlresultado:
            a=str(tmp)
            button=Button(text=info[0],on_press=lambda button: self.getRiderInfo(info[0]))
            self.ids[str(tmp)]=button
            self.ids["opciones"].add_widget(button)
            if tmp<len(self.mysqlresultado)-1:
                tmp+=1

    def getRiderInfo(self,obj):

        rp = self.manager.get_screen("driverriderprofilescreen")
        mysqlcursor.execute(
            "select Nombre,Direccion from empleados where empleados.Nombre='"+obj+"';")
        mysqlresultado = mysqlcursor.fetchall()
        for info in mysqlresultado:
            rp.ids.nameP.text = info[0]
            rp.ids.direc.text=info[1]
        rut.setParada(rp.ids.direc.text)
        rut.setPuntoInicial(us.getAddress())
        rp.ids.tDis.text=rut.crearRutaParada()

        kiv.current="driverriderprofilescreen"
    def cancelSearch(self):
        mysqlcursor.execute("update empleados set BuscandoViajeConductor=False where empleados.CodigoTrabajador="+us.getCode()+";")
        print("busqueda cancelada")
"""clase para conductor para ver el perfil del pasajero"""
class DriverSeeRiderProfileScreen(Screen):
    nameP=ObjectProperty(None)
    direc=ObjectProperty(None)
    tDis=ObjectProperty(None)

    def accept(self):
        na = self.manager.get_screen("endtriprider")
        na.ids.nameD.text = us.getName()
        rp = self.manager.get_screen("driverriderprofilescreen")
        mysqlcursor.execute(
            "update empleados set BuscandoViajePasajero=False where empleados.Nombre='" + rp.ids.nameP.text + "';")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoP=True where empleados.Nombre='" + rp.ids.nameP.text + "';")
        mysqlcursor.execute(
            "update empleados set BuscandoViajeConductor=False where empleados.Nombre='" + us.getName() + "';")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoC=True where empleados.Nombre='" + us.getName() + "';")
        rut.dibujarRutaParada()
"""clase para conductor para contactar al pasajero ó finalizar el viaje"""
class DriverContactRiderScreen(Screen):
    def picked(self):
        rp = self.manager.get_screen("driverriderprofilescreen")
        mysqlcursor.execute(
            "update empleados set BuscandoViajeConductor=True where empleados.Nombre='" + us.getName() + "';")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoC=True where empleados.Nombre='" + us.getName() + "';")

    def cancelRide(self):
        #falta cancelarle el viaje al conductor
        mysqlcursor.execute("update empleados set BuscandoViajePasajero=False where empleados.CodigoTrabajador="+us.getCode()+";")
        mysqlcursor.execute("update empleados set ViajeEncontradoP=False where empleados.CodigoTrabajador=" + us.getCode() + ";")
        mysqlcursor.execute("update empleados set ViajeEncontradoC=False where empleados.ViajeEncontradoC= True;")
        print("viaje cancelado")

    pass
class DriverMoreTripsScreen(Screen):
    def noMore(self):
        rut.crearRutaFinal(us.getAddress())
        rp = self.manager.get_screen("driverriderprofilescreen")
        mysqlcursor.execute(
            "update empleados set BuscandoViajePasajero=True where empleados.Nombre='" + rp.ids.nameP.text + "';")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoP=True where empleados.Nombre='" + rp.ids.nameP.text + "';")
        mysqlcursor.execute(
            "update empleados set BuscandoViajeConductor=True where empleados.Nombre='" + us.getName() + "';")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoC=True where empleados.Nombre='" + us.getName() + "';")
        pass
    def more(self):
        rp = self.manager.get_screen("driverriderprofilescreen")
        mysqlcursor.execute(
            "update empleados set BuscandoViajePasajero=True where empleados.Nombre='" + rp.ids.nameP.text + "';")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoP=True where empleados.Nombre='" + rp.ids.nameP.text + "';")
        mysqlcursor.execute(
            "update empleados set BuscandoViajeConductor=True where empleados.Nombre='" + us.getName() + "';")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoC=False where empleados.Nombre='" + us.getName() + "';")

class DriverEndScreen(Screen):
    def finish(self):


        mysqlcursor.execute(
            "update empleados set BuscandoViajeConductor=False where empleados.Nombre='" + us.getName() + "';")
        mysqlcursor.execute(
            "update empleados set ViajeEncontradoC=False where empleados.Nombre='" + us.getName() + "';")




kiv = Builder.load_file(("Interfaz/main.kv"))
"""MAIN"""
class Pricar(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return kiv
    def show_popup(self,title):
        show = EditPerfil()
        self.popupWindow = Popup(title=title,title_size=25, content=show,
                                 size_hint=(None, None), size=(350,250))
        self.popupWindow.open()
if __name__ == "__main__":
    Pricar().run()
mysqlcnx.close()


from kivymd.app import MDApp
from kivy_garden.mapview import MapView

class MapViewApp(MDApp):
	def build(self):
		mapview = MapView(zoom=9, lat=6, lon=-76)
		return mapview

MapViewApp().run()

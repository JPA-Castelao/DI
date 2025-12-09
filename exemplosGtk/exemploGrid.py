import gi
import CaixaCor

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject


class ExemploBoxColor(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo de uso de Grid layout")

        vermello = CaixaCor.CaixaCor("red")
        azul = CaixaCor.CaixaCor("blue")
        verde = CaixaCor.CaixaCor("green")
        laranxa = CaixaCor.CaixaCor("orange")
        pink = CaixaCor.CaixaCor("rosa")
        marron = CaixaCor.CaixaCor("brown")
        lila = CaixaCor.CaixaCor("purple")

        maia = Gtk.Grid()

        self.add()
        self.connect("delete-event", Gtk.main_quiet)
        self.show_all()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # noqa # That just how GTK for py works apparently

from TagScriptEngine import Interpreter, adapter, block

blocks = [
    block.MathBlock(),
    block.RandomBlock(),
    block.RangeBlock(),
    block.AnyBlock(),
    block.IfBlock(),
    block.AllBlock(),
    block.BreakBlock(),
    block.StrfBlock(),
    block.StopBlock(),
    block.AssignmentBlock(),
    block.FiftyFiftyBlock(),
    block.ShortCutRedirectBlock("message"),
    block.LooseVariableGetterBlock(),
    block.SubstringBlock(),
    block.EmbedBlock()
]
x = Interpreter(blocks)


class Playground(Gtk.Window):
    def __init__(self):
        super().__init__(title="TSE Playground")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.input = Gtk.Entry()
        self.input.set_placeholder_text("Input goes here!")
        self.input.set_text('{embed({"title": "Hello World!"})}')
        vbox.pack_start(self.input, True, True, 0)

        self.output = Gtk.Entry()
        self.output.set_editable(False)
        vbox.pack_start(self.output, True, True, 0)

        self.process_button = Gtk.Button(label="Process")
        self.process_button.connect("clicked", self.do_process)
        vbox.pack_start(self.process_button, True, True, 0)

    def do_process(self, widget):
        o = x.process(self.input.get_text()).body
        self.output.set_text(o)


win = Playground()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

logo_pixbuf = GdkPixbuf.Pixbuf.new_from_file("/usr/share/pixmaps/bluewave-logo.png")
logo_pixbuf = logo_pixbuf.scale_simple(100, 100, GdkPixbuf.InterpType.BILINEAR)
logo_image = Gtk.Image.new_from_pixbuf(logo_pixbuf)
logo_image.set_margin_top(8) 
logo_image.set_valign(Gtk.Align.START)

subprocess.Popen(["/bin/xdg-user-dirs-update", "--force"])

def on_button1_clicked(widget):
    print("Button 1 clicked.")
    subprocess.Popen(["/bin/lxterminal", "-e", "doas", "pacman", "-Syu" ])

def on_button2_clicked(widget):
    print("Button 2 clicked.")
    subprocess.Popen(("/bin/lxterminal", "-e", "doas", "pacman", "-Scc"))

def on_button3_clicked(widget):
    print("Button 3 clicked.")
    subprocess.Popen(("/bin/mousepad", "/etc/.ohlookasecret/MANUAL.txt"))

def on_button4_clicked(widget):
    print("Button 4 clicked.")
    subprocess.Popen(("/bin/timeshift-launcher"))

def on_button5_clicked(widget):
    print("Button 5 clicked.")
    subprocess.Popen(("/bin/lxterminal", "-e", "rm", "-rf", "/$HOME/.config/autostart/blwv.desktop", "&&"))
    Gtk.main_quit()

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.set_default_size(500, 470)
win.set_title("Welcome to Blue Wave")

# image_path = "/usr/share/pixmaps/bluewave-logo.png"
# image = Gtk.Image()
# image.set_from_file(image_path)
# image.set_pixel_size(50)
# image.set_size_request(50, 50)

label = Gtk.Label()
label.set_text("Welcome to Blue Wave!")
label.set_size_request(150, 30)

label2 = Gtk.Label()
label2.set_text("An Arch-based distro that's made for everyone.")
label2.set_size_request(150, 30)

button1 = Gtk.Button(label="Update")
button1.connect("clicked", on_button1_clicked)
button1.set_size_request(400, 40)
button1.set_halign(Gtk.Align.CENTER) 

button2 = Gtk.Button(label="Clean system")
button2.connect("clicked", on_button2_clicked)
button2.set_size_request(400, 40)
button2.set_halign(Gtk.Align.CENTER) 

button3 = Gtk.Button(label="Documentation")
button3.connect("clicked", on_button3_clicked)
button3.set_size_request(400, 40)
button3.set_halign(Gtk.Align.CENTER) 

button4 = Gtk.Button(label="Manage/create snapshots")
button4.connect("clicked", on_button4_clicked)
button4.set_size_request(400, 40)
button4.set_halign(Gtk.Align.CENTER)

button5 = Gtk.Button (label="Remove from autostart and exit")
button5.connect("clicked", on_button5_clicked)
button5.set_size_request(400, 40)
button5.set_halign(Gtk.Align.CENTER) 

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
box.pack_start(logo_image, False, False, 0)
box.pack_start(label, False, False, 0)
box.pack_start(label2, False, False, 0)
box.pack_start(button1, False, False, 0)
box.pack_start(button2, False, False, 0)
box.pack_start(button3, False, False, 0)
box.pack_start(button4, False, False, 0)
box.pack_start(button5, False, False, 0)

win.add(box)
win.show_all()

Gtk.main()

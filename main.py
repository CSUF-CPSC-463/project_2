# Hotel Assignment Project
#

try:
    import Tkinter as tk
    import ttk
except ImportError:
    try:
        import tkinter as tk
        import tkinter.ttk as ttk
    except ImportError:
        print("Could not import tkinter!")

# ============================================================================================
# CLASSES
# classes we may use when creating functionality to code (they do nothing atm)

class HotelRoom:
    """ Hotel Room Class """
    def __init__(self, room_num="000", room_type="King", room_status="unavailable"):
        self.room_num = room_num
        self.room_type = room_type
        self.room_status = room_status

    def get_room_num(self):
        return self.room_num
    def set_room_num(self, room_num):
        self.room_num = room_num

    def get_room_type(self):
        return self.room_type
    def set_room_type(self, room_type):
        self.room_type = room_type

    def get_room_status(self):
        return self.room_status
    def set_room_status(self, room_status):
        self.room_status = room_status


class Guest:
    """ Guest Class """
    def __init__(
                self, first_name="John", last_name="Smith", phone="555-555-5555",
                address="5555 Street Ave, Ca, 55555", email="myEmail@gmail.com"
                ):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.email = email

    def get_first_name(self):
        return self.first_name
    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone

    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address

    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email

# ============================================================================================
# SET DEFAULTS FOR THE MAIN WINDOWS

'''
    This code is what influences the main window that pops up as soon as the app runs.
    (size of window, name of window, etc)
    root "hosts" all the frames (screens) that are being displayed in the GUI
'''
root = tk.Tk()
root.title("Hotel Management App")
root.geometry("600x400")
# ============================================================================================
# CREATE FRAMES

'''
    This code initializes the frames(screens) that we will be using.
    WelcomeFrame is the first screen and serves no purpose other then to welcome users.
    WelcomeFrame leads to main_frame, which hosts the tab system (my_tabs).
    my_tabs hosts all our frames, allowing our frames to be swapped and displayed.
        (so our capability screens are in a tab widget which is displayed on the main_frame)
        (a group of frames within a single frame)
'''
welcome_frame = tk.LabelFrame(root, padx=5, pady=5)
main_frame = tk.Frame(root)

# create tab widget before creating capability frames
my_tabs = ttk.Notebook(main_frame)
my_tabs.pack(pady=15)

# create capability frames
frame1 = tk.Frame(my_tabs)      # capability 1
frame2 = tk.Frame(my_tabs)      # capability 2
frame3 = tk.Frame(my_tabs)      # capability 3
frame4 = tk.Frame(my_tabs)      # capability 4
frame5 = tk.Frame(my_tabs)      # capability 5
frame6 = tk.Frame(my_tabs)      # capability 6
frame7 = tk.Frame(my_tabs)      # capability 7
frame8 = tk.Frame(my_tabs)      # capability 8


# ============================================================================================
# WELCOME: CODE BLOCK
def go_menu():
    welcome_frame.forget()
    main_frame.pack()


# WELCOME: create widgets
welcome_title = tk.Label(welcome_frame, text="Totally Legit Hotel App", font=("Times", 20, "bold"))
welcome_button = tk.Button(welcome_frame, text="Start", padx=25, command=go_menu)

# WELCOME: set widgets
welcome_title.pack()
welcome_button.pack()
welcome_frame.pack(pady=125)
# ============================================================================================
# MAIN: CODE BLOCK

# MAIN: create widgets
menu_label = tk.Button(main_frame, text="Main Menu", font=("Times", 20, "bold"))

# MENU: set widgets
menu_label.pack()
# ============================================================================================

# TODO
# BLOCK CODES GO HERE (look at "WELCOME: CODE BLOCK" above as an example)
# BLOCK CODES GO HERE
# BLOCK CODES GO HERE

# ============================================================================================
# SET CAPABILITY FRAMES AND ADDS THEM INTO TAB SYSTEM
'''
    "Setting(pack)" can be seen as "finalizing a screen".
    Once you have define and added all the desired widgets you
    want on a screen, you pack it, meaning it done being
    changed and can now be visible on screen
'''
# packs the frames
frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)
frame5.pack(fill="both", expand=1)
frame6.pack(fill="both", expand=1)
frame7.pack(fill="both", expand=1)
frame8.pack(fill="both", expand=1)

# adds frames to tab system
my_tabs.add(frame1, text="Room Status")
my_tabs.add(frame2, text="Show Rooms")
my_tabs.add(frame3, text="Reservation")
my_tabs.add(frame4, text="Housekeeping")
my_tabs.add(frame5, text="Manage Guest")
my_tabs.add(frame6, text="All Guest")
my_tabs.add(frame7, text="Search Guest")
my_tabs.add(frame8, text="Report")

# ============================================================================================
# Ending of GUI CODE
root.mainloop()

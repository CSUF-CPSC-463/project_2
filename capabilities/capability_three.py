from rooms_manager import get_hotel_rooms, update_room, update_room_by_number, get_hotel_room_by_num
from guest_manager import add_guest, get_guests, update_guest_by_room

import datetime
import re

try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        print("Could not import tkinter!")

class CapabilityThree:
    def __init__(self, frame, notebook, guest_stay_frame):
        self.frame = frame
        self.current_state = []
        self.notebook = notebook
        self.stay_frame = guest_stay_frame

        self.show_main()

    def show_main(self):
        self.clear_current_state()

        guest_registration_title = tk.Label(self.frame, text="Guest Registration", font=("Times", 20, "bold"))
        guest_registration_title.grid(row = 1, column = 3, padx=15, pady=15)
        self.current_state.append(guest_registration_title)

        check_reservations = tk.Button(self.frame, text="Add Reservation", command=self.show_guest_reservation)
        check_reservations.grid(row = 2, column = 1, padx=15, pady=15)
        self.current_state.append(check_reservations)

        delete_reservations = tk.Button(self.frame, text="Delete Reservation", command=self.show_delete_reservation)
        delete_reservations.grid(row = 2, column = 2, padx=15, pady=15)
        self.current_state.append(delete_reservations)

        show_reservations = tk.Button(self.frame, text="Show Reservations", command=self.show_reservations)
        show_reservations.grid(row = 2, column = 3, padx=15, pady=15)
        self.current_state.append(show_reservations)

    def clear_current_state(self):
        for widget in self.current_state:
            widget.grid_remove()
        self.current_state = []

    def show_guest_reservation(self):
        self.clear_current_state()

        guest_registration_title = tk.Label(self.frame, text="Guest Registration", font=("Times", 20, "bold"))
        guest_registration_title.grid(row = 1, column = 2, padx=15, pady=15)
        self.current_state.append(guest_registration_title)

        first_name = tk.Label(self.frame, text="First Name", font=("Times", 20, "bold"))
        first_name.grid(row = 2, column = 1, padx=15, pady=15)
        self.current_state.append(first_name)

        first_name_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        first_name_entry.grid(row = 2, column = 2, padx=15, pady=15)
        self.current_state.append(first_name_entry)

        last_name = tk.Label(self.frame, text="Last Name", font=("Times", 20, "bold"))
        last_name.grid(row = 3, column = 1, padx=15, pady=15)
        self.current_state.append(last_name)

        last_name_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        last_name_entry.grid(row = 3, column = 2, padx=15, pady=15)
        self.current_state.append(last_name_entry)

        phone = tk.Label(self.frame, text="Phone", font=("Times", 20, "bold"))
        phone.grid(row = 4, column = 1, padx=15, pady=15)
        self.current_state.append(phone)

        phone_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        phone_entry.grid(row = 4, column = 2, padx=15, pady=15)
        self.current_state.append(phone_entry)

        vehicle_plate = tk.Label(self.frame, text="ID No.", font=("Times", 20, "bold"))
        vehicle_plate.grid(row = 2, column = 3, padx=15, pady=15)
        self.current_state.append(vehicle_plate)

        vehicle_plate_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        vehicle_plate_entry.grid(row = 2, column = 4, padx=15, pady=15)
        self.current_state.append(vehicle_plate_entry)

        id = tk.Label(self.frame, text="License Plate No.", font=("Times", 20, "bold"))
        id.grid(row = 3, column = 3, padx=15, pady=15)
        self.current_state.append(id)

        id_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        id_entry.grid(row = 3, column = 4, padx=15, pady=15)
        self.current_state.append(id_entry)

        address = tk.Label(self.frame, text="Address", font=("Times", 20, "bold"))
        address.grid(row = 4, column = 3, padx=15, pady=15)
        self.current_state.append(address)

        address_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        address_entry.grid(row = 4, column = 4, padx=15, pady=15)
        self.current_state.append(address_entry)

        email = tk.Label(self.frame, text="Email", font=("Times", 20, "bold"))
        email.grid(row = 6, column = 1, padx=15, pady=15)
        self.current_state.append(email)

        email_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        email_entry.grid(row = 6, column = 2, padx=15, pady=15)
        self.current_state.append(email_entry)

        check_in = tk.Label(self.frame, text="Check-In", font=("Times", 20, "bold"))
        check_in.grid(row = 7, column = 1, padx=15, pady=15)
        self.current_state.append(check_in)

        check_in_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        check_in_entry.grid(row = 7, column = 2, padx=15, pady=15)
        self.current_state.append(check_in_entry)

        check_out = tk.Label(self.frame, text="Check Out", font=("Times", 20, "bold"))
        check_out.grid(row = 7, column = 3, padx=15, pady=15)
        self.current_state.append(check_out)

        check_out_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        check_out_entry.grid(row = 7, column = 4, padx=15, pady=15)
        self.current_state.append(check_out_entry)

        room_type = tk.Label(self.frame, text="Room Type", font=("Times", 20, "bold"))
        room_type.grid(row = 6, column = 3, padx=15, pady=15)
        self.current_state.append(room_type)

        room_type_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        room_type_entry.grid(row = 6, column = 4, padx=15, pady=15)
        self.current_state.append(room_type_entry)

        # room_num = tk.Label(self.frame, text="Room No.", font=("Times", 20, "bold"))
        # room_num.grid(row = 7, column = 3, padx=15, pady=15)
        # self.current_state.append(room_num)

        # room_num_entry = tk.Entry(self.frame, font=("Times", 20, "bold"))
        # room_num_entry.grid(row = 7, column = 4, padx=15, pady=15)
        # self.current_state.append(room_num_entry)

        # Fixed values for now
        daily_rate = tk.Label(self.frame, text="Daily Rate", font=("Times", 20, "bold"))
        daily_rate.grid(row = 13, column = 1, padx=15, pady=15)
        self.current_state.append(daily_rate)

        total_charge = tk.Label(self.frame, text="Total Charge", font=("Times", 20, "bold"))
        total_charge.grid(row = 13, column = 2, padx=15, pady=15)
        self.current_state.append(total_charge)

        daily_rate_value = tk.Label(self.frame, text="$30", font=("Times", 15))
        daily_rate_value.grid(row = 14, column = 1, padx=15, pady=15)
        self.current_state.append(daily_rate_value)

        total_charge_value = tk.Label(self.frame, text="$200", font=("Times", 15))
        total_charge_value.grid(row = 14, column = 2, padx=15, pady=15)
        self.current_state.append(total_charge_value)

        check_availability = tk.Button(self.frame, text="Check Availability", command=lambda room=room_type_entry,
                                        check_in=check_in_entry, check_out=check_out_entry: self.check_availability(room, check_in, check_out))
        check_availability.grid(row = 15, column = 1, padx=15, pady=15)
        self.current_state.append(check_availability)
        
        reserve = tk.Button(self.frame, text="Reserve Room", command=lambda room_type=room_type_entry,
                            guest={
                                "fname": first_name_entry,
                                "lname": last_name_entry,
                                "phone": phone_entry,
                                "address": address_entry,
                                "email": email_entry,
                                "vehicle": vehicle_plate_entry,
                                "id": id_entry,
                                "room_type": room_type_entry,
                                "chk_in": check_in_entry,
                                "chk_out": check_out_entry,
                                "img_path": ".res/placeholder.png"
                            }, check_in=check_in_entry, check_out=check_out_entry: self.add_reservation(room_type, guest, check_in, check_out))
        reserve.grid(row = 15, column = 2, padx=15, pady=15)
        self.current_state.append(reserve)
        
        go_back = tk.Button(self.frame, text="Back", command=self.show_main)
        go_back.grid(row = 16, column = 1, padx=15, pady=15)
        self.current_state.append(go_back)


    def show_reservations(self):
        self.clear_current_state()

        group = tk.LabelFrame(self.frame, text="Rooms", font=("Times", 20, "bold"))
        self.current_state.append(group)
        guests = get_guests()

        for i, room in enumerate(guests):
            hotel_room_obj = get_hotel_room_by_num(room.rm_number)
            if hotel_room_obj is None:
                print("Invalid room reserved!")
                continue
            room_color = hotel_room_obj.get_room_color(datetime.datetime.today().weekday())
            room_button = tk.Button(group, text="Room " + room.rm_number, font=("Times", 20, "bold"), bg=room_color, command=lambda guest=room: self.switch_to_guest_profile(guest))
            room_button.grid(row = i, column = 1, padx=15, pady=15)
        group.grid(row = 1, column = 1, padx=15, pady=15)

        go_back = tk.Button(self.frame, text="Back", command=self.show_main)
        go_back.grid(row = 15, column = 1, padx=15, pady=15)
        self.current_state.append(go_back)

    def clear_and_set(self, widget_name, text):
        self.stay_frame.nametowidget(widget_name).config(text=text)

    def switch_to_guest_profile(self, guest):
        self.clear_and_set("name", guest.fname + " " + guest.lname)
        self.clear_and_set("check_in", guest.chk_in)
        self.clear_and_set("check_out", guest.chk_out)
        self.clear_and_set("rate", "$10")
        self.clear_and_set("total", "$110")
        self.clear_and_set("paid", "$100")
        self.clear_and_set("remain", "$10")

        self.notebook.select(5)

    def show_delete_reservation(self):
        self.clear_current_state()

        guest_registration_title = tk.Label(self.frame, text="Guest Registration", font=("Times", 20, "bold"))
        guest_registration_title.grid(row = 1, column = 3, padx=15, pady=15)
        self.current_state.append(guest_registration_title)

        group = tk.LabelFrame(self.frame, text="Rooms", font=("Times", 20, "bold"))
        self.current_state.append(group)
        guests = get_guests()
        
        for i, guest in enumerate(guests):
            room = guest.rm_number
            room_button = tk.Button(group, text="Room " + room, font=("Times", 20, "bold"), bg="orange", command=lambda guest=guest: self.delete_reservation(guest))
            room_button.grid(row = i, column = 1, padx=15, pady=15)
            self.current_state.append(room_button)

        group.grid(row = 12, column = 7, padx=2, pady=2)

        go_back = tk.Button(self.frame, text="Back", command=self.show_main)
        go_back.grid(row = 13, column = 1, padx=15, pady=15)
        self.current_state.append(go_back)

    def transform_to_datetime(self, date):
        if re.match(r'\d{2}\/\d{2}\/\d{4}', date) is None:
            print("Invalid Check-in/Check-out format. Please use MM/DD/YYYY format!")
            return None
        
        stripped_date = date.split('/')

        return datetime.date(month=int(stripped_date[0]), day=int(stripped_date[1]), year=int(stripped_date[2]))

    def add_reservation(self, room_type, guest, check_in, check_out):
        rooms = get_hotel_rooms()
        check_in = check_in.get()
        check_out = check_out.get()

        check_in_date = self.transform_to_datetime(check_in)
        check_out_date = self.transform_to_datetime(check_out)
            
        if not check_in_date or not check_out_date:
            print("Invalid Date. Please use MM/DD/YYYY format!")
            return

        for index, room in enumerate(rooms):
            if room.room_type == room_type.get() and self.room_is_available(room, check_in_date, check_out_date):
                add_guest(guest, room, check_in, check_out)
                update_room(index, "Unavailable", check_in_date.weekday(), check_out_date.weekday())
                print("Room Reserved")
                return

    def check_availability(self, room_type, check_in, check_out):
        check_in = check_in.get()
        check_out = check_out.get()
        rooms = get_hotel_rooms()

        check_in_date = self.transform_to_datetime(check_in)
        check_out_date = self.transform_to_datetime(check_out)
            
        if not check_in_date or not check_out_date:
            print("Invalid Date. Please use MM/DD/YYYY format!")
            return False

        for room in rooms:
            if room.room_type == room_type.get() and self.room_is_available(room, check_in_date, check_out_date):
                print("Room Available")
                return True

        print("Room Unavailable")
        return False

    def room_is_available(self, room, check_in, check_out, convert=False):
        if convert:
            room = get_hotel_room_by_num(room.get())
            check_in = check_in.get()
            check_out = check_out.get()
                
            check_in_date = self.transform_to_datetime(check_in)
            check_out_date = self.transform_to_datetime(check_out)

            if not check_in_date or not check_out_date:
                print("Invalid Date. Please use MM/DD/YYYY format!")
                return False

            if check_in == check_out:
                print("Please only reserve rooms for 6 days or less and cannot check-in and check_out on the same day!")
                return

            for i in range(check_in_date.weekday() % 7, check_out_date.weekday()%7):
                if room.room_week[str(i)] != "Available":
                    print("Room Unavailable")
                    return False
            print("Room Available")
            return True

        if check_in == check_out:
            print("Please only reserve rooms for 6 days or less and cannot check-in and check_out on the same day!")
            return 
        for i in range(check_in.weekday() % 7, check_out.weekday()%7):
            if room.room_week[str(i)] != "Available":
                print("Room Unavailable")
                return False
        print("Room Available")
        return True

    def delete_reservation(self, guest):
        room = guest.rm_number
        update_room_by_number(room, "Available", self.transform_to_datetime(guest.chk_in).weekday(), self.transform_to_datetime(guest.chk_out).weekday())
        update_guest_by_room(room)

        self.show_delete_reservation()


    def go_back(self):
        previous_state = self.previous_state.pop()
        for widget in previous_state:
            widget.grid()

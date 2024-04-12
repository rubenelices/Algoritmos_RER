class Hotel:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        self._name = name
        self._rooms = []
        self._employees = []
        self._reservations = {}


        def name(self):
            return self._name

    def add_room(self, room):
        if not isinstance(room, room):
            raise ValueError("Invalid room object")
        self._rooms.append(room)

    def remove_room(self, room_number):
        self._rooms = [room for room in self._rooms if room.number != room_number]

    def add_employee(self, employee):
        if not isinstance(employee, employee):
            raise ValueError("Invalid employee object")
        self._employees.append(employee)

    def remove_employee(self, emp_id):
        self._employees = [emp for emp in self._employees if emp.emp_id != emp_id]

    def check_in(self, room_number, guest_name):
        if room_number in self._reservations:
            raise Exception("Room is already reserved")
        room = self.find_room(room_number)
        if room is None:
            raise ValueError("Room not found")
        if room.is_occupied():
            raise Exception("Room is already occupied")
        room.check_in()
        self._reservations[room_number] = guest_name

    def check_out(self, room_number):
        room = self.find_room(room_number)
        if room is None:
            raise ValueError("Room not found")
        if not room.is_occupied():
            raise Exception("Room is not occupied")
        room.check_out()
        del self._reservations[room_number]

    def find_room(self, room_number):
        for room in self._rooms:
            if room.number == room_number:
                return room
        return None

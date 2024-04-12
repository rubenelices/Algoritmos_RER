from enum import Enum

class RoomType(Enum):
    INDIVIDUAL = "Individual"
    DOBLE = "Doble"
    SUITE = "Suite"

class Room:
    def __init__(self, room_type, room_number, room_state, room_price):
        if not isinstance(room_type, RoomType):
            raise ValueError("room_type must be an instance of RoomType Enum")
        if not isinstance(room_number, int):
            raise ValueError("room_number must be an integer")
        if room_state not in ["Ocupada", "Desocupada"]:
            raise ValueError("room_state must be 'Ocupada' or 'Desocupada'")
        if not isinstance(room_price, (int, float)) or room_price <= 0:
            raise ValueError("room_price must be a positive number")
        
        self._room_type = room_type
        self._room_number = room_number
        self._room_state = room_state
        self._room_price = room_price

    def room_type(self):
        return self._room_type.value 
    def room_number(self):
        return self._room_number


    def room_state(self):
        return self._room_state


    def room_price(self):
        return self._room_price

    
    def room_price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("room_price must be a positive number")
        self._room_price = value

    def is_occupied(self):
        return self._room_state == "Ocupada"

    def check_in(self):
        if self.is_occupied():
            return "La habitación ya está ocupada."
        self._room_state = "Ocupada"
        return "Check-in realizado con éxito."

    def check_out(self):
        if not self.is_occupied():
            return "La habitación ya está desocupada."
        self._room_state = "Desocupada"
        return "Check-out realizado con éxito."



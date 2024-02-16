from dataclasses import dataclass

@dataclass
class User:
    name: str
    gender: str

@dataclass
class Vehicle:
    registration_number: str
    user_name: str
    name: str

@dataclass
class Ride:
    id: int
    registration_number: str
    origin: str
    destination: str
    ended: bool
    available_seats: int
    occupied_seats: int

@dataclass
class Booking:
    ride_id: int
    seats: int
    user_name: str

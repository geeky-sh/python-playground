from typing import List
from .domain import User, Booking, Ride, Vehicle

class UserRepo:
    users: List[User]

    def __init__(self) -> None:
        self.users = []

    def add(self, name: str, gender: str) -> User:
        user = User(name=str, gender=str)
        self.users.append(user)
        return user

    def find(self, name: str) -> User:
        for user in self.users:
            if user.name == name:
                return user

    def list(self) -> List[User]:
        return self.users

class VehicleRepo:
    vehicles: List[Vehicle]

    def __init__(self) -> None:
        self.vehicles = []

    def find(self, registration_number: str) -> Vehicle:
        for vehicle in self.vehicles:
            if registration_number == vehicle.registration_number:
                return vehicle

    def add(self, registration_number: str, name: str, user_name: str) -> Vehicle:
        vehicle = Vehicle(registration_number=registration_number, name=name, user_name=user_name)
        self.vehicles.append(vehicle)
        return vehicle


class RideRepo:
    counter: int
    rides: List[Ride]

    def __init__(self) -> None:
        self.counter = 0
        self.rides = []

    def add(self, name: str, registration_number: str, origin: str, destination: str, available_seats: int) -> Ride:
        self.counter += 1
        ride = Ride(id=self.counter, registration_number=registration_number,
                    origin=origin, destination=destination, available_seats=available_seats)
        self.rides.append(ride)
        return ride

    def find(self, ride_id) -> Ride:
        for ride in self.rides:
            if ride.id == ride_id:
                return ride
            
    def find_by_attr(self, user_name)

    def end(self, ride_id) -> Ride:
        ride = self.find(ride_id=ride_id)
        if ride is not None:
            ride.ended = True
        return ride

    def list(self, origin: str, destination: str) -> List[Ride]:
        return [ride for ride in self.rides if origin == ride.origin and destination == ride.destination]

class BookingRepo:
    booking: List[Booking]

    def add(self, user_name: str, ride_id: int, seats: int) -> Booking:
        booking = Booking(ride_id=ride_id, seats=seats, user_name=user_name)
        self.booking.append(booking)
        return booking

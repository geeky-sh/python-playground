from typing import List
from .repository import UserRepo, VehicleRepo, BookingRepo, RideRepo
from .domain import User, Vehicle, Booking, Ride

class Service:
    users: List[User]
    bookings: List[Booking]
    Ride: List[Ride]
    vehicles: List[Vehicle]

    def __init__(self) -> None:
        self.booking_repo = BookingRepo()
        self.user_repo = UserRepo()
        self.vehicle_repo = VehicleRepo()
        self.ride_repo = RideRepo()

    """
    get user by name
    get vehicle by registration_number
    get available rides sorted by vacancy
    get available rides filtered by vehicle
    create booking
    increment occupied in ride.
    end ride
    """

    def add_user(self, name: str, gender: str) -> User:
        """
        check if user account already exists,
        if yes, raise an exception, if no, create user
        """

    def add_vehicle(self, user_name: str, vehicle_name: str, registration_number: str):
        """
        check if user account valid, if not raise an exception (r)
        check if vehicle already exists, if yes, raise an exception
        if the user is already part of the non-ended ride, raise an exception
        create vehicle
        """
        pass

    def offer_ride(self, user_name: str, origin: str, destination: str, available_seats: str, registration_number: str):
        """
        check if vehicle and user_name is valid, if not raise an exception
        check if the same vehicle is already offering a ride, if yes, raise an exception.
        create ride
        """
        pass

    def select_ride(user_name: str, origin: str, destination: str, seats: str, strategy: int, preferred_vehicle: str):
        """
        check if user is part of an existing non-ended ride, if yes raise exception
        if strategy is 1, most vacant
            get all non filled rides sorted by occupancy
            get the first one
        if strategy is 2, preferred
            if preferred argument is empty, raise an exception
            get non-filled rides for that vehicle, if not found, get all-non-filled rides sorted by occupancy
            get the first ride
        create booking for the ride
        """

    def end_ride(ride_id: str):
        pass

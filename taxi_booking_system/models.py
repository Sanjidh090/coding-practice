"""
Models for Taxi Booking System
Contains classes for Customer, Driver, Administrator, and Booking
"""

from datetime import datetime
from typing import List, Optional


class User:
    """Base class for all users in the system"""
    def __init__(self, user_id: str, username: str, password: str, name: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name

    def to_string(self) -> str:
        """Convert user to string for file storage"""
        return f"{self.user_id}|{self.username}|{self.password}|{self.name}"


class Customer(User):
    """Customer class with registration details"""
    def __init__(self, user_id: str, username: str, password: str, name: str, 
                 address: str, phone: str, email: str):
        super().__init__(user_id, username, password, name)
        self.address = address
        self.phone = phone
        self.email = email

    def to_string(self) -> str:
        """Convert customer to string for file storage"""
        return f"{self.user_id}|{self.username}|{self.password}|{self.name}|{self.address}|{self.phone}|{self.email}"

    @staticmethod
    def from_string(data: str) -> 'Customer':
        """Create customer from string"""
        parts = data.strip().split('|')
        if len(parts) >= 7:
            return Customer(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6])
        return None


class Driver(User):
    """Driver class"""
    def __init__(self, user_id: str, username: str, password: str, name: str, 
                 phone: str, license_number: str):
        super().__init__(user_id, username, password, name)
        self.phone = phone
        self.license_number = license_number

    def to_string(self) -> str:
        """Convert driver to string for file storage"""
        return f"{self.user_id}|{self.username}|{self.password}|{self.name}|{self.phone}|{self.license_number}"

    @staticmethod
    def from_string(data: str) -> 'Driver':
        """Create driver from string"""
        parts = data.strip().split('|')
        if len(parts) >= 6:
            return Driver(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
        return None


class Administrator(User):
    """Administrator class"""
    def __init__(self, user_id: str, username: str, password: str, name: str):
        super().__init__(user_id, username, password, name)

    @staticmethod
    def from_string(data: str) -> 'Administrator':
        """Create administrator from string"""
        parts = data.strip().split('|')
        if len(parts) >= 4:
            return Administrator(parts[0], parts[1], parts[2], parts[3])
        return None


class Booking:
    """Booking class for taxi bookings"""
    def __init__(self, booking_id: str, customer_id: str, pickup_location: str, 
                 dropoff_location: str, booking_date: str, booking_time: str, 
                 status: str = "Pending", driver_id: str = ""):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.booking_date = booking_date
        self.booking_time = booking_time
        self.status = status  # Pending, Assigned, Completed, Cancelled
        self.driver_id = driver_id

    def to_string(self) -> str:
        """Convert booking to string for file storage"""
        return f"{self.booking_id}|{self.customer_id}|{self.pickup_location}|{self.dropoff_location}|{self.booking_date}|{self.booking_time}|{self.status}|{self.driver_id}"

    @staticmethod
    def from_string(data: str) -> 'Booking':
        """Create booking from string"""
        parts = data.strip().split('|')
        if len(parts) >= 8:
            return Booking(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7])
        return None

    def get_datetime(self) -> datetime:
        """Get datetime object from booking date and time"""
        try:
            return datetime.strptime(f"{self.booking_date} {self.booking_time}", "%Y-%m-%d %H:%M")
        except:
            return None

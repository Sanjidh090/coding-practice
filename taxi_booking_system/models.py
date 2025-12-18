"""
Models for Taxi Booking System
Contains classes for Customer, Driver, Administrator, and Booking
Enhanced with password hashing and location support
"""

from datetime import datetime
from typing import List, Optional
import hashlib


class User:
    """Base class for all users in the system"""
    def __init__(self, user_id: str, username: str, password: str, name: str, is_hashed: bool = False):
        self.user_id = user_id
        self.username = username
        # Hash password if not already hashed
        self.password = password if is_hashed else self._hash_password(password)
        self.name = name

    @staticmethod
    def _hash_password(password: str) -> str:
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str) -> bool:
        """Verify password against stored hash"""
        return self.password == self._hash_password(password)

    def to_string(self) -> str:
        """Convert user to string for file storage"""
        return f"{self.user_id}|{self.username}|{self.password}|{self.name}"


class Customer(User):
    """Customer class with registration details"""
    def __init__(self, user_id: str, username: str, password: str, name: str, 
                 address: str, phone: str, email: str, is_hashed: bool = False):
        super().__init__(user_id, username, password, name, is_hashed)
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
            # Password is already hashed in file
            return Customer(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], is_hashed=True)
        return None


class Driver(User):
    """Driver class with location tracking"""
    def __init__(self, user_id: str, username: str, password: str, name: str, 
                 phone: str, license_number: str, latitude: float = 0.0, 
                 longitude: float = 0.0, is_hashed: bool = False):
        super().__init__(user_id, username, password, name, is_hashed)
        self.phone = phone
        self.license_number = license_number
        self.latitude = latitude
        self.longitude = longitude
        self.is_available = True

    def to_string(self) -> str:
        """Convert driver to string for file storage"""
        return f"{self.user_id}|{self.username}|{self.password}|{self.name}|{self.phone}|{self.license_number}|{self.latitude}|{self.longitude}"

    @staticmethod
    def from_string(data: str) -> 'Driver':
        """Create driver from string"""
        parts = data.strip().split('|')
        if len(parts) >= 6:
            lat = float(parts[6]) if len(parts) > 6 else 0.0
            lon = float(parts[7]) if len(parts) > 7 else 0.0
            # Password is already hashed in file
            return Driver(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], lat, lon, is_hashed=True)
        return None


class Administrator(User):
    """Administrator class"""
    def __init__(self, user_id: str, username: str, password: str, name: str, is_hashed: bool = False):
        super().__init__(user_id, username, password, name, is_hashed)

    @staticmethod
    def from_string(data: str) -> 'Administrator':
        """Create administrator from string"""
        parts = data.strip().split('|')
        if len(parts) >= 4:
            # Password is already hashed in file
            return Administrator(parts[0], parts[1], parts[2], parts[3], is_hashed=True)
        return None


class Booking:
    """Booking class for taxi bookings with location coordinates"""
    def __init__(self, booking_id: str, customer_id: str, pickup_location: str, 
                 dropoff_location: str, booking_date: str, booking_time: str, 
                 status: str = "Pending", driver_id: str = "",
                 pickup_lat: float = 0.0, pickup_lon: float = 0.0,
                 dropoff_lat: float = 0.0, dropoff_lon: float = 0.0):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.booking_date = booking_date
        self.booking_time = booking_time
        self.status = status  # Pending, Assigned, Completed, Cancelled
        self.driver_id = driver_id
        self.pickup_lat = pickup_lat
        self.pickup_lon = pickup_lon
        self.dropoff_lat = dropoff_lat
        self.dropoff_lon = dropoff_lon

    def to_string(self) -> str:
        """Convert booking to string for file storage"""
        return f"{self.booking_id}|{self.customer_id}|{self.pickup_location}|{self.dropoff_location}|{self.booking_date}|{self.booking_time}|{self.status}|{self.driver_id}|{self.pickup_lat}|{self.pickup_lon}|{self.dropoff_lat}|{self.dropoff_lon}"

    @staticmethod
    def from_string(data: str) -> 'Booking':
        """Create booking from string"""
        parts = data.strip().split('|')
        if len(parts) >= 8:
            pickup_lat = float(parts[8]) if len(parts) > 8 else 0.0
            pickup_lon = float(parts[9]) if len(parts) > 9 else 0.0
            dropoff_lat = float(parts[10]) if len(parts) > 10 else 0.0
            dropoff_lon = float(parts[11]) if len(parts) > 11 else 0.0
            return Booking(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7],
                         pickup_lat, pickup_lon, dropoff_lat, dropoff_lon)
        return None

    def get_datetime(self) -> datetime:
        """Get datetime object from booking date and time"""
        try:
            return datetime.strptime(f"{self.booking_date} {self.booking_time}", "%Y-%m-%d %H:%M")
        except (ValueError, TypeError):
            return None

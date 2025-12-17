"""
Data Manager for Taxi Booking System
Handles file operations for storing and retrieving data
"""

import os
from typing import List, Optional
from models import Customer, Driver, Administrator, Booking


class DataManager:
    """Manages data persistence using text files"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.customers_file = os.path.join(data_dir, "customers.txt")
        self.drivers_file = os.path.join(data_dir, "drivers.txt")
        self.admins_file = os.path.join(data_dir, "administrators.txt")
        self.bookings_file = os.path.join(data_dir, "bookings.txt")
        self._ensure_data_files()

    def _ensure_data_files(self):
        """Create data directory and files if they don't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        # Create files with default admin if they don't exist
        if not os.path.exists(self.customers_file):
            open(self.customers_file, 'w').close()
        
        if not os.path.exists(self.drivers_file):
            # Create sample drivers
            with open(self.drivers_file, 'w') as f:
                f.write("D001|driver1|pass123|John Driver|555-0101|DL001\n")
                f.write("D002|driver2|pass123|Jane Driver|555-0102|DL002\n")
                f.write("D003|driver3|pass123|Bob Driver|555-0103|DL003\n")
        
        if not os.path.exists(self.admins_file):
            # Create default admin
            with open(self.admins_file, 'w') as f:
                f.write("A001|admin|admin123|System Administrator\n")
        
        if not os.path.exists(self.bookings_file):
            open(self.bookings_file, 'w').close()

    # Customer operations
    def save_customer(self, customer: Customer) -> bool:
        """Save a new customer"""
        try:
            with open(self.customers_file, 'a') as f:
                f.write(customer.to_string() + "\n")
            return True
        except Exception as e:
            print(f"Error saving customer: {e}")
            return False

    def get_all_customers(self) -> List[Customer]:
        """Get all customers"""
        customers = []
        try:
            with open(self.customers_file, 'r') as f:
                for line in f:
                    if line.strip():
                        customer = Customer.from_string(line)
                        if customer:
                            customers.append(customer)
        except Exception as e:
            print(f"Error reading customers: {e}")
        return customers

    def get_customer_by_username(self, username: str) -> Optional[Customer]:
        """Get customer by username"""
        customers = self.get_all_customers()
        for customer in customers:
            if customer.username == username:
                return customer
        return None

    def get_customer_by_id(self, customer_id: str) -> Optional[Customer]:
        """Get customer by ID"""
        customers = self.get_all_customers()
        for customer in customers:
            if customer.user_id == customer_id:
                return customer
        return None

    def get_next_customer_id(self) -> str:
        """Generate next customer ID"""
        customers = self.get_all_customers()
        if not customers:
            return "C001"
        max_id = max([int(c.user_id[1:]) for c in customers])
        return f"C{str(max_id + 1).zfill(3)}"

    # Driver operations
    def get_all_drivers(self) -> List[Driver]:
        """Get all drivers"""
        drivers = []
        try:
            with open(self.drivers_file, 'r') as f:
                for line in f:
                    if line.strip():
                        driver = Driver.from_string(line)
                        if driver:
                            drivers.append(driver)
        except Exception as e:
            print(f"Error reading drivers: {e}")
        return drivers

    def get_driver_by_username(self, username: str) -> Optional[Driver]:
        """Get driver by username"""
        drivers = self.get_all_drivers()
        for driver in drivers:
            if driver.username == username:
                return driver
        return None

    def get_driver_by_id(self, driver_id: str) -> Optional[Driver]:
        """Get driver by ID"""
        drivers = self.get_all_drivers()
        for driver in drivers:
            if driver.user_id == driver_id:
                return driver
        return None

    # Administrator operations
    def get_all_admins(self) -> List[Administrator]:
        """Get all administrators"""
        admins = []
        try:
            with open(self.admins_file, 'r') as f:
                for line in f:
                    if line.strip():
                        admin = Administrator.from_string(line)
                        if admin:
                            admins.append(admin)
        except Exception as e:
            print(f"Error reading administrators: {e}")
        return admins

    def get_admin_by_username(self, username: str) -> Optional[Administrator]:
        """Get administrator by username"""
        admins = self.get_all_admins()
        for admin in admins:
            if admin.username == username:
                return admin
        return None

    # Booking operations
    def save_booking(self, booking: Booking) -> bool:
        """Save a new booking"""
        try:
            with open(self.bookings_file, 'a') as f:
                f.write(booking.to_string() + "\n")
            return True
        except Exception as e:
            print(f"Error saving booking: {e}")
            return False

    def get_all_bookings(self) -> List[Booking]:
        """Get all bookings"""
        bookings = []
        try:
            with open(self.bookings_file, 'r') as f:
                for line in f:
                    if line.strip():
                        booking = Booking.from_string(line)
                        if booking:
                            bookings.append(booking)
        except Exception as e:
            print(f"Error reading bookings: {e}")
        return bookings

    def get_bookings_by_customer(self, customer_id: str) -> List[Booking]:
        """Get all bookings for a customer"""
        all_bookings = self.get_all_bookings()
        return [b for b in all_bookings if b.customer_id == customer_id]

    def get_bookings_by_driver(self, driver_id: str) -> List[Booking]:
        """Get all bookings assigned to a driver"""
        all_bookings = self.get_all_bookings()
        return [b for b in all_bookings if b.driver_id == driver_id and b.status != "Cancelled"]

    def get_booking_by_id(self, booking_id: str) -> Optional[Booking]:
        """Get booking by ID"""
        bookings = self.get_all_bookings()
        for booking in bookings:
            if booking.booking_id == booking_id:
                return booking
        return None

    def update_booking(self, booking: Booking) -> bool:
        """Update an existing booking"""
        try:
            bookings = self.get_all_bookings()
            updated = False
            
            with open(self.bookings_file, 'w') as f:
                for b in bookings:
                    if b.booking_id == booking.booking_id:
                        f.write(booking.to_string() + "\n")
                        updated = True
                    else:
                        f.write(b.to_string() + "\n")
            
            return updated
        except Exception as e:
            print(f"Error updating booking: {e}")
            return False

    def get_next_booking_id(self) -> str:
        """Generate next booking ID"""
        bookings = self.get_all_bookings()
        if not bookings:
            return "B001"
        max_id = max([int(b.booking_id[1:]) for b in bookings])
        return f"B{str(max_id + 1).zfill(3)}"

    def check_driver_availability(self, driver_id: str, booking_date: str, booking_time: str) -> bool:
        """Check if driver is available at given date and time"""
        driver_bookings = self.get_bookings_by_driver(driver_id)
        
        from datetime import datetime, timedelta
        try:
            new_booking_dt = datetime.strptime(f"{booking_date} {booking_time}", "%Y-%m-%d %H:%M")
            
            for booking in driver_bookings:
                existing_dt = booking.get_datetime()
                if existing_dt:
                    # Check if bookings overlap (within 2 hours window)
                    time_diff = abs((new_booking_dt - existing_dt).total_seconds() / 3600)
                    if time_diff < 2:
                        return False
            return True
        except (ValueError, TypeError):
            return True

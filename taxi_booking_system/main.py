"""
Taxi Booking System - Main Application
Provides text-based menu interface for all user types
"""

import os
import sys
from datetime import datetime
from models import Customer, Driver, Administrator, Booking
from data_manager import DataManager


class TaxiBookingSystem:
    """Main system class for taxi booking operations"""
    
    def __init__(self):
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(script_dir, "data")
        self.data_manager = DataManager(data_dir)
        self.current_user = None
        self.user_type = None

    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title: str):
        """Print a formatted header"""
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)

    def print_menu(self, options: list):
        """Print a menu with options"""
        print()
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print()

    def get_choice(self, max_option: int) -> int:
        """Get user choice with validation"""
        while True:
            try:
                choice = input("Enter your choice: ").strip()
                choice_num = int(choice)
                if 1 <= choice_num <= max_option:
                    return choice_num
                else:
                    print(f"Please enter a number between 1 and {max_option}")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def main_menu(self):
        """Display main menu"""
        while True:
            self.clear_screen()
            self.print_header("TAXI BOOKING SYSTEM")
            self.print_menu([
                "Customer Login",
                "Customer Registration",
                "Driver Login",
                "Administrator Login",
                "Exit"
            ])
            
            choice = self.get_choice(5)
            
            if choice == 1:
                self.customer_login()
            elif choice == 2:
                self.customer_registration()
            elif choice == 3:
                self.driver_login()
            elif choice == 4:
                self.admin_login()
            elif choice == 5:
                print("\nThank you for using Taxi Booking System!")
                sys.exit(0)

    def customer_login(self):
        """Customer login"""
        self.clear_screen()
        self.print_header("CUSTOMER LOGIN")
        
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        customer = self.data_manager.get_customer_by_username(username)
        
        if customer and customer.verify_password(password):
            self.current_user = customer
            self.user_type = "customer"
            print("\n✓ Login successful!")
            input("Press Enter to continue...")
            self.customer_menu()
        else:
            print("\n✗ Invalid username or password!")
            input("Press Enter to continue...")

    def customer_registration(self):
        """Customer registration"""
        self.clear_screen()
        self.print_header("CUSTOMER REGISTRATION")
        
        print("\nPlease provide your details:")
        username = input("Username: ").strip()
        
        # Check if username already exists
        if self.data_manager.get_customer_by_username(username):
            print("\n✗ Username already exists!")
            input("Press Enter to continue...")
            return
        
        password = input("Password: ").strip()
        name = input("Full Name: ").strip()
        address = input("Address: ").strip()
        phone = input("Phone Number: ").strip()
        email = input("Email: ").strip()
        
        if not all([username, password, name, address, phone, email]):
            print("\n✗ All fields are required!")
            input("Press Enter to continue...")
            return
        
        customer_id = self.data_manager.get_next_customer_id()
        customer = Customer(customer_id, username, password, name, address, phone, email)
        
        if self.data_manager.save_customer(customer):
            print(f"\n✓ Registration successful! Your Customer ID is: {customer_id}")
            print("You can now login with your username and password.")
        else:
            print("\n✗ Registration failed. Please try again.")
        
        input("Press Enter to continue...")

    def customer_menu(self):
        """Customer menu after login"""
        while True:
            self.clear_screen()
            self.print_header(f"CUSTOMER MENU - Welcome {self.current_user.name}")
            self.print_menu([
                "Book a Taxi",
                "View My Bookings",
                "Update Booking",
                "Cancel Booking",
                "Logout"
            ])
            
            choice = self.get_choice(5)
            
            if choice == 1:
                self.book_taxi()
            elif choice == 2:
                self.view_customer_bookings()
            elif choice == 3:
                self.update_booking()
            elif choice == 4:
                self.cancel_booking()
            elif choice == 5:
                self.current_user = None
                self.user_type = None
                break

    def book_taxi(self):
        """Book a taxi"""
        self.clear_screen()
        self.print_header("BOOK A TAXI")
        
        print("\nPlease provide booking details:")
        pickup = input("Pickup Location: ").strip()
        dropoff = input("Drop-off Location: ").strip()
        
        while True:
            date = input("Date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD")
        
        while True:
            time = input("Time (HH:MM): ").strip()
            try:
                datetime.strptime(time, "%H:%M")
                break
            except ValueError:
                print("Invalid time format. Please use HH:MM (24-hour format)")
        
        if not all([pickup, dropoff, date, time]):
            print("\n✗ All fields are required!")
            input("Press Enter to continue...")
            return
        
        booking_id = self.data_manager.get_next_booking_id()
        booking = Booking(booking_id, self.current_user.user_id, pickup, dropoff, 
                         date, time, "Pending", "")
        
        if self.data_manager.save_booking(booking):
            print(f"\n✓ Booking successful! Your Booking ID is: {booking_id}")
            print("Status: Pending (Waiting for driver assignment)")
        else:
            print("\n✗ Booking failed. Please try again.")
        
        input("Press Enter to continue...")

    def view_customer_bookings(self):
        """View customer's bookings"""
        self.clear_screen()
        self.print_header("MY BOOKINGS")
        
        bookings = self.data_manager.get_bookings_by_customer(self.current_user.user_id)
        
        if not bookings:
            print("\nYou have no bookings.")
        else:
            print(f"\nTotal Bookings: {len(bookings)}\n")
            for booking in bookings:
                driver_name = "Not Assigned"
                if booking.driver_id:
                    driver = self.data_manager.get_driver_by_id(booking.driver_id)
                    if driver:
                        driver_name = driver.name
                
                print(f"Booking ID: {booking.booking_id}")
                print(f"From: {booking.pickup_location} → To: {booking.dropoff_location}")
                print(f"Date & Time: {booking.booking_date} at {booking.booking_time}")
                print(f"Status: {booking.status}")
                print(f"Driver: {driver_name}")
                print("-" * 60)
        
        input("\nPress Enter to continue...")

    def update_booking(self):
        """Update a booking"""
        self.clear_screen()
        self.print_header("UPDATE BOOKING")
        
        bookings = self.data_manager.get_bookings_by_customer(self.current_user.user_id)
        pending_bookings = [b for b in bookings if b.status == "Pending"]
        
        if not pending_bookings:
            print("\nYou have no pending bookings to update.")
            input("Press Enter to continue...")
            return
        
        print("\nYour Pending Bookings:")
        for i, booking in enumerate(pending_bookings, 1):
            print(f"\n{i}. Booking ID: {booking.booking_id}")
            print(f"   From: {booking.pickup_location} → To: {booking.dropoff_location}")
            print(f"   Date & Time: {booking.booking_date} at {booking.booking_time}")
        
        print(f"\n{len(pending_bookings) + 1}. Go Back")
        choice = self.get_choice(len(pending_bookings) + 1)
        
        if choice == len(pending_bookings) + 1:
            return
        
        booking = pending_bookings[choice - 1]
        
        print("\n\nEnter new details (press Enter to keep current value):")
        pickup = input(f"Pickup Location [{booking.pickup_location}]: ").strip()
        dropoff = input(f"Drop-off Location [{booking.dropoff_location}]: ").strip()
        date = input(f"Date [{booking.booking_date}]: ").strip()
        time = input(f"Time [{booking.booking_time}]: ").strip()
        
        # Update only if new values provided
        if pickup:
            booking.pickup_location = pickup
        if dropoff:
            booking.dropoff_location = dropoff
        if date:
            try:
                datetime.strptime(date, "%Y-%m-%d")
                booking.booking_date = date
            except ValueError:
                print("Invalid date format. Keeping original date.")
        if time:
            try:
                datetime.strptime(time, "%H:%M")
                booking.booking_time = time
            except ValueError:
                print("Invalid time format. Keeping original time.")
        
        if self.data_manager.update_booking(booking):
            print("\n✓ Booking updated successfully!")
        else:
            print("\n✗ Failed to update booking.")
        
        input("Press Enter to continue...")

    def cancel_booking(self):
        """Cancel a booking"""
        self.clear_screen()
        self.print_header("CANCEL BOOKING")
        
        bookings = self.data_manager.get_bookings_by_customer(self.current_user.user_id)
        active_bookings = [b for b in bookings if b.status != "Cancelled" and b.status != "Completed"]
        
        if not active_bookings:
            print("\nYou have no active bookings to cancel.")
            input("Press Enter to continue...")
            return
        
        print("\nYour Active Bookings:")
        for i, booking in enumerate(active_bookings, 1):
            print(f"\n{i}. Booking ID: {booking.booking_id}")
            print(f"   From: {booking.pickup_location} → To: {booking.dropoff_location}")
            print(f"   Date & Time: {booking.booking_date} at {booking.booking_time}")
            print(f"   Status: {booking.status}")
        
        print(f"\n{len(active_bookings) + 1}. Go Back")
        choice = self.get_choice(len(active_bookings) + 1)
        
        if choice == len(active_bookings) + 1:
            return
        
        booking = active_bookings[choice - 1]
        
        confirm = input(f"\nAre you sure you want to cancel booking {booking.booking_id}? (yes/no): ").strip().lower()
        if confirm == 'yes':
            booking.status = "Cancelled"
            if self.data_manager.update_booking(booking):
                print("\n✓ Booking cancelled successfully!")
            else:
                print("\n✗ Failed to cancel booking.")
        else:
            print("\nCancellation aborted.")
        
        input("Press Enter to continue...")

    def driver_login(self):
        """Driver login"""
        self.clear_screen()
        self.print_header("DRIVER LOGIN")
        
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        driver = self.data_manager.get_driver_by_username(username)
        
        if driver and driver.verify_password(password):
            self.current_user = driver
            self.user_type = "driver"
            print("\n✓ Login successful!")
            input("Press Enter to continue...")
            self.driver_menu()
        else:
            print("\n✗ Invalid username or password!")
            input("Press Enter to continue...")

    def driver_menu(self):
        """Driver menu after login"""
        while True:
            self.clear_screen()
            self.print_header(f"DRIVER MENU - Welcome {self.current_user.name}")
            self.print_menu([
                "View My Assigned Trips",
                "Logout"
            ])
            
            choice = self.get_choice(2)
            
            if choice == 1:
                self.view_driver_trips()
            elif choice == 2:
                self.current_user = None
                self.user_type = None
                break

    def view_driver_trips(self):
        """View driver's assigned trips"""
        self.clear_screen()
        self.print_header("MY ASSIGNED TRIPS")
        
        bookings = self.data_manager.get_bookings_by_driver(self.current_user.user_id)
        
        if not bookings:
            print("\nYou have no assigned trips.")
        else:
            print(f"\nTotal Trips: {len(bookings)}\n")
            for booking in bookings:
                customer = self.data_manager.get_customer_by_id(booking.customer_id)
                customer_name = customer.name if customer else "Unknown"
                
                print(f"Booking ID: {booking.booking_id}")
                print(f"Customer: {customer_name}")
                print(f"Phone: {customer.phone if customer else 'N/A'}")
                print(f"From: {booking.pickup_location} → To: {booking.dropoff_location}")
                print(f"Date & Time: {booking.booking_date} at {booking.booking_time}")
                print(f"Status: {booking.status}")
                print("-" * 60)
        
        input("\nPress Enter to continue...")

    def admin_login(self):
        """Administrator login"""
        self.clear_screen()
        self.print_header("ADMINISTRATOR LOGIN")
        
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        admin = self.data_manager.get_admin_by_username(username)
        
        if admin and admin.verify_password(password):
            self.current_user = admin
            self.user_type = "admin"
            print("\n✓ Login successful!")
            input("Press Enter to continue...")
            self.admin_menu()
        else:
            print("\n✗ Invalid username or password!")
            input("Press Enter to continue...")

    def admin_menu(self):
        """Administrator menu after login"""
        while True:
            self.clear_screen()
            self.print_header(f"ADMINISTRATOR MENU - Welcome {self.current_user.name}")
            self.print_menu([
                "View All Bookings",
                "Assign Driver to Booking",
                "View All Drivers",
                "View All Customers",
                "Logout"
            ])
            
            choice = self.get_choice(5)
            
            if choice == 1:
                self.view_all_bookings()
            elif choice == 2:
                self.assign_driver()
            elif choice == 3:
                self.view_all_drivers()
            elif choice == 4:
                self.view_all_customers()
            elif choice == 5:
                self.current_user = None
                self.user_type = None
                break

    def view_all_bookings(self):
        """View all bookings in the system"""
        self.clear_screen()
        self.print_header("ALL BOOKINGS")
        
        bookings = self.data_manager.get_all_bookings()
        
        if not bookings:
            print("\nNo bookings in the system.")
        else:
            print(f"\nTotal Bookings: {len(bookings)}\n")
            for booking in bookings:
                customer = self.data_manager.get_customer_by_id(booking.customer_id)
                customer_name = customer.name if customer else "Unknown"
                
                driver_name = "Not Assigned"
                if booking.driver_id:
                    driver = self.data_manager.get_driver_by_id(booking.driver_id)
                    if driver:
                        driver_name = driver.name
                
                print(f"Booking ID: {booking.booking_id}")
                print(f"Customer: {customer_name} (ID: {booking.customer_id})")
                print(f"From: {booking.pickup_location} → To: {booking.dropoff_location}")
                print(f"Date & Time: {booking.booking_date} at {booking.booking_time}")
                print(f"Status: {booking.status}")
                print(f"Driver: {driver_name}")
                print("-" * 60)
        
        input("\nPress Enter to continue...")

    def assign_driver(self):
        """Assign a driver to a booking"""
        self.clear_screen()
        self.print_header("ASSIGN DRIVER TO BOOKING")
        
        bookings = self.data_manager.get_all_bookings()
        pending_bookings = [b for b in bookings if b.status == "Pending"]
        
        if not pending_bookings:
            print("\nNo pending bookings to assign.")
            input("Press Enter to continue...")
            return
        
        print("\nPending Bookings:")
        for i, booking in enumerate(pending_bookings, 1):
            customer = self.data_manager.get_customer_by_id(booking.customer_id)
            customer_name = customer.name if customer else "Unknown"
            
            print(f"\n{i}. Booking ID: {booking.booking_id}")
            print(f"   Customer: {customer_name}")
            print(f"   From: {booking.pickup_location} → To: {booking.dropoff_location}")
            print(f"   Date & Time: {booking.booking_date} at {booking.booking_time}")
        
        print(f"\n{len(pending_bookings) + 1}. Go Back")
        choice = self.get_choice(len(pending_bookings) + 1)
        
        if choice == len(pending_bookings) + 1:
            return
        
        booking = pending_bookings[choice - 1]
        
        # Show available drivers
        drivers = self.data_manager.get_all_drivers()
        print("\n\nAvailable Drivers:")
        available_drivers = []
        
        for i, driver in enumerate(drivers, 1):
            is_available = self.data_manager.check_driver_availability(
                driver.user_id, booking.booking_date, booking.booking_time
            )
            status = "✓ Available" if is_available else "✗ Busy"
            print(f"{i}. {driver.name} (ID: {driver.user_id}) - {status}")
            available_drivers.append((driver, is_available))
        
        print(f"\n{len(drivers) + 1}. Go Back")
        driver_choice = self.get_choice(len(drivers) + 1)
        
        if driver_choice == len(drivers) + 1:
            return
        
        selected_driver, is_available = available_drivers[driver_choice - 1]
        
        if not is_available:
            print(f"\n⚠ Warning: {selected_driver.name} has overlapping bookings!")
            confirm = input("Do you still want to assign? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print("Assignment cancelled.")
                input("Press Enter to continue...")
                return
        
        booking.driver_id = selected_driver.user_id
        booking.status = "Assigned"
        
        if self.data_manager.update_booking(booking):
            print(f"\n✓ Driver {selected_driver.name} assigned successfully!")
        else:
            print("\n✗ Failed to assign driver.")
        
        input("Press Enter to continue...")

    def view_all_drivers(self):
        """View all drivers in the system"""
        self.clear_screen()
        self.print_header("ALL DRIVERS")
        
        drivers = self.data_manager.get_all_drivers()
        
        if not drivers:
            print("\nNo drivers in the system.")
        else:
            print(f"\nTotal Drivers: {len(drivers)}\n")
            for driver in drivers:
                trips = self.data_manager.get_bookings_by_driver(driver.user_id)
                print(f"Driver ID: {driver.user_id}")
                print(f"Name: {driver.name}")
                print(f"Phone: {driver.phone}")
                print(f"License: {driver.license_number}")
                print(f"Assigned Trips: {len(trips)}")
                print("-" * 60)
        
        input("\nPress Enter to continue...")

    def view_all_customers(self):
        """View all customers in the system"""
        self.clear_screen()
        self.print_header("ALL CUSTOMERS")
        
        customers = self.data_manager.get_all_customers()
        
        if not customers:
            print("\nNo customers in the system.")
        else:
            print(f"\nTotal Customers: {len(customers)}\n")
            for customer in customers:
                bookings = self.data_manager.get_bookings_by_customer(customer.user_id)
                print(f"Customer ID: {customer.user_id}")
                print(f"Name: {customer.name}")
                print(f"Phone: {customer.phone}")
                print(f"Email: {customer.email}")
                print(f"Total Bookings: {len(bookings)}")
                print("-" * 60)
        
        input("\nPress Enter to continue...")

    def run(self):
        """Run the taxi booking system"""
        try:
            self.main_menu()
        except KeyboardInterrupt:
            print("\n\nSystem interrupted. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\n\nAn error occurred: {e}")
            input("Press Enter to exit...")
            sys.exit(1)


def main():
    """Main entry point"""
    system = TaxiBookingSystem()
    system.run()


if __name__ == "__main__":
    main()

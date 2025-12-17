"""
Demonstration Script for Taxi Booking System
Shows how to use the system with sample data
"""

import os
import sys

# Add the taxi_booking_system directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import Customer, Driver, Booking
from data_manager import DataManager


def setup_demo_data():
    """Create demo data for demonstration"""
    print("\n" + "="*70)
    print("  TAXI BOOKING SYSTEM - DEMO DATA SETUP")
    print("="*70)
    
    # Use the actual data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "data")
    dm = DataManager(data_dir)
    
    print("\n📝 Creating sample customers...")
    
    # Create sample customers
    customers = [
        Customer("C001", "alice", "pass123", "Alice Johnson", 
                "123 Oak Street", "555-1001", "alice@email.com"),
        Customer("C002", "bob", "pass123", "Bob Smith",
                "456 Maple Avenue", "555-1002", "bob@email.com"),
        Customer("C003", "charlie", "pass123", "Charlie Brown",
                "789 Pine Road", "555-1003", "charlie@email.com"),
    ]
    
    for customer in customers:
        existing = dm.get_customer_by_username(customer.username)
        if not existing:
            dm.save_customer(customer)
            print(f"  ✓ Created customer: {customer.name} (username: {customer.username})")
        else:
            print(f"  ℹ Customer already exists: {customer.name}")
    
    print("\n📝 Creating sample bookings...")
    
    # Create sample bookings
    bookings = [
        Booking("B001", "C001", "Downtown", "Airport", "2024-12-25", "08:00", "Pending", ""),
        Booking("B002", "C001", "Airport", "Hotel Plaza", "2024-12-25", "18:00", "Assigned", "D001"),
        Booking("B003", "C002", "Home", "Office Park", "2024-12-26", "09:00", "Pending", ""),
        Booking("B004", "C002", "Shopping Mall", "Restaurant", "2024-12-26", "14:00", "Assigned", "D002"),
        Booking("B005", "C003", "Train Station", "University", "2024-12-27", "10:00", "Cancelled", ""),
    ]
    
    for booking in bookings:
        existing = dm.get_booking_by_id(booking.booking_id)
        if not existing:
            dm.save_booking(booking)
            customer = dm.get_customer_by_id(booking.customer_id)
            customer_name = customer.name if customer else "Unknown"
            print(f"  ✓ Created booking: {booking.booking_id} for {customer_name} ({booking.status})")
        else:
            print(f"  ℹ Booking already exists: {booking.booking_id}")
    
    print("\n✅ Demo data setup complete!")
    print("\n" + "="*70)
    print("  SYSTEM INFORMATION")
    print("="*70)
    
    print("\n📊 Statistics:")
    print(f"  • Total Customers: {len(dm.get_all_customers())}")
    print(f"  • Total Drivers: {len(dm.get_all_drivers())}")
    print(f"  • Total Administrators: {len(dm.get_all_admins())}")
    print(f"  • Total Bookings: {len(dm.get_all_bookings())}")
    
    print("\n🔑 Login Credentials:")
    print("\n  ADMINISTRATOR:")
    print("    Username: admin")
    print("    Password: admin123")
    
    print("\n  DRIVERS:")
    drivers = dm.get_all_drivers()
    for driver in drivers[:3]:
        print(f"    Username: {driver.username}, Password: pass123 ({driver.name})")
    
    print("\n  CUSTOMERS:")
    for customer in customers:
        print(f"    Username: {customer.username}, Password: pass123 ({customer.name})")
    
    print("\n" + "="*70)
    print("  USAGE GUIDE")
    print("="*70)
    
    print("""
📖 How to use the system:

1. CUSTOMER WORKFLOW:
   • Select "Customer Login" or "Customer Registration"
   • Login with username and password
   • Choose "Book a Taxi" to create a new booking
   • View your bookings to see status
   • Update or cancel bookings as needed

2. DRIVER WORKFLOW:
   • Select "Driver Login"
   • Login with driver credentials
   • View assigned trips with customer details

3. ADMINISTRATOR WORKFLOW:
   • Select "Administrator Login"
   • View all bookings in the system
   • Assign drivers to pending bookings
   • System checks for scheduling conflicts
   • View all customers and drivers

📝 BOOKING STATES:
   • Pending: Waiting for driver assignment
   • Assigned: Driver has been assigned
   • Completed: Trip finished
   • Cancelled: Booking cancelled by customer

⚠️  IMPORTANT NOTES:
   • Only pending bookings can be updated or assigned
   • System prevents driver double-booking (2-hour window)
   • All data is persisted in text files
   • Default admin: admin/admin123
   • Sample driver: driver1/pass123
   • Sample customer: alice/pass123
""")
    
    print("="*70)
    print("  Ready to run! Execute: python main.py")
    print("="*70)


if __name__ == "__main__":
    setup_demo_data()

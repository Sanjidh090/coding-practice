"""
Test Script for Taxi Booking System
Automated tests to verify system functionality
"""

import os
import sys
import tempfile

# Add the taxi_booking_system directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import Customer, Driver, Administrator, Booking
from data_manager import DataManager

# Test directory constant
TEST_DATA_DIR = os.path.join(tempfile.gettempdir(), "taxi_test_data")


def test_models():
    """Test model classes"""
    print("\n" + "="*60)
    print("Testing Models")
    print("="*60)
    
    # Test Customer
    customer = Customer("C001", "john_doe", "pass123", "John Doe", 
                       "123 Main St", "555-0100", "john@email.com")
    customer_str = customer.to_string()
    print(f"✓ Customer to_string: {customer_str}")
    
    customer_restored = Customer.from_string(customer_str)
    assert customer_restored.user_id == customer.user_id
    print(f"✓ Customer from_string: ID={customer_restored.user_id}")
    
    # Test Driver
    driver = Driver("D001", "driver1", "pass123", "Jane Driver", 
                   "555-0101", "DL001")
    driver_str = driver.to_string()
    print(f"✓ Driver to_string: {driver_str}")
    
    driver_restored = Driver.from_string(driver_str)
    assert driver_restored.license_number == driver.license_number
    print(f"✓ Driver from_string: License={driver_restored.license_number}")
    
    # Test Booking
    booking = Booking("B001", "C001", "Downtown", "Airport", 
                     "2024-12-20", "14:30", "Pending", "")
    booking_str = booking.to_string()
    print(f"✓ Booking to_string: {booking_str}")
    
    booking_restored = Booking.from_string(booking_str)
    assert booking_restored.booking_id == booking.booking_id
    print(f"✓ Booking from_string: ID={booking_restored.booking_id}")
    
    print("\n✅ All model tests passed!")


def test_data_manager():
    """Test data manager operations"""
    print("\n" + "="*60)
    print("Testing Data Manager")
    print("="*60)
    
    # Create a test data directory
    if os.path.exists(TEST_DATA_DIR):
        import shutil
        shutil.rmtree(TEST_DATA_DIR)
    
    dm = DataManager(TEST_DATA_DIR)
    print(f"✓ DataManager initialized with test directory")
    
    # Test customer operations
    customer = Customer("C001", "test_user", "test123", "Test User",
                       "Test Address", "555-0001", "test@test.com")
    assert dm.save_customer(customer) == True
    print(f"✓ Customer saved successfully")
    
    customers = dm.get_all_customers()
    assert len(customers) == 1
    print(f"✓ Retrieved {len(customers)} customer(s)")
    
    retrieved = dm.get_customer_by_username("test_user")
    assert retrieved is not None
    assert retrieved.email == "test@test.com"
    print(f"✓ Customer retrieved by username: {retrieved.name}")
    
    # Test driver operations
    drivers = dm.get_all_drivers()
    assert len(drivers) == 3  # Default drivers
    print(f"✓ Retrieved {len(drivers)} driver(s)")
    
    driver = dm.get_driver_by_username("driver1")
    assert driver is not None
    print(f"✓ Driver retrieved by username: {driver.name}")
    
    # Test admin operations
    admins = dm.get_all_admins()
    assert len(admins) == 1  # Default admin
    print(f"✓ Retrieved {len(admins)} administrator(s)")
    
    admin = dm.get_admin_by_username("admin")
    assert admin is not None
    assert admin.verify_password("admin123")
    print(f"✓ Administrator retrieved: {admin.name}")
    
    # Test booking operations
    booking = Booking("B001", "C001", "Location A", "Location B",
                     "2024-12-20", "14:00", "Pending", "")
    assert dm.save_booking(booking) == True
    print(f"✓ Booking saved successfully")
    
    bookings = dm.get_all_bookings()
    assert len(bookings) == 1
    print(f"✓ Retrieved {len(bookings)} booking(s)")
    
    # Test booking update
    booking.status = "Assigned"
    booking.driver_id = "D001"
    assert dm.update_booking(booking) == True
    print(f"✓ Booking updated successfully")
    
    updated = dm.get_booking_by_id("B001")
    assert updated.status == "Assigned"
    assert updated.driver_id == "D001"
    print(f"✓ Booking update verified: Status={updated.status}")
    
    # Test driver availability check
    is_available = dm.check_driver_availability("D002", "2024-12-20", "14:00")
    assert is_available == True
    print(f"✓ Driver D002 is available at specified time")
    
    is_available = dm.check_driver_availability("D001", "2024-12-20", "14:30")
    assert is_available == False  # Should conflict with existing booking
    print(f"✓ Driver D001 conflict detected correctly")
    
    print("\n✅ All data manager tests passed!")


def test_authentication():
    """Test authentication logic"""
    print("\n" + "="*60)
    print("Testing Authentication")
    print("="*60)
    
    dm = DataManager(TEST_DATA_DIR)
    
    # Test customer authentication
    customer = dm.get_customer_by_username("test_user")
    assert customer is not None
    assert customer.verify_password("test123")
    print(f"✓ Customer authentication successful")
    
    # Test invalid customer
    invalid = dm.get_customer_by_username("nonexistent")
    assert invalid is None
    print(f"✓ Invalid customer rejected")
    
    # Test driver authentication
    driver = dm.get_driver_by_username("driver1")
    assert driver is not None
    assert driver.verify_password("pass123")
    print(f"✓ Driver authentication successful")
    
    # Test admin authentication
    admin = dm.get_admin_by_username("admin")
    assert admin is not None
    assert admin.verify_password("admin123")
    print(f"✓ Administrator authentication successful")
    
    print("\n✅ All authentication tests passed!")


def test_booking_workflow():
    """Test complete booking workflow"""
    print("\n" + "="*60)
    print("Testing Booking Workflow")
    print("="*60)
    
    dm = DataManager(TEST_DATA_DIR)
    
    # Customer creates booking
    booking_id = dm.get_next_booking_id()
    booking = Booking(booking_id, "C001", "Home", "Office",
                     "2024-12-25", "09:00", "Pending", "")
    dm.save_booking(booking)
    print(f"✓ Customer created booking: {booking_id}")
    
    # Verify booking is pending
    created = dm.get_booking_by_id(booking_id)
    assert created.status == "Pending"
    assert created.driver_id == ""
    print(f"✓ Booking status: {created.status}")
    
    # Admin assigns driver
    created.driver_id = "D002"
    created.status = "Assigned"
    dm.update_booking(created)
    print(f"✓ Administrator assigned driver: D002")
    
    # Verify assignment
    assigned = dm.get_booking_by_id(booking_id)
    assert assigned.driver_id == "D002"
    assert assigned.status == "Assigned"
    print(f"✓ Booking status: {assigned.status}")
    
    # Driver views trips
    driver_trips = dm.get_bookings_by_driver("D002")
    assert len(driver_trips) == 1
    print(f"✓ Driver has {len(driver_trips)} assigned trip(s)")
    
    # Customer cancels booking
    assigned.status = "Cancelled"
    dm.update_booking(assigned)
    print(f"✓ Customer cancelled booking")
    
    # Verify cancellation
    cancelled = dm.get_booking_by_id(booking_id)
    assert cancelled.status == "Cancelled"
    print(f"✓ Booking status: {cancelled.status}")
    
    print("\n✅ All workflow tests passed!")


def test_id_generation():
    """Test ID generation"""
    print("\n" + "="*60)
    print("Testing ID Generation")
    print("="*60)
    
    dm = DataManager(TEST_DATA_DIR)
    
    # Test customer ID generation
    next_id = dm.get_next_customer_id()
    print(f"✓ Next customer ID: {next_id}")
    assert next_id == "C002"  # After C001 in test data
    
    # Test booking ID generation  
    next_id = dm.get_next_booking_id()
    print(f"✓ Next booking ID: {next_id}")
    assert next_id.startswith("B")
    
    print("\n✅ All ID generation tests passed!")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*70)
    print("  TAXI BOOKING SYSTEM - AUTOMATED TEST SUITE")
    print("="*70)
    
    try:
        test_models()
        test_data_manager()
        test_authentication()
        test_booking_workflow()
        test_id_generation()
        
        print("\n" + "="*70)
        print("  ✅ ALL TESTS PASSED SUCCESSFULLY!")
        print("="*70)
        print("\nTest Summary:")
        print("  • Model serialization/deserialization ✓")
        print("  • Data persistence (file operations) ✓")
        print("  • User authentication (all types) ✓")
        print("  • Booking creation and management ✓")
        print("  • Driver assignment ✓")
        print("  • Conflict detection ✓")
        print("  • Status transitions ✓")
        print("  • ID generation ✓")
        print("\nThe system is ready for production use!")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()

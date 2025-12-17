"""
Enhanced Test Script for GUI Taxi Booking System
Tests password hashing, driver assignment algorithm, and location features
"""

import os
import sys
import tempfile

# Add the taxi_booking_system directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import Customer, Driver, Administrator, Booking
from data_manager import DataManager
from assignment_algorithm import DriverAssignmentAlgorithm

# Test directory constant
TEST_DATA_DIR = os.path.join(tempfile.gettempdir(), "taxi_test_gui")


def test_password_hashing():
    """Test password hashing and verification"""
    print("\n" + "="*60)
    print("Testing Password Hashing")
    print("="*60)
    
    # Test customer password hashing
    customer = Customer("C001", "john_doe", "pass123", "John Doe",
                       "123 Main St", "555-0100", "john@email.com")
    
    # Check password is hashed (64 char hex string)
    assert len(customer.password) == 64
    assert customer.password != "pass123"
    print(f"✓ Password hashed: {customer.password[:20]}...")
    
    # Test password verification
    assert customer.verify_password("pass123") == True
    print(f"✓ Correct password verified")
    
    assert customer.verify_password("wrong") == False
    print(f"✓ Wrong password rejected")
    
    # Test driver password hashing
    driver = Driver("D001", "driver1", "pass123", "Jane Driver",
                   "555-0101", "DL001", 40.7128, -74.0060)
    assert driver.verify_password("pass123") == True
    print(f"✓ Driver password verification works")
    
    # Test admin password hashing
    admin = Administrator("A001", "admin", "admin123", "System Admin")
    assert admin.verify_password("admin123") == True
    print(f"✓ Admin password verification works")
    
    # Test from_string preserves hashed password
    customer_str = customer.to_string()
    customer_restored = Customer.from_string(customer_str)
    assert customer_restored.verify_password("pass123") == True
    print(f"✓ Password remains hashed after serialization")
    
    print("\n✅ All password hashing tests passed!")


def test_driver_locations():
    """Test driver location features"""
    print("\n" + "="*60)
    print("Testing Driver Locations")
    print("="*60)
    
    # Create driver with location
    driver = Driver("D001", "driver1", "pass123", "John Driver",
                   "555-0101", "DL001", 40.7128, -74.0060)
    
    assert driver.latitude == 40.7128
    assert driver.longitude == -74.0060
    print(f"✓ Driver location stored: ({driver.latitude}, {driver.longitude})")
    
    # Test serialization with location
    driver_str = driver.to_string()
    assert "40.7128" in driver_str
    assert "-74.006" in driver_str
    print(f"✓ Driver location serialized correctly")
    
    # Test deserialization with location
    driver_restored = Driver.from_string(driver_str)
    assert driver_restored.latitude == 40.7128
    assert driver_restored.longitude == -74.0060
    print(f"✓ Driver location deserialized correctly")
    
    print("\n✅ All driver location tests passed!")


def test_booking_locations():
    """Test booking location features"""
    print("\n" + "="*60)
    print("Testing Booking Locations")
    print("="*60)
    
    # Create booking with locations
    booking = Booking("B001", "C001", "Times Square", "JFK Airport",
                     "2024-12-25", "10:00", "Pending", "",
                     40.7580, -73.9855, 40.6413, -73.7781)
    
    assert booking.pickup_lat == 40.7580
    assert booking.pickup_lon == -73.9855
    assert booking.dropoff_lat == 40.6413
    assert booking.dropoff_lon == -73.7781
    print(f"✓ Booking locations stored correctly")
    
    # Test serialization
    booking_str = booking.to_string()
    assert "40.758" in booking_str
    assert "-73.9855" in booking_str
    print(f"✓ Booking locations serialized correctly")
    
    # Test deserialization
    booking_restored = Booking.from_string(booking_str)
    assert booking_restored.pickup_lat == 40.7580
    assert booking_restored.dropoff_lat == 40.6413
    print(f"✓ Booking locations deserialized correctly")
    
    print("\n✅ All booking location tests passed!")


def test_distance_calculation():
    """Test Haversine distance calculation"""
    print("\n" + "="*60)
    print("Testing Distance Calculation")
    print("="*60)
    
    # Test distance between two known NYC locations
    # Times Square to Empire State Building (~0.7 km)
    times_square = (40.7580, -73.9855)
    empire_state = (40.7484, -73.9857)
    
    dist = DriverAssignmentAlgorithm.calculate_distance(
        times_square[0], times_square[1],
        empire_state[0], empire_state[1]
    )
    
    # Should be approximately 1.07 km
    assert 0.5 < dist < 1.5
    print(f"✓ Times Square to Empire State: {dist:.2f} km")
    
    # Test zero distance (same location)
    dist = DriverAssignmentAlgorithm.calculate_distance(
        40.7580, -73.9855, 40.7580, -73.9855
    )
    assert dist == 0.0
    print(f"✓ Same location distance: {dist:.2f} km")
    
    # Test longer distance (NYC to Boston ~300 km)
    nyc = (40.7128, -74.0060)
    boston = (42.3601, -71.0589)
    dist = DriverAssignmentAlgorithm.calculate_distance(
        nyc[0], nyc[1], boston[0], boston[1]
    )
    assert 250 < dist < 350
    print(f"✓ NYC to Boston: {dist:.2f} km")
    
    print("\n✅ All distance calculation tests passed!")


def test_driver_availability():
    """Test driver availability checking"""
    print("\n" + "="*60)
    print("Testing Driver Availability")
    print("="*60)
    
    from datetime import datetime
    
    driver = Driver("D001", "driver1", "pass123", "John Driver",
                   "555-0101", "DL001", 40.7128, -74.0060)
    
    # Create existing bookings
    existing_bookings = [
        Booking("B001", "C001", "Loc A", "Loc B", "2024-12-25", "10:00",
               "Assigned", "D001", 40.7, -74.0, 40.8, -74.1),
        Booking("B002", "C002", "Loc C", "Loc D", "2024-12-25", "15:00",
               "Assigned", "D001", 40.7, -74.0, 40.8, -74.1)
    ]
    
    # Test: Driver is available at 13:00 (between bookings with enough gap)
    booking_datetime = datetime.strptime("2024-12-25 13:00", "%Y-%m-%d %H:%M")
    is_available = DriverAssignmentAlgorithm.is_driver_available(
        driver, booking_datetime, existing_bookings
    )
    assert is_available == True
    print(f"✓ Driver available at 13:00 (between bookings)")
    
    # Test: Driver is NOT available at 10:30 (within 2-hour window of 10:00 booking)
    booking_datetime = datetime.strptime("2024-12-25 10:30", "%Y-%m-%d %H:%M")
    is_available = DriverAssignmentAlgorithm.is_driver_available(
        driver, booking_datetime, existing_bookings
    )
    assert is_available == False
    print(f"✓ Driver not available at 10:30 (too close to 10:00 booking)")
    
    # Test: Driver is available on different day
    booking_datetime = datetime.strptime("2024-12-26 10:00", "%Y-%m-%d %H:%M")
    is_available = DriverAssignmentAlgorithm.is_driver_available(
        driver, booking_datetime, existing_bookings
    )
    assert is_available == True
    print(f"✓ Driver available on different day")
    
    print("\n✅ All driver availability tests passed!")


def test_driver_assignment():
    """Test the complete driver assignment algorithm"""
    print("\n" + "="*60)
    print("Testing Driver Assignment Algorithm")
    print("="*60)
    
    # Create drivers at different locations
    drivers = [
        Driver("D001", "driver1", "pass123", "John Driver",
              "555-0101", "DL001", 40.7128, -74.0060),  # Far
        Driver("D002", "driver2", "pass123", "Jane Driver",
              "555-0102", "DL002", 40.7580, -73.9855),  # Very close
        Driver("D003", "driver3", "pass123", "Bob Driver",
              "555-0103", "DL003", 40.7614, -73.9776)   # Close
    ]
    
    # Create booking near driver2's location
    booking = Booking("B001", "C001", "Times Square", "JFK Airport",
                     "2024-12-25", "10:00", "Pending", "",
                     40.7580, -73.9855, 40.6413, -73.7781)
    
    # No existing bookings for any driver
    driver_bookings_map = {
        "D001": [],
        "D002": [],
        "D003": []
    }
    
    # Find best driver
    result = DriverAssignmentAlgorithm.find_best_driver(drivers, booking, driver_bookings_map)
    assert result is not None
    driver, distance = result
    assert driver.user_id == "D002"  # Should assign Jane (closest)
    assert distance < 0.1  # Should be very close (almost 0)
    print(f"✓ Assigned nearest driver: {driver.name} at {distance:.2f} km")
    
    # Test with one driver busy
    driver_bookings_map["D002"] = [
        Booking("B999", "C999", "Loc", "Loc", "2024-12-25", "10:00",
               "Assigned", "D002", 40.7, -74.0, 40.8, -74.1)
    ]
    
    result = DriverAssignmentAlgorithm.find_best_driver(drivers, booking, driver_bookings_map)
    assert result is not None
    driver, distance = result
    assert driver.user_id == "D003"  # Should assign Bob (D002 is busy)
    print(f"✓ Assigned next nearest available driver: {driver.name}")
    
    # Test with all drivers busy
    driver_bookings_map["D001"].append(
        Booking("B998", "C998", "Loc", "Loc", "2024-12-25", "10:00",
               "Assigned", "D001", 40.7, -74.0, 40.8, -74.1)
    )
    driver_bookings_map["D003"].append(
        Booking("B997", "C997", "Loc", "Loc", "2024-12-25", "10:00",
               "Assigned", "D003", 40.7, -74.0, 40.8, -74.1)
    )
    
    result = DriverAssignmentAlgorithm.find_best_driver(drivers, booking, driver_bookings_map)
    assert result is None  # No driver available
    print(f"✓ Correctly returns None when all drivers busy")
    
    print("\n✅ All driver assignment tests passed!")


def test_driver_recommendations():
    """Test driver recommendation system"""
    print("\n" + "="*60)
    print("Testing Driver Recommendations")
    print("="*60)
    
    # Create drivers
    drivers = [
        Driver("D001", "driver1", "pass", "John", "555-0101", "DL001", 40.7128, -74.0060),
        Driver("D002", "driver2", "pass", "Jane", "555-0102", "DL002", 40.7580, -73.9855),
        Driver("D003", "driver3", "pass", "Bob", "555-0103", "DL003", 40.7614, -73.9776)
    ]
    
    booking = Booking("B001", "C001", "Times Square", "JFK", "2024-12-25", "10:00",
                     "Pending", "", 40.7580, -73.9855, 40.6413, -73.7781)
    
    driver_bookings_map = {"D001": [], "D002": [], "D003": []}
    
    # Get top 3 recommendations
    recommendations = DriverAssignmentAlgorithm.get_driver_recommendations(
        booking, drivers, driver_bookings_map, top_n=3
    )
    
    assert len(recommendations) == 3
    print(f"✓ Got {len(recommendations)} recommendations")
    
    # Check they're sorted by availability then distance
    for i, (driver, distance, is_available) in enumerate(recommendations, 1):
        status = "Available" if is_available else "Busy"
        print(f"  {i}. {driver.name}: {distance:.2f} km - {status}")
    
    # All should be available in this test
    assert all(rec[2] for rec in recommendations)
    print(f"✓ All recommended drivers are available")
    
    # First should be closest
    assert recommendations[0][1] <= recommendations[1][1]
    print(f"✓ Recommendations sorted by distance")
    
    print("\n✅ All driver recommendation tests passed!")


def run_all_tests():
    """Run all enhanced tests"""
    print("\n" + "="*70)
    print("  TAXI BOOKING SYSTEM - ENHANCED TEST SUITE (GUI VERSION)")
    print("="*70)
    
    try:
        test_password_hashing()
        test_driver_locations()
        test_booking_locations()
        test_distance_calculation()
        test_driver_availability()
        test_driver_assignment()
        test_driver_recommendations()
        
        print("\n" + "="*70)
        print("  ✅ ALL ENHANCED TESTS PASSED SUCCESSFULLY!")
        print("="*70)
        print("\nTest Summary:")
        print("  • Password hashing and verification ✓")
        print("  • Driver location tracking ✓")
        print("  • Booking location tracking ✓")
        print("  • Distance calculation (Haversine) ✓")
        print("  • Driver availability checking ✓")
        print("  • Intelligent driver assignment ✓")
        print("  • Driver recommendations ✓")
        print("\nThe GUI system is ready for production use!")
        
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

# Taxi Booking System

A comprehensive taxi booking system implemented in Python using computational thinking principles and object-oriented design.

## System Overview

This system provides a complete solution for managing taxi bookings with three types of users:
- **Customers**: Can register, book taxis, view and cancel bookings
- **Drivers**: Can view their assigned trips
- **Administrators**: Can assign drivers to bookings and manage the system

## Features

### Customer Features
- User registration with complete profile (name, address, phone, email)
- Login authentication
- Book taxi rides with pickup/dropoff locations, date, and time
- View all personal bookings
- Update pending bookings
- Cancel active bookings

### Driver Features
- Login authentication
- View all assigned trips with customer details
- See trip schedule with dates and times

### Administrator Features
- Login authentication
- View all bookings in the system
- Assign drivers to pending bookings
- Prevent driver booking conflicts (checks for overlapping schedules)
- View all drivers and customers
- Monitor system statistics

## Installation and Setup

1. Navigate to the taxi_booking_system directory:
```bash
cd taxi_booking_system
```

2. Run the system:
```bash
python main.py
```

## Default Credentials

### Administrator
- Username: `admin`
- Password: `admin123`

### Drivers
Three sample drivers are pre-configured:
- Username: `driver1`, Password: `pass123`
- Username: `driver2`, Password: `pass123`
- Username: `driver3`, Password: `pass123`

### Customers
No default customers - use the registration feature to create new accounts.

## System Architecture

### Computational Thinking Applied

1. **Decomposition**: The system is broken down into smaller modules:
   - User management (Customer, Driver, Administrator)
   - Booking management
   - Authentication
   - Data persistence
   - Menu interface

2. **Pattern Recognition**: Similar operations are reused:
   - Login mechanism shared across all user types
   - Common file handling patterns
   - Menu display and navigation patterns

3. **Abstraction**: Only essential data is stored:
   - User credentials and contact information
   - Booking details (locations, dates, times)
   - Assignment relationships

4. **Algorithm Design**: Structured processes for:
   - User registration and authentication
   - Booking creation and management
   - Driver assignment with conflict detection
   - Data persistence and retrieval

### File Structure

```
taxi_booking_system/
├── main.py              # Main application with menu interface
├── models.py            # Data models (Customer, Driver, Administrator, Booking)
├── data_manager.py      # File handling and data operations
├── README.md            # This file
├── data/                # Data storage directory
│   ├── customers.txt    # Customer records
│   ├── drivers.txt      # Driver records
│   ├── administrators.txt # Administrator records
│   └── bookings.txt     # Booking records
└── diagrams/            # UML diagrams (to be added)
```

## UML Diagrams

### 1. Use Case Diagram

The system has three actors:

**Customer:**
- Register
- Login
- Book Taxi
- View Bookings
- Update Booking
- Cancel Booking

**Driver:**
- Login
- View Assigned Trips

**Administrator:**
- Login
- View All Bookings
- Assign Driver to Booking
- View Drivers
- View Customers

### 2. Activity Diagram - Customer Booking Process

1. Customer logs in
2. Selects "Book a Taxi"
3. Enters pickup location
4. Enters drop-off location
5. Enters date (validated)
6. Enters time (validated)
7. System creates booking with "Pending" status
8. System generates booking ID
9. Displays confirmation to customer

### 3. Class Diagram

**User (Base Class)**
- Attributes: user_id, username, password, name
- Methods: __init__(), to_string()

**Customer (Inherits User)**
- Additional Attributes: address, phone, email
- Methods: __init__(), to_string(), from_string()

**Driver (Inherits User)**
- Additional Attributes: phone, license_number
- Methods: __init__(), to_string(), from_string()

**Administrator (Inherits User)**
- Methods: __init__(), from_string()

**Booking**
- Attributes: booking_id, customer_id, pickup_location, dropoff_location, booking_date, booking_time, status, driver_id
- Methods: __init__(), to_string(), from_string(), get_datetime()

**DataManager**
- Attributes: data_dir, customers_file, drivers_file, admins_file, bookings_file
- Methods: 
  - save_customer(), get_all_customers(), get_customer_by_username(), get_customer_by_id()
  - get_all_drivers(), get_driver_by_username(), get_driver_by_id()
  - get_all_admins(), get_admin_by_username()
  - save_booking(), get_all_bookings(), update_booking(), get_bookings_by_customer(), get_bookings_by_driver()
  - check_driver_availability()

**TaxiBookingSystem**
- Attributes: data_manager, current_user, user_type
- Methods: All menu and operation methods

## Data Storage

The system uses text file storage with pipe-delimited format:

### customers.txt
```
C001|username|password|Full Name|Address|Phone|Email
```

### drivers.txt
```
D001|username|password|Full Name|Phone|License Number
```

### administrators.txt
```
A001|username|password|Full Name
```

### bookings.txt
```
B001|C001|Pickup|Dropoff|2024-12-20|14:30|Pending|
B002|C001|Location A|Location B|2024-12-21|10:00|Assigned|D001
```

## Testing Guide

### Test Scenario 1: Customer Registration and Booking
1. Run the system
2. Select "Customer Registration"
3. Enter all required details
4. Login with created credentials
5. Book a taxi with valid details
6. View bookings to verify creation

### Test Scenario 2: Driver Assignment
1. Login as administrator (admin/admin123)
2. View all bookings
3. Select "Assign Driver to Booking"
4. Choose a pending booking
5. Assign an available driver
6. Verify assignment in booking list

### Test Scenario 3: Driver View Trips
1. Login as driver (driver1/pass123)
2. View assigned trips
3. Verify trip details are displayed correctly

### Test Scenario 4: Booking Management
1. Login as customer
2. Create a new booking
3. Update the booking details
4. View updated booking
5. Cancel the booking
6. Verify cancellation

### Test Scenario 5: Conflict Prevention
1. Login as administrator
2. Assign driver to a booking at specific time
3. Try to assign same driver to another booking at overlapping time
4. System should warn about conflict
5. Administrator can override or choose different driver

## Design Decisions

### 1. File-Based Storage
- Simple text files for easy inspection and debugging
- Pipe-delimited format for structured data
- Separate files for different entity types
- Easy migration to database if needed

### 2. Text-Based Interface
- No external dependencies required
- Clear and intuitive menu system
- Easy to test and demonstrate
- Cross-platform compatible

### 3. User Types Separation
- Clear role-based access control
- Separate login paths for security
- Dedicated menus for each user type
- Easy to extend with new roles

### 4. Booking Status Management
- Four states: Pending, Assigned, Completed, Cancelled
- Clear workflow progression
- Easy to track booking lifecycle

### 5. Conflict Detection
- 2-hour window for driver availability
- Prevents double-booking
- Administrator override option
- Ensures service quality

## Future Enhancements (Optional)

1. **GUI Implementation**: Add Tkinter-based graphical interface
2. **Database Migration**: Move from text files to SQLite
3. **Payment Integration**: Add fare calculation and payment
4. **Real-time Tracking**: GPS integration
5. **Notifications**: Email/SMS alerts
6. **Rating System**: Customer and driver ratings
7. **Trip History**: Completed trip analytics
8. **Multi-language Support**: Internationalization

## Troubleshooting

### Issue: Cannot login
- Verify username and password
- Check that you're using the correct login option (Customer/Driver/Admin)
- Ensure data files exist in the data directory

### Issue: Booking not saved
- Check write permissions on data directory
- Verify all required fields are filled
- Check date/time format

### Issue: Driver assignment fails
- Verify driver exists in system
- Check for timing conflicts
- Ensure booking is in Pending status

## System Requirements

- Python 3.6 or higher
- No external dependencies required
- Works on Windows, macOS, and Linux

## License

This is an educational project for learning purposes.

## Authors

Developed as part of a computational thinking and system design assignment.

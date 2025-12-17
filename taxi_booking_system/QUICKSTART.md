# Quick Start Guide - Taxi Booking System

## Get Started in 3 Steps

### Step 1: Navigate to the Project Directory
```bash
cd taxi_booking_system
```

### Step 2: Set Up Demo Data (Optional but Recommended)
```bash
python setup_demo.py
```

This creates sample customers, drivers, and bookings for testing.

### Step 3: Run the System
```bash
python main.py
```

---

## Quick Test Scenarios

### Scenario 1: Try as a Customer (5 minutes)

1. **Start the system**: `python main.py`
2. **Select**: `2. Customer Registration`
3. **Enter your details**:
   ```
   Username: yourname
   Password: your123
   Full Name: Your Name
   Address: Your Address
   Phone: 555-1234
   Email: you@email.com
   ```
4. **Login**: Select `1. Customer Login`
   - Username: `yourname`
   - Password: `your123`
5. **Book a Taxi**: Select `1. Book a Taxi`
   ```
   Pickup: Home
   Dropoff: Office
   Date: 2024-12-30
   Time: 09:00
   ```
6. **View Bookings**: Select `2. View My Bookings`
7. **Logout**: Select `5. Logout`

### Scenario 2: Try as Administrator (3 minutes)

1. **Start the system**: `python main.py`
2. **Select**: `4. Administrator Login`
3. **Login**:
   - Username: `admin`
   - Password: `admin123`
4. **View All Bookings**: Select `1. View All Bookings`
5. **Assign Driver**: Select `2. Assign Driver to Booking`
   - Choose a pending booking
   - Select an available driver
   - Confirm assignment
6. **Logout**: Select `5. Logout`

### Scenario 3: Try as Driver (2 minutes)

1. **Start the system**: `python main.py`
2. **Select**: `3. Driver Login`
3. **Login**:
   - Username: `driver1`
   - Password: `pass123`
4. **View Trips**: Select `1. View My Assigned Trips`
5. **Logout**: Select `2. Logout`

---

## Pre-configured Accounts

### Administrator
- **Username**: admin
- **Password**: admin123

### Drivers
- **driver1** / pass123 (John Driver)
- **driver2** / pass123 (Jane Driver)
- **driver3** / pass123 (Bob Driver)

### Sample Customers (after running setup_demo.py)
- **alice** / pass123 (Alice Johnson)
- **bob** / pass123 (Bob Smith)
- **charlie** / pass123 (Charlie Brown)

---

## System Features Checklist

### ✅ Customer Features
- [x] Registration with full profile
- [x] Login authentication
- [x] Book taxi with date/time
- [x] View all bookings
- [x] Update pending bookings
- [x] Cancel active bookings

### ✅ Driver Features
- [x] Login authentication
- [x] View assigned trips
- [x] See customer details

### ✅ Administrator Features
- [x] Login authentication
- [x] View all bookings
- [x] Assign drivers to bookings
- [x] Check driver availability
- [x] Prevent booking conflicts
- [x] View all customers and drivers

---

## Common Operations

### How to Register a New Customer
1. Main Menu → `2. Customer Registration`
2. Fill in all required fields
3. Remember your username and password
4. Login with your credentials

### How to Book a Taxi
1. Login as customer
2. Customer Menu → `1. Book a Taxi`
3. Enter pickup and dropoff locations
4. Enter date (format: YYYY-MM-DD)
5. Enter time (format: HH:MM)
6. Note your booking ID

### How to Assign a Driver (Admin)
1. Login as administrator
2. Admin Menu → `2. Assign Driver to Booking`
3. Select a pending booking
4. Review driver availability
5. Select an available driver
6. Confirm assignment

### How to Update a Booking
1. Login as customer
2. Customer Menu → `3. Update Booking`
3. Select the booking to update
4. Enter new details (or press Enter to keep current)
5. Confirm changes

### How to Cancel a Booking
1. Login as customer
2. Customer Menu → `4. Cancel Booking`
3. Select the booking to cancel
4. Type `yes` to confirm

---

## Troubleshooting

### Problem: "Invalid username or password"
- **Solution**: Check you're using the correct login option (Customer/Driver/Admin)
- Verify you typed the password correctly
- For demo accounts, use credentials listed above

### Problem: "All fields are required"
- **Solution**: Make sure you enter something for every field during registration or booking

### Problem: Date/Time format error
- **Solution**: Use exact format requested
  - Date: YYYY-MM-DD (e.g., 2024-12-25)
  - Time: HH:MM (e.g., 14:30)

### Problem: Cannot update booking
- **Solution**: Only "Pending" bookings can be updated
- Check booking status in "View Bookings"

### Problem: Driver shows as "Busy"
- **Solution**: Driver has another booking within 2 hours
- Choose a different driver or override the warning (Admin only)

---

## File Locations

```
taxi_booking_system/
├── main.py              ← Run this to start
├── setup_demo.py        ← Run this for demo data
├── test_system.py       ← Run this to test
├── data/                ← Your data is stored here
│   ├── customers.txt
│   ├── drivers.txt
│   ├── administrators.txt
│   └── bookings.txt
├── README.md            ← Full documentation
├── PROJECT_REPORT.md    ← Project report
└── diagrams/
    └── UML_DIAGRAMS.md  ← UML diagrams
```

---

## Running Tests

To verify everything works correctly:

```bash
python test_system.py
```

You should see:
```
✅ ALL TESTS PASSED SUCCESSFULLY!
```

---

## Need Help?

1. **Check the README**: See README.md for detailed documentation
2. **Review the Report**: See PROJECT_REPORT.md for design details
3. **View UML Diagrams**: See diagrams/UML_DIAGRAMS.md for system design
4. **Check Data Files**: Look in data/ directory to see stored records

---

## Tips for Best Experience

1. **Start with demo data**: Run `setup_demo.py` first to see the system in action
2. **Try all roles**: Login as customer, driver, and admin to see different perspectives
3. **Test workflows**: Create a booking as customer, assign as admin, view as driver
4. **Experiment**: Try updating, cancelling, and creating multiple bookings
5. **Check conflicts**: Try assigning same driver to overlapping bookings

---

## What's Next?

After trying the system:
1. Review the UML diagrams to understand the design
2. Read the project report for implementation details
3. Examine the code to see how features are implemented
4. Consider potential enhancements (GUI, database, etc.)

---

**Enjoy using the Taxi Booking System!**

# 🚖 Taxi Booking System - Quick Start Guide

## 🎯 Choose Your Interface

### Option 1: Modern GUI Application (Recommended)
**Features**: Password Security ✓ | Auto Driver Assignment ✓ | Beautiful Interface ✓

```bash
cd taxi_booking_system
python3 gui_main.py
```

### Option 2: Classic CLI Application
**Features**: Text-based | Simple | Password Security ✓

```bash
cd taxi_booking_system
python3 main.py
```

---

## 📦 Installation

### Prerequisites
```bash
# Check Python version (requires 3.6+)
python3 --version

# Install PyQt5 (for GUI only)
pip install PyQt5
```

### Quick Setup
```bash
# Clone or navigate to repository
cd taxi_booking_system

# Run tests to verify installation
python3 test_gui_system.py
```

---

## 🔑 Default Login Credentials

### 👤 Administrator
- **Username**: `admin`
- **Password**: `admin123`
- **Access**: Full system control

### 🚗 Drivers (3 available)
| Username | Password | Name | Location |
|----------|----------|------|----------|
| driver1 | pass123 | John Driver | Manhattan |
| driver2 | pass123 | Jane Driver | Times Square |
| driver3 | pass123 | Bob Driver | Central Park |

### 👥 Customers
- No default customers
- **Register through GUI/CLI**

---

## 🚀 Quick Tutorial

### For Customers

#### 1️⃣ Register (First Time)
**GUI:**
1. Click "Register (Customer)" on login screen
2. Fill in all fields
3. Get your Customer ID
4. Login with your credentials

**CLI:**
1. Select "Customer Registration"
2. Enter all required information
3. Note your Customer ID

#### 2️⃣ Book a Taxi
**GUI:**
1. Login as Customer
2. Go to "Book Taxi" tab
3. Enter pickup and dropoff locations
4. Select date and time
5. Click "Book Taxi (Auto-Assign Driver)"
6. 🎉 Driver automatically assigned!

**CLI:**
1. Login as Customer
2. Select "Book a Taxi"
3. Enter booking details
4. Status: Pending (admin will assign driver)

#### 3️⃣ View Your Bookings
**GUI:**
- Navigate to "My Bookings" tab
- See all bookings with driver info

**CLI:**
- Select "View My Bookings"
- See booking history

---

### For Drivers

#### 1️⃣ Login
- Username: `driver1` (or driver2/driver3)
- Password: `pass123`

#### 2️⃣ View Assigned Trips
**GUI:**
- Automatically shows in "My Trips" tab
- Includes customer name and phone

**CLI:**
- Select "View My Assigned Trips"
- See trip details

---

### For Administrators

#### 1️⃣ Login
- Username: `admin`
- Password: `admin123`

#### 2️⃣ View System Status
**GUI:**
- "All Bookings" tab: See all bookings
- "Statistics" tab: System metrics

**CLI:**
- Select from admin menu options

#### 3️⃣ Assign Drivers
**GUI:**
- Click "Auto-Assign Pending Bookings"
- ✨ Magic! System assigns optimal drivers

**CLI:**
- Select "Assign Driver to Booking"
- Choose booking and driver

---

## 🎨 GUI Features Overview

### 🔐 Login Window
- **User Type Selection**: Customer | Driver | Administrator
- **Secure Login**: Hashed password verification
- **Quick Registration**: One-click customer registration

### 👤 Customer Dashboard
```
┌─────────────────────────────────────┐
│ Welcome, Alice Johnson!             │
├─────────────────────────────────────┤
│ Tab: Book Taxi                      │
│   • Pickup Location                 │
│   • Dropoff Location                │
│   • Date Picker (Calendar)          │
│   • Time Picker (Clock)             │
│   • [Book Taxi (Auto-Assign)]       │
│                                     │
│ Tab: My Bookings                    │
│   • Table with all bookings         │
│   • Booking ID | Status | Driver    │
│   • [Refresh Bookings]              │
└─────────────────────────────────────┘
```

### 🚗 Driver Dashboard
```
┌─────────────────────────────────────┐
│ Welcome, John Driver!               │
├─────────────────────────────────────┤
│ Tab: My Trips                       │
│   • Booking ID                      │
│   • Customer Name & Phone           │
│   • Pickup & Dropoff                │
│   • Date & Time                     │
│   • [Refresh Trips]                 │
└─────────────────────────────────────┘
```

### 👔 Admin Dashboard
```
┌─────────────────────────────────────┐
│ Welcome, System Administrator!      │
├─────────────────────────────────────┤
│ Tab: All Bookings                   │
│   • Complete booking overview       │
│   • [Refresh]                       │
│   • [Auto-Assign Pending Bookings]  │
│                                     │
│ Tab: Statistics                     │
│   • Total customers/drivers         │
│   • Booking status breakdown        │
│   • Driver utilization metrics      │
│   • [Refresh Statistics]            │
└─────────────────────────────────────┘
```

---

## 🧠 Intelligent Features

### 🎯 Auto Driver Assignment Algorithm
When you book a taxi, the system:

1. **Finds Available Drivers**
   - Checks all drivers
   - Filters out busy drivers (2-hour buffer)

2. **Calculates Distances**
   - Uses Haversine formula
   - GPS coordinates for accuracy

3. **Selects Best Driver**
   - Nearest available driver
   - Optimal for customer

4. **Updates Booking**
   - Status: Pending → Assigned
   - Notification to customer

**Example:**
```
Booking: Times Square → JFK Airport
Time: 10:00 AM

Available Drivers:
✓ Jane (0.5 km away) ← ASSIGNED!
✗ John (5.3 km away)
✗ Bob (Busy at 10:00 AM)
```

### 🔒 Password Security
- **SHA-256 Hashing**: Industry standard
- **No Plain Text**: Passwords never stored unencrypted
- **Secure Verification**: Hash comparison only
- **One-Way**: Cannot reverse hash to password

**Security Flow:**
```
User enters: "myPassword123"
         ↓
SHA-256 Hash: "a3f2b8c9d1e4..."
         ↓
Stored in DB: "a3f2b8c9d1e4..."
```

---

## 📁 Data Storage

### Location
```
taxi_booking_system/
└── data/
    ├── customers.txt        (Customer records)
    ├── drivers.txt          (Driver records with GPS)
    ├── administrators.txt   (Admin records)
    └── bookings.txt         (Booking records)
```

### Format
All data stored in pipe-delimited format:
```
# customers.txt
C001|alice|[hash]|Alice Johnson|123 Oak St|555-1001|alice@email.com

# drivers.txt
D001|driver1|[hash]|John Driver|555-0101|DL001|40.7128|-74.0060

# bookings.txt
B001|C001|Times Sq|JFK|2024-12-25|10:00|Assigned|D002|40.758|-73.99|40.64|-73.78
```

---

## 🧪 Testing

### Run All Tests
```bash
# GUI system tests
python3 test_gui_system.py

# Legacy system tests
python3 test_system.py
```

### Test Coverage
- ✓ Password hashing
- ✓ Driver locations
- ✓ Distance calculation
- ✓ Driver availability
- ✓ Auto assignment
- ✓ Data persistence
- ✓ Authentication

---

## 🔧 Troubleshooting

### Problem: PyQt5 not found
**Solution:**
```bash
pip install PyQt5
```

### Problem: Login fails with correct password
**Solution:**
- Check if data files exist in `data/` directory
- Run migration script if upgrading from old version:
  ```bash
  python3 migrate_passwords.py
  ```

### Problem: No drivers available for booking
**Solution:**
- Check if drivers exist: Login as admin → View statistics
- Try different date/time
- Drivers may be busy (2-hour buffer per booking)

### Problem: Import errors
**Solution:**
```bash
# Make sure you're in the correct directory
cd taxi_booking_system
python3 gui_main.py
```

---

## 📚 Documentation

### Full Documentation
- **GUI_README.md** - Complete GUI feature guide
- **ARCHITECTURE.md** - System architecture & algorithms
- **README.md** - Original system documentation

### Key Concepts
- **Haversine Formula**: Distance calculation between GPS points
- **Driver Assignment**: Nearest available driver algorithm
- **Password Hashing**: SHA-256 security implementation
- **Booking States**: Pending → Assigned → Completed/Cancelled

---

## 🎓 Learning Resources

### Concepts Demonstrated
1. **Object-Oriented Programming**
   - Inheritance (User → Customer/Driver/Admin)
   - Encapsulation (private methods)
   - Polymorphism (different user types)

2. **GUI Development**
   - Event-driven programming
   - PyQt5 widgets and layouts
   - User experience design

3. **Algorithms**
   - Distance calculation (Haversine)
   - Scheduling (conflict prevention)
   - Optimization (nearest driver)

4. **Security**
   - Password hashing (SHA-256)
   - Authentication mechanisms
   - Data protection

5. **Software Engineering**
   - Modular design
   - Testing (unit tests)
   - Documentation
   - Version control

---

## 🌟 Feature Comparison

| Feature | GUI Version | CLI Version |
|---------|-------------|-------------|
| Password Hashing | ✅ SHA-256 | ✅ SHA-256 |
| Auto Driver Assignment | ✅ Yes | ❌ Manual |
| Location Tracking | ✅ GPS Coords | ❌ No |
| User Interface | 🎨 Modern | 📝 Text |
| Date/Time Picker | ✅ Calendar | 📝 Manual Entry |
| Real-time Stats | ✅ Yes | ⚠️ Limited |
| Recommended For | Production | Learning |

---

## 💡 Tips & Tricks

### For Best Experience
1. **Use GUI version** for production
2. **Run tests** before first use
3. **Backup data/** directory regularly
4. **Use unique usernames** for each customer
5. **Check statistics** to monitor system health

### Performance Tips
- System handles 100+ bookings efficiently
- Driver assignment is instant (<1 second)
- No internet required (standalone app)

---

## 🚀 Next Steps

### Getting Started
1. ✅ Install PyQt5
2. ✅ Run `python3 test_gui_system.py`
3. ✅ Start `python3 gui_main.py`
4. ✅ Register as customer
5. ✅ Book your first taxi!

### Advanced Usage
- Read ARCHITECTURE.md for algorithm details
- Customize driver locations in data/drivers.txt
- Extend system with new features
- Deploy for real use case

---

## 📞 Need Help?

1. Check troubleshooting section above
2. Review GUI_README.md for detailed features
3. Run tests to verify system health
4. Check data files for correct format

---

**🎉 Ready to Book! Start with `python3 gui_main.py` 🎉**

---

*Built with Python 🐍 | PyQt5 🎨 | Love ❤️*

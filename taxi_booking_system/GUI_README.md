# Taxi Booking System - GUI Edition

## 🚖 A Modern, Secure, and Intelligent Taxi Booking Application

This is a complete GUI-based taxi booking system with enhanced security features and intelligent driver assignment algorithm. Built with Python and PyQt5.

---

## ✨ Key Features

### 🔒 **Enhanced Security & Privacy**
- **Password Hashing**: All passwords are securely hashed using SHA-256
- **Secure Authentication**: No plain-text password storage
- **User Privacy**: Sensitive customer data is protected
- **Session Management**: Secure user sessions

### 🤖 **Intelligent Driver Assignment**
- **Automatic Assignment**: Drivers are automatically assigned based on proximity
- **Distance Calculation**: Uses Haversine formula for accurate distance calculation
- **Availability Checking**: Prevents driver double-booking (2-hour buffer)
- **Smart Recommendations**: Admin can see top recommended drivers for each booking

### 🎨 **Modern GUI Interface**
- **User-Friendly Design**: Clean and intuitive interface
- **Role-Based Access**: Separate interfaces for Customers, Drivers, and Administrators
- **Real-Time Updates**: Live booking status and driver assignment
- **Tabbed Navigation**: Easy-to-use tabs for different functions

---

## 📋 Requirements

- Python 3.6 or higher
- PyQt5

### Installation

```bash
# Install PyQt5
pip install PyQt5
```

---

## 🚀 Quick Start

### Running the GUI Application

```bash
cd taxi_booking_system
python3 gui_main.py
```

### First-Time Setup

The system automatically creates:
- Default administrator account
- Three sample drivers with locations
- Empty customer and booking databases

---

## 👤 Default Credentials

### Administrator
- **Username**: `admin`
- **Password**: `admin123`

### Drivers
- **Username**: `driver1`, **Password**: `pass123` (John Driver)
- **Username**: `driver2`, **Password**: `pass123` (Jane Driver)
- **Username**: `driver3`, **Password**: `pass123` (Bob Driver)

### Customers
No default customers - register through the GUI!

---

## 📖 User Guide

### For Customers

1. **Registration**:
   - Click "Register (Customer)" on login screen
   - Fill in all required information
   - System will generate a unique Customer ID
   - Login with your credentials

2. **Booking a Taxi**:
   - Navigate to "Book Taxi" tab
   - Enter pickup and dropoff locations
   - Select date and time
   - Click "Book Taxi (Auto-Assign Driver)"
   - System automatically finds and assigns nearest available driver!

3. **View Bookings**:
   - Navigate to "My Bookings" tab
   - See all your bookings with status and assigned driver
   - Click "Refresh Bookings" to update

### For Drivers

1. **Login**:
   - Select "Driver" radio button
   - Enter driver credentials
   - Click "Login"

2. **View Assigned Trips**:
   - See all assigned trips with customer details
   - View customer phone number for contact
   - Check pickup/dropoff locations and times

### For Administrators

1. **Login**:
   - Select "Administrator" radio button
   - Enter admin credentials
   - Click "Login"

2. **View All Bookings**:
   - See complete booking overview
   - Monitor all customer bookings
   - Track driver assignments

3. **Auto-Assign Drivers**:
   - Click "Auto-Assign Pending Bookings"
   - System intelligently assigns nearest available drivers
   - Prevents scheduling conflicts automatically

4. **View Statistics**:
   - Navigate to "Statistics" tab
   - Monitor system health
   - Track driver utilization

---

## 🧠 Driver Assignment Algorithm

The system uses a sophisticated algorithm to assign drivers:

### Algorithm Steps:

1. **Availability Check**: Filter drivers not busy at booking time
2. **Distance Calculation**: Calculate distance from each driver to pickup location using Haversine formula
3. **Sort by Distance**: Rank drivers by proximity (nearest first)
4. **Conflict Prevention**: Ensure 2-hour buffer between bookings
5. **Assignment**: Automatically assign the optimal driver

### Distance Formula:

The system uses the Haversine formula to calculate accurate distances between GPS coordinates:

```
d = 2r × arcsin(√(sin²((lat₂-lat₁)/2) + cos(lat₁) × cos(lat₂) × sin²((lon₂-lon₁)/2)))
```

Where:
- `r` = Earth's radius (6371 km)
- `lat₁, lon₁` = Driver's location
- `lat₂, lon₂` = Pickup location

---

## 🔐 Security Features

### Password Security
- All passwords are hashed using SHA-256
- 64-character hexadecimal hash output
- No reversible encryption - one-way hashing
- Passwords never stored in plain text

### Migration Tool
If you have existing data with plain-text passwords:

```bash
cd taxi_booking_system
python3 migrate_passwords.py
```

This will:
- Backup existing data files
- Convert all passwords to hashed format
- Maintain system compatibility

---

## 📁 Project Structure

```
taxi_booking_system/
├── gui_main.py                  # Main GUI application
├── main.py                      # Legacy CLI version
├── models.py                    # Data models with password hashing
├── data_manager.py              # Data persistence layer
├── assignment_algorithm.py      # Intelligent driver assignment
├── migrate_passwords.py         # Password migration tool
├── test_system.py              # Test suite
├── setup_demo.py               # Demo data setup
├── README.md                   # Legacy documentation
├── GUI_README.md               # This file
└── data/                       # Data storage
    ├── customers.txt           # Customer records
    ├── drivers.txt            # Driver records with coordinates
    ├── administrators.txt     # Admin records
    └── bookings.txt          # Booking records
```

---

## 🏗️ Architecture

### Data Models

**User (Base Class)**
- `user_id`: Unique identifier
- `username`: Login username
- `password`: SHA-256 hashed password
- `name`: Full name
- `verify_password()`: Secure password verification

**Customer** (extends User)
- `address`: Home address
- `phone`: Contact number
- `email`: Email address

**Driver** (extends User)
- `phone`: Contact number
- `license_number`: Driver's license
- `latitude`: Current GPS latitude
- `longitude`: Current GPS longitude
- `is_available`: Availability status

**Administrator** (extends User)
- Standard user fields only

**Booking**
- `booking_id`: Unique identifier
- `customer_id`: Associated customer
- `driver_id`: Assigned driver (if any)
- `pickup_location`: Pickup address
- `dropoff_location`: Destination address
- `pickup_lat/lon`: Pickup coordinates
- `dropoff_lat/lon`: Destination coordinates
- `booking_date`: Scheduled date
- `booking_time`: Scheduled time
- `status`: Pending/Assigned/Completed/Cancelled

---

## 🧪 Testing

### Running Tests

```bash
cd taxi_booking_system
python3 test_system.py
```

The test suite covers:
- Model serialization/deserialization
- Password hashing and verification
- Data persistence
- User authentication
- Booking creation and management
- Driver assignment
- Conflict detection

---

## 🔄 Legacy CLI Version

The original command-line interface is still available:

```bash
cd taxi_booking_system
python3 main.py
```

**Note**: The CLI version does not include:
- Password hashing
- Automatic driver assignment
- Location-based matching

---

## 🛠️ Development

### Adding New Features

The modular design makes it easy to extend:

1. **New User Types**: Extend the `User` base class
2. **New Algorithms**: Add to `assignment_algorithm.py`
3. **GUI Enhancements**: Modify `gui_main.py`
4. **Data Models**: Update `models.py` and `data_manager.py`

### Code Style

- Follow PEP 8 guidelines
- Use docstrings for all classes and methods
- Keep functions focused and small
- Add type hints where appropriate

---

## 📊 System Statistics

The admin dashboard provides:
- Total customers, drivers, and bookings
- Booking status breakdown (Pending/Assigned/Completed/Cancelled)
- Driver utilization metrics
- Real-time system health monitoring

---

## ⚠️ Important Notes

### Data Storage
- All data stored in plain text files with pipe delimiters
- Passwords are hashed - never in plain text
- Easy migration to database if needed
- Backup data directory regularly

### Driver Locations
- Current implementation uses mock NYC coordinates
- In production, integrate with GPS/mapping API
- Update driver locations in real-time
- Consider implementing geofencing

### Booking Coordinates
- Currently generates random coordinates for demo
- In production, integrate geocoding API (Google Maps, OpenStreetMap)
- Convert addresses to lat/lon automatically
- Validate location accuracy

---

## 🐛 Troubleshooting

### PyQt5 Not Found
```bash
pip install PyQt5
```

### Import Errors
Ensure you're running from the correct directory:
```bash
cd taxi_booking_system
python3 gui_main.py
```

### Login Issues
- Verify username and password
- Check you've selected correct user type
- Ensure data files exist in `data/` directory

### Password Migration Failed
- Check file permissions
- Verify data directory exists
- Review backup files created

---

## 🚀 Future Enhancements

### Planned Features
- [ ] Real-time GPS tracking integration
- [ ] Payment gateway integration
- [ ] SMS/Email notifications
- [ ] Rating and review system
- [ ] Trip history and analytics
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] API for third-party integration

### Technical Improvements
- [ ] Database migration (SQLite/PostgreSQL)
- [ ] RESTful API backend
- [ ] WebSocket for real-time updates
- [ ] Containerization (Docker)
- [ ] Cloud deployment
- [ ] Automated testing (pytest)
- [ ] CI/CD pipeline

---

## 📝 License

This is an educational project for learning purposes.

---

## 👥 Contributing

This project demonstrates:
- Object-oriented programming
- GUI development with PyQt5
- Algorithm design and implementation
- Security best practices
- Software architecture patterns
- Data modeling and persistence

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the user guide
3. Examine the test suite for examples
4. Check the code comments and docstrings

---

## 🎓 Educational Value

This project demonstrates:
- **Computational Thinking**: Decomposition, pattern recognition, abstraction, algorithms
- **Software Engineering**: Modular design, clean architecture, testing
- **Security**: Password hashing, secure authentication, data protection
- **Algorithms**: Distance calculation, optimization, scheduling
- **GUI Development**: Event handling, user experience, interface design
- **Data Management**: CRUD operations, file I/O, data modeling

---

**Built with ❤️ using Python and PyQt5**

🚖 Happy Booking! 🚖

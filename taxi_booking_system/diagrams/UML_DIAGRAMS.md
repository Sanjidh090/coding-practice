# UML Diagrams for Taxi Booking System

## 1. USE CASE DIAGRAM

### Actors:
1. Customer
2. Driver
3. Administrator

### Use Cases:

#### Customer Use Cases:
- Register (extends: Login)
- Login
- Book Taxi
  - Include: Enter Pickup Location
  - Include: Enter Dropoff Location
  - Include: Enter Date & Time
- View Bookings
- Update Booking
  - Precondition: Booking must be in "Pending" status
- Cancel Booking
  - Precondition: Booking must not be "Completed" or "Cancelled"

#### Driver Use Cases:
- Login
- View Assigned Trips
  - Display: Customer details, pickup/dropoff, date/time

#### Administrator Use Cases:
- Login
- View All Bookings
- Assign Driver to Booking
  - Include: Check Driver Availability
  - Include: Prevent Conflict
- View All Drivers
- View All Customers

### Relationships:
- All users have "Login" as a required use case
- "Check Driver Availability" is included in "Assign Driver to Booking"
- "Register" leads to "Login" for customers

---

## 2. ACTIVITY DIAGRAM - Customer Booking a Taxi

```
START
  ↓
[Customer Logs In]
  ↓
[Display Customer Menu]
  ↓
[Select "Book a Taxi"]
  ↓
[Enter Pickup Location]
  ↓
[Enter Dropoff Location]
  ↓
[Enter Date]
  ↓
<Validate Date Format> ─→ [Invalid] ─→ [Show Error] ─→ [Loop back to Enter Date]
  ↓ [Valid]
[Enter Time]
  ↓
<Validate Time Format> ─→ [Invalid] ─→ [Show Error] ─→ [Loop back to Enter Time]
  ↓ [Valid]
[Generate Booking ID]
  ↓
[Create Booking with Status="Pending"]
  ↓
[Save Booking to File]
  ↓
<Save Successful?> 
  ↓ [Yes]
[Display Success Message with Booking ID]
  ↓
[Return to Customer Menu]
  ↓
END
  
  ↓ [No]
[Display Error Message]
  ↓
[Return to Customer Menu]
  ↓
END
```

**Decision Points:**
- Date validation (YYYY-MM-DD format)
- Time validation (HH:MM format)
- Save operation success/failure

**Swimlanes:**
- Customer Lane: Input activities
- System Lane: Validation, generation, persistence

---

## 3. ACTIVITY DIAGRAM - Administrator Assigning Driver

```
START
  ↓
[Administrator Logs In]
  ↓
[Display Admin Menu]
  ↓
[Select "Assign Driver to Booking"]
  ↓
[Load All Bookings]
  ↓
[Filter Pending Bookings]
  ↓
<Any Pending Bookings?> ─→ [No] ─→ [Show "No Pending Bookings"] ─→ [Return to Menu] ─→ END
  ↓ [Yes]
[Display Pending Bookings]
  ↓
[Administrator Selects Booking]
  ↓
[Load All Drivers]
  ↓
[For Each Driver, Check Availability]
  ↓
[Display Drivers with Availability Status]
  ↓
[Administrator Selects Driver]
  ↓
<Driver Available?> ─→ [No] ─→ [Show Warning]
  ↓                              ↓
[Yes]                     <Override?> ─→ [No] ─→ [Return to Driver Selection]
  ↓                              ↓ [Yes]
  └──────────[Continue]──────────┘
  ↓
[Assign Driver ID to Booking]
  ↓
[Update Booking Status to "Assigned"]
  ↓
[Save Updated Booking]
  ↓
<Save Successful?>
  ↓ [Yes]
[Display Success Message]
  ↓
[Return to Admin Menu]
  ↓
END

  ↓ [No]
[Display Error Message]
  ↓
[Return to Admin Menu]
  ↓
END
```

**Parallel Activities:**
- Checking availability for multiple drivers (concurrent)
- Loading driver and booking data (can be parallel)

---

## 4. CLASS DIAGRAM

```
┌─────────────────────────────────────┐
│           <<abstract>>              │
│              User                   │
├─────────────────────────────────────┤
│ - user_id: str                      │
│ - username: str                     │
│ - password: str                     │
│ - name: str                         │
├─────────────────────────────────────┤
│ + __init__(...)                     │
│ + to_string(): str                  │
└─────────────────────────────────────┘
           △
           │
           │ (inherits)
    ┌──────┴──────┬──────────────┐
    │             │              │
    │             │              │
┌───┴────────┐ ┌──┴─────────┐ ┌─┴──────────────┐
│  Customer  │ │   Driver   │ │ Administrator  │
├────────────┤ ├────────────┤ ├────────────────┤
│ + address  │ │ + phone    │ │                │
│ + phone    │ │ + license_ │ │                │
│ + email    │ │   number   │ │                │
├────────────┤ ├────────────┤ ├────────────────┤
│+ to_string│ │+ to_string │ │+ from_string() │
│+ from_     │ │+ from_     │ │                │
│  string()  │ │  string()  │ │                │
└────────────┘ └────────────┘ └────────────────┘
     1                1
     │                │
     │                │
     │ creates        │ assigned to
     │                │
     ↓                ↓
┌─────────────────────────────────────┐
│           Booking                   │
├─────────────────────────────────────┤
│ - booking_id: str                   │
│ - customer_id: str                  │
│ - pickup_location: str              │
│ - dropoff_location: str             │
│ - booking_date: str                 │
│ - booking_time: str                 │
│ - status: str                       │
│ - driver_id: str                    │
├─────────────────────────────────────┤
│ + __init__(...)                     │
│ + to_string(): str                  │
│ + from_string(data): Booking        │
│ + get_datetime(): datetime          │
└─────────────────────────────────────┘
           │
           │ manages
           ↓
┌─────────────────────────────────────┐
│         DataManager                 │
├─────────────────────────────────────┤
│ - data_dir: str                     │
│ - customers_file: str               │
│ - drivers_file: str                 │
│ - admins_file: str                  │
│ - bookings_file: str                │
├─────────────────────────────────────┤
│ + __init__(data_dir)                │
│ + save_customer(customer): bool     │
│ + get_all_customers(): List         │
│ + get_customer_by_username(str)     │
│ + get_customer_by_id(str)           │
│ + get_all_drivers(): List           │
│ + get_driver_by_username(str)       │
│ + get_driver_by_id(str)             │
│ + get_all_admins(): List            │
│ + get_admin_by_username(str)        │
│ + save_booking(booking): bool       │
│ + get_all_bookings(): List          │
│ + update_booking(booking): bool     │
│ + get_bookings_by_customer(str)     │
│ + get_bookings_by_driver(str)       │
│ + check_driver_availability(...)    │
│ + get_next_customer_id(): str       │
│ + get_next_booking_id(): str        │
└─────────────────────────────────────┘
           │
           │ uses
           ↓
┌─────────────────────────────────────┐
│      TaxiBookingSystem              │
├─────────────────────────────────────┤
│ - data_manager: DataManager         │
│ - current_user: User                │
│ - user_type: str                    │
├─────────────────────────────────────┤
│ + __init__()                        │
│ + main_menu()                       │
│ + customer_login()                  │
│ + customer_registration()           │
│ + customer_menu()                   │
│ + book_taxi()                       │
│ + view_customer_bookings()          │
│ + update_booking()                  │
│ + cancel_booking()                  │
│ + driver_login()                    │
│ + driver_menu()                     │
│ + view_driver_trips()               │
│ + admin_login()                     │
│ + admin_menu()                      │
│ + view_all_bookings()               │
│ + assign_driver()                   │
│ + view_all_drivers()                │
│ + view_all_customers()              │
│ + run()                             │
└─────────────────────────────────────┘
```

### Relationships:
1. **Inheritance**: Customer, Driver, and Administrator inherit from User
2. **Association**: 
   - Customer creates Booking (1 to many)
   - Driver is assigned to Booking (1 to many)
3. **Composition**: TaxiBookingSystem contains DataManager
4. **Dependency**: DataManager depends on all model classes

### Multiplicity:
- One Customer can have multiple Bookings (1..*)
- One Driver can have multiple Bookings (0..*)
- One Booking belongs to one Customer (1)
- One Booking may have zero or one Driver (0..1)

---

## 5. SEQUENCE DIAGRAM - Booking Process

```
Customer    System         DataManager    File System
   │           │               │              │
   │─login()──→│               │              │
   │           │─verify()─────→│              │
   │           │               │─read()──────→│
   │           │               │←─data────────│
   │           │←─success──────│              │
   │←─menu─────│               │              │
   │           │               │              │
   │─book()───→│               │              │
   │           │─validate()────│              │
   │           │               │              │
   │           │─generate_id()→│              │
   │           │←─booking_id───│              │
   │           │               │              │
   │           │─save()───────→│              │
   │           │               │─write()─────→│
   │           │               │←─success─────│
   │           │←─success──────│              │
   │←─confirm──│               │              │
   │           │               │              │
```

---

## 6. STATE DIAGRAM - Booking Status

```
     [START]
        ↓
   ┌─────────┐
   │ Pending │ ← Initial state after customer books
   └─────────┘
        │
        │ Administrator assigns driver
        ↓
   ┌──────────┐
   │ Assigned │ ← Driver is assigned
   └──────────┘
        │
        ├───────────────────────┐
        │                       │
        │ Trip completed        │ Customer cancels
        ↓                       ↓
   ┌───────────┐          ┌───────────┐
   │ Completed │          │ Cancelled │
   └───────────┘          └───────────┘
        │                       │
        ↓                       ↓
      [END]                   [END]
```

**State Transitions:**
- Pending → Assigned (Administrator assigns driver)
- Assigned → Completed (Trip is completed)
- Pending → Cancelled (Customer cancels before assignment)
- Assigned → Cancelled (Customer cancels after assignment)

**Business Rules:**
- Only Pending bookings can be updated by customer
- Only Pending bookings can be assigned by administrator
- Cancelled and Completed bookings cannot be modified

---

## Design Patterns Used

1. **Singleton Pattern**: DataManager (single instance managing all data)
2. **Factory Pattern**: from_string() methods create objects from serialized data
3. **Template Method**: User base class provides common structure
4. **Strategy Pattern**: Different menu strategies for different user types

## Key Design Principles

1. **Single Responsibility**: Each class has one clear purpose
2. **Open/Closed**: Easy to extend with new user types
3. **Liskov Substitution**: Child classes can replace User base class
4. **Interface Segregation**: Each user type has specific interfaces
5. **Dependency Inversion**: High-level modules depend on abstractions

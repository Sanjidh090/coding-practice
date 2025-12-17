# Visual UML Diagrams (ASCII Art)

This file contains visual representations of the UML diagrams for the Taxi Booking System.

## 1. USE CASE DIAGRAM

```
                     TAXI BOOKING SYSTEM
     ┌─────────────────────────────────────────────────────┐
     │                                                       │
     │                                                       │
     │    ╔══════════╗                       ╔══════════╗  │
     │    ║ Customer ║                       ║  Driver  ║  │
     │    ╚═════╤════╝                       ╚═════╤════╝  │
     │          │                                  │        │
     │          │                                  │        │
     │          ├──────►(Register)                 │        │
     │          │                                  │        │
     │          ├──────►(Login)◄──────────────────┤        │
     │          │          │                       │        │
     │          │          │                       │        │
     │          ├──────►(Book Taxi)                │        │
     │          │       ↓ includes                 │        │
     │          │    (Enter Pickup)                │        │
     │          │    (Enter Dropoff)               │        │
     │          │    (Enter Date/Time)             │        │
     │          │                                  │        │
     │          ├──────►(View Bookings)◄───────────┤        │
     │          │                                  │        │
     │          ├──────►(Update Booking)           │        │
     │          │                                  │        │
     │          ├──────►(Cancel Booking)           │        │
     │          │                                  │        │
     │          │                                  │        │
     │          │       ╔════════════════╗         │        │
     │          │       ║ Administrator  ║         │        │
     │          │       ╚═══════╤════════╝         │        │
     │          │               │                  │        │
     │          └───────────────┼──────────────────┘        │
     │                          │                            │
     │                          ├──────►(Assign Driver)      │
     │                          │         ↓ includes         │
     │                          │    (Check Availability)    │
     │                          │    (Prevent Conflict)      │
     │                          │                            │
     │                          ├──────►(View All Bookings)  │
     │                          │                            │
     │                          ├──────►(View All Drivers)   │
     │                          │                            │
     │                          └──────►(View All Customers) │
     │                                                       │
     └─────────────────────────────────────────────────────┘
```

## 2. CLASS DIAGRAM

```
┌─────────────────────────────────────────────────────────────────┐
│                          <<abstract>>                            │
│                             User                                 │
├─────────────────────────────────────────────────────────────────┤
│ # user_id: str                                                   │
│ # username: str                                                  │
│ # password: str                                                  │
│ # name: str                                                      │
├─────────────────────────────────────────────────────────────────┤
│ + __init__(user_id, username, password, name)                   │
│ + to_string(): str                                              │
└─────────────────────────────────────────────────────────────────┘
                              △
                              │
                              │ inherits
              ┌───────────────┼───────────────┐
              │               │               │
┌─────────────┴───────────┐ ┌┴────────────────┴┐ ┌───────────────┴────────┐
│      Customer           │ │      Driver       │ │    Administrator       │
├─────────────────────────┤ ├───────────────────┤ ├────────────────────────┤
│ - address: str          │ │ - phone: str      │ │                        │
│ - phone: str            │ │ - license_number  │ │                        │
│ - email: str            │ │                   │ │                        │
├─────────────────────────┤ ├───────────────────┤ ├────────────────────────┤
│ + to_string(): str      │ │ + to_string()     │ │ + from_string(): Admin │
│ + from_string(): Customer│ │ + from_string()  │ │                        │
└────────┬────────────────┘ └──────┬────────────┘ └────────────────────────┘
         │                         │
         │ 1                       │ 0..1
         │                         │
         │ creates                 │ assigned to
         │                         │
         └────────┐       ┌────────┘
                  │       │
                  ↓       ↓
         ┌─────────────────────────────────────┐
         │           Booking                   │
         ├─────────────────────────────────────┤
         │ - booking_id: str                   │
         │ - customer_id: str     ←────────────┼─── FK to Customer
         │ - pickup_location: str              │
         │ - dropoff_location: str             │
         │ - booking_date: str                 │
         │ - booking_time: str                 │
         │ - status: str                       │
         │ - driver_id: str       ←────────────┼─── FK to Driver
         ├─────────────────────────────────────┤
         │ + __init__(...)                     │
         │ + to_string(): str                  │
         │ + from_string(data): Booking        │
         │ + get_datetime(): datetime          │
         └──────────────┬──────────────────────┘
                        │
                        │ manages
                        │ *
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
         │ + save_customer(customer): bool     │
         │ + get_all_customers(): List         │
         │ + save_booking(booking): bool       │
         │ + get_all_bookings(): List          │
         │ + update_booking(booking): bool     │
         │ + check_driver_availability(): bool │
         │ + get_next_customer_id(): str       │
         │ + get_next_booking_id(): str        │
         └──────────────┬──────────────────────┘
                        │
                        │ uses
                        │ 1
                        ↓
         ┌─────────────────────────────────────┐
         │      TaxiBookingSystem              │
         ├─────────────────────────────────────┤
         │ - data_manager: DataManager         │
         │ - current_user: User                │
         │ - user_type: str                    │
         ├─────────────────────────────────────┤
         │ + main_menu()                       │
         │ + customer_login()                  │
         │ + customer_menu()                   │
         │ + book_taxi()                       │
         │ + driver_login()                    │
         │ + driver_menu()                     │
         │ + admin_login()                     │
         │ + admin_menu()                      │
         │ + assign_driver()                   │
         │ + run()                             │
         └─────────────────────────────────────┘
```

## 3. SEQUENCE DIAGRAM - Customer Booking Process

```
 Customer      System          DataManager      FileSystem
    │             │                 │               │
    │──login()───→│                 │               │
    │             │──verify()──────→│               │
    │             │                 │──read()──────→│
    │             │                 │←──data────────┤
    │             │←──success───────┤               │
    │←──menu()────┤                 │               │
    │             │                 │               │
    │──book()────→│                 │               │
    │             │──validate()     │               │
    │             │    dates        │               │
    │             │                 │               │
    │             │──generate_id()─→│               │
    │             │←──booking_id────┤               │
    │             │                 │               │
    │             │──save()────────→│               │
    │             │                 │──write()─────→│
    │             │                 │←──success─────┤
    │             │←──success───────┤               │
    │←──confirm───┤                 │               │
    │             │                 │               │
```

## 4. SEQUENCE DIAGRAM - Administrator Assigns Driver

```
 Admin         System          DataManager      FileSystem
   │              │                 │               │
   │──login()────→│                 │               │
   │              │──verify()──────→│               │
   │              │                 │──read()──────→│
   │              │                 │←──data────────┤
   │              │←──success───────┤               │
   │←──menu()─────┤                 │               │
   │              │                 │               │
   │──assign()───→│                 │               │
   │              │──get_bookings()→│               │
   │              │                 │──read()──────→│
   │              │                 │←──bookings────┤
   │              │←──bookings──────┤               │
   │←──display────┤                 │               │
   │              │                 │               │
   │──select──────→                 │               │
   │              │──check_avail()─→│               │
   │              │                 │──calculate────┤
   │              │←──available─────┤               │
   │←──show───────┤                 │               │
   │              │                 │               │
   │──confirm────→│                 │               │
   │              │──update()──────→│               │
   │              │                 │──write()─────→│
   │              │                 │←──success─────┤
   │              │←──success───────┤               │
   │←──confirm────┤                 │               │
   │              │                 │               │
```

## 5. STATE DIAGRAM - Booking Lifecycle

```
                    ┌───────────┐
                    │   START   │
                    └─────┬─────┘
                          │
                          │ Customer creates booking
                          ↓
                    ┌───────────┐
                ┌──→│  Pending  │←──┐
                │   └─────┬─────┘   │
                │         │         │
                │         │ Admin   │ Customer updates
                │         │ assigns │ (pickup/dropoff/time)
                │         │ driver  │
                │         │         │
                │         ↓         │
                │   ┌───────────┐   │
                │   │ Assigned  │───┘
                │   └─────┬─────┘
                │         │
                │         ├───────────────────┐
                │         │                   │
    Customer    │         │ Trip             │ Customer
    cancels     │         │ completed        │ cancels
    (before     │         │                   │ (after
    assignment) │         ↓                   ↓ assignment)
                │   ┌───────────┐       ┌───────────┐
                └──→│ Cancelled │       │ Completed │
                    └─────┬─────┘       └─────┬─────┘
                          │                   │
                          │                   │
                          └──────┬────────────┘
                                 │
                                 ↓
                           ┌───────────┐
                           │    END    │
                           └───────────┘
```

## 6. ACTIVITY DIAGRAM - Customer Books a Taxi

```
        ┌─────────────┐
        │    START    │
        └──────┬──────┘
               │
               ↓
        ┌─────────────┐
        │ Enter Login │
        │ Credentials │
        └──────┬──────┘
               │
               ↓
        ╱─────────────╲          No
       ╱  Valid Login? ╲─────────────────┐
       ╲───────────────╱                 │
               │ Yes                     │
               ↓                         ↓
        ┌─────────────┐           ┌──────────────┐
        │Show Customer│           │ Show Error   │
        │    Menu     │           │   Message    │
        └──────┬──────┘           └──────┬───────┘
               │                         │
               ↓                         │
        ┌─────────────┐                 │
        │Select "Book │                 │
        │   a Taxi"   │                 │
        └──────┬──────┘                 │
               │                         │
               ↓                         │
        ┌─────────────┐                 │
        │Enter Pickup │                 │
        │  Location   │                 │
        └──────┬──────┘                 │
               │                         │
               ↓                         │
        ┌─────────────┐                 │
        │Enter Dropoff│                 │
        │  Location   │                 │
        └──────┬──────┘                 │
               │                         │
               ↓                         │
        ┌─────────────┐                 │
        │ Enter Date  │                 │
        └──────┬──────┘                 │
               │                         │
               ↓                         │
        ╱─────────────╲          No     │
       ╱  Valid Date?  ╲────────────────┤
       ╲───────────────╱                │
               │ Yes                     │
               ↓                         │
        ┌─────────────┐                 │
        │ Enter Time  │                 │
        └──────┬──────┘                 │
               │                         │
               ↓                         │
        ╱─────────────╲          No     │
       ╱  Valid Time?  ╲────────────────┤
       ╲───────────────╱                │
               │ Yes                     │
               ↓                         │
        ┌─────────────┐                 │
        │  Generate   │                 │
        │ Booking ID  │                 │
        └──────┬──────┘                 │
               │                         │
               ↓                         │
        ┌─────────────┐                 │
        │Create Booking│                │
        │Status:Pending│                │
        └──────┬──────┘                 │
               │                         │
               ↓                         │
        ┌─────────────┐                 │
        │Save to File │                 │
        └──────┬──────┘                 │
               │                         │
               ↓                         │
        ╱─────────────╲          No     │
       ╱  Save Success?╲────────────────┘
       ╲───────────────╱
               │ Yes
               ↓
        ┌─────────────┐
        │   Display   │
        │ Booking ID  │
        │& Confirmation│
        └──────┬──────┘
               │
               ↓
        ┌─────────────┐
        │    END      │
        └─────────────┘
```

## 7. COMPONENT DIAGRAM

```
┌────────────────────────────────────────────────────────────┐
│                  Taxi Booking System                       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────────────┐         ┌────────────────────┐     │
│  │  User Interface  │         │   Business Logic   │     │
│  │    Component     │────────→│     Component      │     │
│  ├──────────────────┤         ├────────────────────┤     │
│  │ • Main Menu      │         │ • Authentication   │     │
│  │ • Customer Menu  │         │ • Booking Mgmt     │     │
│  │ • Driver Menu    │         │ • Assignment Logic │     │
│  │ • Admin Menu     │         │ • Validation       │     │
│  │ • Input/Output   │         │ • Conflict Check   │     │
│  └──────────────────┘         └────────┬───────────┘     │
│                                         │                  │
│                                         │                  │
│                                         ↓                  │
│                               ┌────────────────────┐      │
│                               │   Data Access      │      │
│                               │    Component       │      │
│                               ├────────────────────┤      │
│                               │ • DataManager      │      │
│                               │ • File Operations  │      │
│                               │ • CRUD Methods     │      │
│                               │ • Data Persistence │      │
│                               └────────┬───────────┘      │
│                                        │                   │
│                                        │                   │
│                                        ↓                   │
│                               ┌────────────────────┐      │
│                               │   Model Objects    │      │
│                               │    Component       │      │
│                               ├────────────────────┤      │
│                               │ • Customer         │      │
│                               │ • Driver           │      │
│                               │ • Administrator    │      │
│                               │ • Booking          │      │
│                               └────────────────────┘      │
│                                                            │
└────────────────────────────────────────────────────────────┘
                               │
                               │ persists to
                               ↓
                    ┌──────────────────────┐
                    │   File System        │
                    ├──────────────────────┤
                    │ customers.txt        │
                    │ drivers.txt          │
                    │ administrators.txt   │
                    │ bookings.txt         │
                    └──────────────────────┘
```

## Legend

```
Symbols Used:
━━━━━  Solid line: Association/Connection
- - -  Dashed line: Dependency
──────→ Arrow: Direction of flow
△      Triangle: Inheritance
◊      Diamond: Composition/Aggregation
╱     ╲ Decision diamond
┌─────┐ Rectangle: Class/Component/Process
╔═════╗ Double border: Actor
(name)  Oval: Use case
```

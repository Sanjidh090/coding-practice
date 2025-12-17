"""
Taxi Booking System - GUI Application
Modern GUI interface using PyQt5 with enhanced security and automated driver assignment
"""

import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox,
                             QTabWidget, QTableWidget, QTableWidgetItem, QDialog,
                             QFormLayout, QComboBox, QDateEdit, QTimeEdit, QTextEdit,
                             QHeaderView, QGroupBox, QRadioButton, QButtonGroup)
from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtGui import QFont, QIcon

from models import Customer, Driver, Administrator, Booking
from data_manager import DataManager
from assignment_algorithm import DriverAssignmentAlgorithm


class LoginWindow(QDialog):
    """Login window for all user types"""
    
    def __init__(self):
        super().__init__()
        self.user = None
        self.user_type = None
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Taxi Booking System - Login")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("""
            QDialog {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 12px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton {
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QRadioButton {
                font-size: 12px;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("🚖 Taxi Booking System")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # User type selection
        user_type_group = QGroupBox("Select User Type")
        user_type_layout = QVBoxLayout()
        
        self.user_type_group = QButtonGroup()
        self.customer_radio = QRadioButton("Customer")
        self.driver_radio = QRadioButton("Driver")
        self.admin_radio = QRadioButton("Administrator")
        self.customer_radio.setChecked(True)
        
        self.user_type_group.addButton(self.customer_radio, 1)
        self.user_type_group.addButton(self.driver_radio, 2)
        self.user_type_group.addButton(self.admin_radio, 3)
        
        user_type_layout.addWidget(self.customer_radio)
        user_type_layout.addWidget(self.driver_radio)
        user_type_layout.addWidget(self.admin_radio)
        user_type_group.setLayout(user_type_layout)
        layout.addWidget(user_type_group)
        
        # Login form
        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")
        form_layout.addRow("Username:", self.username_input)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)
        form_layout.addRow("Password:", self.password_input)
        
        layout.addLayout(form_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.handle_login)
        button_layout.addWidget(login_btn)
        
        register_btn = QPushButton("Register (Customer)")
        register_btn.setStyleSheet("background-color: #2196F3;")
        register_btn.clicked.connect(self.show_registration)
        button_layout.addWidget(register_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
        # Data manager
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(script_dir, "data")
        self.data_manager = DataManager(data_dir)
    
    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter username and password")
            return
        
        selected_type = self.user_type_group.checkedId()
        
        if selected_type == 1:  # Customer
            user = self.data_manager.get_customer_by_username(username)
            user_type = "customer"
        elif selected_type == 2:  # Driver
            user = self.data_manager.get_driver_by_username(username)
            user_type = "driver"
        else:  # Admin
            user = self.data_manager.get_admin_by_username(username)
            user_type = "admin"
        
        if user and user.verify_password(password):
            self.user = user
            self.user_type = user_type
            self.accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password!")
    
    def show_registration(self):
        dialog = RegistrationDialog(self.data_manager)
        if dialog.exec_() == QDialog.Accepted:
            QMessageBox.information(self, "Success", 
                                  f"Registration successful!\nYour Customer ID: {dialog.customer_id}\n"
                                  "You can now login with your credentials.")


class RegistrationDialog(QDialog):
    """Customer registration dialog"""
    
    def __init__(self, data_manager):
        super().__init__()
        self.data_manager = data_manager
        self.customer_id = None
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Customer Registration")
        self.setGeometry(150, 150, 400, 450)
        
        layout = QFormLayout()
        
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.name = QLineEdit()
        self.address = QLineEdit()
        self.phone = QLineEdit()
        self.email = QLineEdit()
        
        layout.addRow("Username:", self.username)
        layout.addRow("Password:", self.password)
        layout.addRow("Full Name:", self.name)
        layout.addRow("Address:", self.address)
        layout.addRow("Phone:", self.phone)
        layout.addRow("Email:", self.email)
        
        register_btn = QPushButton("Register")
        register_btn.clicked.connect(self.handle_registration)
        layout.addRow(register_btn)
        
        self.setLayout(layout)
    
    def handle_registration(self):
        # Validate fields
        if not all([self.username.text(), self.password.text(), self.name.text(),
                   self.address.text(), self.phone.text(), self.email.text()]):
            QMessageBox.warning(self, "Error", "All fields are required!")
            return
        
        # Check if username exists
        if self.data_manager.get_customer_by_username(self.username.text()):
            QMessageBox.warning(self, "Error", "Username already exists!")
            return
        
        # Create customer
        customer_id = self.data_manager.get_next_customer_id()
        customer = Customer(
            customer_id,
            self.username.text().strip(),
            self.password.text().strip(),
            self.name.text().strip(),
            self.address.text().strip(),
            self.phone.text().strip(),
            self.email.text().strip()
        )
        
        if self.data_manager.save_customer(customer):
            self.customer_id = customer_id
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Registration failed!")


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self, user, user_type, data_manager):
        super().__init__()
        self.user = user
        self.user_type = user_type
        self.data_manager = data_manager
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle(f"Taxi Booking System - {self.user.name}")
        self.setGeometry(100, 100, 1000, 700)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Welcome message
        welcome = QLabel(f"Welcome, {self.user.name}!")
        welcome_font = QFont()
        welcome_font.setPointSize(14)
        welcome_font.setBold(True)
        welcome.setFont(welcome_font)
        layout.addWidget(welcome)
        
        # Tab widget
        self.tabs = QTabWidget()
        
        if self.user_type == "customer":
            self.setup_customer_tabs()
        elif self.user_type == "driver":
            self.setup_driver_tabs()
        else:  # admin
            self.setup_admin_tabs()
        
        layout.addWidget(self.tabs)
        
        # Logout button
        logout_btn = QPushButton("Logout")
        logout_btn.clicked.connect(self.logout)
        logout_btn.setStyleSheet("background-color: #f44336;")
        layout.addWidget(logout_btn)
        
        central_widget.setLayout(layout)
    
    def setup_customer_tabs(self):
        """Setup tabs for customer"""
        # Book Taxi tab
        book_tab = QWidget()
        book_layout = QVBoxLayout()
        
        form = QFormLayout()
        
        self.pickup_input = QLineEdit()
        self.dropoff_input = QLineEdit()
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)
        self.time_input = QTimeEdit()
        self.time_input.setTime(QTime.currentTime())
        
        form.addRow("Pickup Location:", self.pickup_input)
        form.addRow("Dropoff Location:", self.dropoff_input)
        form.addRow("Date:", self.date_input)
        form.addRow("Time:", self.time_input)
        
        book_btn = QPushButton("Book Taxi (Auto-Assign Driver)")
        book_btn.clicked.connect(self.book_taxi)
        form.addRow(book_btn)
        
        book_layout.addLayout(form)
        book_layout.addStretch()
        book_tab.setLayout(book_layout)
        
        # My Bookings tab
        bookings_tab = QWidget()
        bookings_layout = QVBoxLayout()
        
        refresh_btn = QPushButton("Refresh Bookings")
        refresh_btn.clicked.connect(self.load_customer_bookings)
        bookings_layout.addWidget(refresh_btn)
        
        self.bookings_table = QTableWidget()
        self.bookings_table.setColumnCount(7)
        self.bookings_table.setHorizontalHeaderLabels([
            "Booking ID", "Pickup", "Dropoff", "Date", "Time", "Status", "Driver"
        ])
        self.bookings_table.horizontalHeader().setStretchLastSection(True)
        bookings_layout.addWidget(self.bookings_table)
        
        bookings_tab.setLayout(bookings_layout)
        
        self.tabs.addTab(book_tab, "Book Taxi")
        self.tabs.addTab(bookings_tab, "My Bookings")
        
        # Load bookings
        self.load_customer_bookings()
    
    def setup_driver_tabs(self):
        """Setup tabs for driver"""
        trips_tab = QWidget()
        trips_layout = QVBoxLayout()
        
        refresh_btn = QPushButton("Refresh Trips")
        refresh_btn.clicked.connect(self.load_driver_trips)
        trips_layout.addWidget(refresh_btn)
        
        self.trips_table = QTableWidget()
        self.trips_table.setColumnCount(7)
        self.trips_table.setHorizontalHeaderLabels([
            "Booking ID", "Customer", "Phone", "Pickup", "Dropoff", "Date", "Time"
        ])
        self.trips_table.horizontalHeader().setStretchLastSection(True)
        trips_layout.addWidget(self.trips_table)
        
        trips_tab.setLayout(trips_layout)
        self.tabs.addTab(trips_tab, "My Trips")
        
        # Load trips
        self.load_driver_trips()
    
    def setup_admin_tabs(self):
        """Setup tabs for admin"""
        # All Bookings tab
        bookings_tab = QWidget()
        bookings_layout = QVBoxLayout()
        
        btn_layout = QHBoxLayout()
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.load_all_bookings)
        btn_layout.addWidget(refresh_btn)
        
        assign_btn = QPushButton("Auto-Assign Pending Bookings")
        assign_btn.clicked.connect(self.auto_assign_all_pending)
        btn_layout.addWidget(assign_btn)
        btn_layout.addStretch()
        
        bookings_layout.addLayout(btn_layout)
        
        self.admin_bookings_table = QTableWidget()
        self.admin_bookings_table.setColumnCount(8)
        self.admin_bookings_table.setHorizontalHeaderLabels([
            "ID", "Customer", "Pickup", "Dropoff", "Date", "Time", "Status", "Driver"
        ])
        self.admin_bookings_table.horizontalHeader().setStretchLastSection(True)
        bookings_layout.addWidget(self.admin_bookings_table)
        
        bookings_tab.setLayout(bookings_layout)
        
        # Statistics tab
        stats_tab = QWidget()
        stats_layout = QVBoxLayout()
        
        self.stats_text = QTextEdit()
        self.stats_text.setReadOnly(True)
        stats_layout.addWidget(self.stats_text)
        
        refresh_stats_btn = QPushButton("Refresh Statistics")
        refresh_stats_btn.clicked.connect(self.load_statistics)
        stats_layout.addWidget(refresh_stats_btn)
        
        stats_tab.setLayout(stats_layout)
        
        self.tabs.addTab(bookings_tab, "All Bookings")
        self.tabs.addTab(stats_tab, "Statistics")
        
        # Load data
        self.load_all_bookings()
        self.load_statistics()
    
    def book_taxi(self):
        """Book a taxi with automatic driver assignment"""
        pickup = self.pickup_input.text().strip()
        dropoff = self.dropoff_input.text().strip()
        date = self.date_input.date().toString("yyyy-MM-dd")
        time = self.time_input.time().toString("HH:mm")
        
        if not pickup or not dropoff:
            QMessageBox.warning(self, "Error", "Please fill all fields!")
            return
        
        # Create booking with mock coordinates
        booking_id = self.data_manager.get_next_booking_id()
        
        # Assign random coordinates for demo (in real app, use geocoding API)
        import random
        pickup_lat = 40.7128 + random.uniform(-0.1, 0.1)
        pickup_lon = -74.0060 + random.uniform(-0.1, 0.1)
        dropoff_lat = 40.7128 + random.uniform(-0.1, 0.1)
        dropoff_lon = -74.0060 + random.uniform(-0.1, 0.1)
        
        booking = Booking(
            booking_id, self.user.user_id, pickup, dropoff, date, time,
            "Pending", "", pickup_lat, pickup_lon, dropoff_lat, dropoff_lon
        )
        
        # Try to auto-assign driver
        drivers = self.data_manager.get_all_drivers()
        driver_bookings_map = {}
        for driver in drivers:
            driver_bookings_map[driver.user_id] = self.data_manager.get_bookings_by_driver(driver.user_id)
        
        assigned_driver_id = DriverAssignmentAlgorithm.assign_driver_to_booking(
            booking, drivers, driver_bookings_map
        )
        
        if assigned_driver_id:
            booking.driver_id = assigned_driver_id
            booking.status = "Assigned"
            driver = self.data_manager.get_driver_by_id(assigned_driver_id)
            driver_name = driver.name if driver else "Unknown"
            message = f"Booking created successfully!\nBooking ID: {booking_id}\nDriver: {driver_name} (Auto-assigned)"
        else:
            message = f"Booking created successfully!\nBooking ID: {booking_id}\nStatus: Pending (No available driver at this time)"
        
        if self.data_manager.save_booking(booking):
            QMessageBox.information(self, "Success", message)
            self.pickup_input.clear()
            self.dropoff_input.clear()
            self.load_customer_bookings()
        else:
            QMessageBox.critical(self, "Error", "Failed to create booking!")
    
    def load_customer_bookings(self):
        """Load customer bookings"""
        bookings = self.data_manager.get_bookings_by_customer(self.user.user_id)
        self.bookings_table.setRowCount(len(bookings))
        
        for i, booking in enumerate(bookings):
            driver_name = "Not Assigned"
            if booking.driver_id:
                driver = self.data_manager.get_driver_by_id(booking.driver_id)
                if driver:
                    driver_name = driver.name
            
            self.bookings_table.setItem(i, 0, QTableWidgetItem(booking.booking_id))
            self.bookings_table.setItem(i, 1, QTableWidgetItem(booking.pickup_location))
            self.bookings_table.setItem(i, 2, QTableWidgetItem(booking.dropoff_location))
            self.bookings_table.setItem(i, 3, QTableWidgetItem(booking.booking_date))
            self.bookings_table.setItem(i, 4, QTableWidgetItem(booking.booking_time))
            self.bookings_table.setItem(i, 5, QTableWidgetItem(booking.status))
            self.bookings_table.setItem(i, 6, QTableWidgetItem(driver_name))
    
    def load_driver_trips(self):
        """Load driver trips"""
        bookings = self.data_manager.get_bookings_by_driver(self.user.user_id)
        self.trips_table.setRowCount(len(bookings))
        
        for i, booking in enumerate(bookings):
            customer = self.data_manager.get_customer_by_id(booking.customer_id)
            customer_name = customer.name if customer else "Unknown"
            customer_phone = customer.phone if customer else "N/A"
            
            self.trips_table.setItem(i, 0, QTableWidgetItem(booking.booking_id))
            self.trips_table.setItem(i, 1, QTableWidgetItem(customer_name))
            self.trips_table.setItem(i, 2, QTableWidgetItem(customer_phone))
            self.trips_table.setItem(i, 3, QTableWidgetItem(booking.pickup_location))
            self.trips_table.setItem(i, 4, QTableWidgetItem(booking.dropoff_location))
            self.trips_table.setItem(i, 5, QTableWidgetItem(booking.booking_date))
            self.trips_table.setItem(i, 6, QTableWidgetItem(booking.booking_time))
    
    def load_all_bookings(self):
        """Load all bookings for admin"""
        bookings = self.data_manager.get_all_bookings()
        self.admin_bookings_table.setRowCount(len(bookings))
        
        for i, booking in enumerate(bookings):
            customer = self.data_manager.get_customer_by_id(booking.customer_id)
            customer_name = customer.name if customer else "Unknown"
            
            driver_name = "Not Assigned"
            if booking.driver_id:
                driver = self.data_manager.get_driver_by_id(booking.driver_id)
                if driver:
                    driver_name = driver.name
            
            self.admin_bookings_table.setItem(i, 0, QTableWidgetItem(booking.booking_id))
            self.admin_bookings_table.setItem(i, 1, QTableWidgetItem(customer_name))
            self.admin_bookings_table.setItem(i, 2, QTableWidgetItem(booking.pickup_location))
            self.admin_bookings_table.setItem(i, 3, QTableWidgetItem(booking.dropoff_location))
            self.admin_bookings_table.setItem(i, 4, QTableWidgetItem(booking.booking_date))
            self.admin_bookings_table.setItem(i, 5, QTableWidgetItem(booking.booking_time))
            self.admin_bookings_table.setItem(i, 6, QTableWidgetItem(booking.status))
            self.admin_bookings_table.setItem(i, 7, QTableWidgetItem(driver_name))
    
    def auto_assign_all_pending(self):
        """Auto-assign all pending bookings"""
        bookings = self.data_manager.get_all_bookings()
        pending_bookings = [b for b in bookings if b.status == "Pending"]
        
        if not pending_bookings:
            QMessageBox.information(self, "Info", "No pending bookings to assign!")
            return
        
        drivers = self.data_manager.get_all_drivers()
        driver_bookings_map = {}
        for driver in drivers:
            driver_bookings_map[driver.user_id] = self.data_manager.get_bookings_by_driver(driver.user_id)
        
        assigned_count = 0
        for booking in pending_bookings:
            assigned_driver_id = DriverAssignmentAlgorithm.assign_driver_to_booking(
                booking, drivers, driver_bookings_map
            )
            
            if assigned_driver_id:
                booking.driver_id = assigned_driver_id
                booking.status = "Assigned"
                self.data_manager.update_booking(booking)
                # Update map for next iteration
                driver_bookings_map[assigned_driver_id].append(booking)
                assigned_count += 1
        
        QMessageBox.information(self, "Success", 
                              f"Assigned {assigned_count} out of {len(pending_bookings)} bookings!")
        self.load_all_bookings()
    
    def load_statistics(self):
        """Load system statistics"""
        customers = self.data_manager.get_all_customers()
        drivers = self.data_manager.get_all_drivers()
        bookings = self.data_manager.get_all_bookings()
        
        pending = len([b for b in bookings if b.status == "Pending"])
        assigned = len([b for b in bookings if b.status == "Assigned"])
        completed = len([b for b in bookings if b.status == "Completed"])
        cancelled = len([b for b in bookings if b.status == "Cancelled"])
        
        stats = f"""
        ===== SYSTEM STATISTICS =====
        
        Total Customers: {len(customers)}
        Total Drivers: {len(drivers)}
        Total Bookings: {len(bookings)}
        
        Booking Status:
        - Pending: {pending}
        - Assigned: {assigned}
        - Completed: {completed}
        - Cancelled: {cancelled}
        
        Driver Utilization:
        """
        
        for driver in drivers:
            trips = self.data_manager.get_bookings_by_driver(driver.user_id)
            stats += f"\n- {driver.name}: {len(trips)} trips"
        
        self.stats_text.setText(stats)
    
    def logout(self):
        """Logout and return to login"""
        self.close()
        login_window = LoginWindow()
        if login_window.exec_() == QDialog.Accepted:
            main_window = MainWindow(login_window.user, login_window.user_type, 
                                   login_window.data_manager)
            main_window.show()


def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    
    # Show login
    login_window = LoginWindow()
    if login_window.exec_() == QDialog.Accepted:
        main_window = MainWindow(login_window.user, login_window.user_type, 
                               login_window.data_manager)
        main_window.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    main()

"""
Driver Assignment Algorithm
Intelligent algorithm for assigning nearest available driver to bookings
"""

import math
from typing import List, Optional, Tuple
from datetime import datetime, timedelta


class DriverAssignmentAlgorithm:
    """
    Robust driver assignment algorithm that:
    1. Finds available drivers at the requested time
    2. Calculates distance to pickup location
    3. Assigns the nearest available driver
    4. Handles edge cases and conflicts
    """
    
    @staticmethod
    def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate distance between two coordinates using Haversine formula
        Returns distance in kilometers
        """
        # Radius of Earth in kilometers
        R = 6371.0
        
        # Convert degrees to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        
        # Differences
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        distance = R * c
        return distance
    
    @staticmethod
    def is_driver_available(driver, booking_datetime: datetime, driver_bookings: List) -> bool:
        """
        Check if driver is available at the requested time
        Considers a 2-hour buffer for each booking
        """
        for existing_booking in driver_bookings:
            if existing_booking.status in ["Cancelled"]:
                continue
                
            try:
                existing_datetime = datetime.strptime(
                    f"{existing_booking.booking_date} {existing_booking.booking_time}",
                    "%Y-%m-%d %H:%M"
                )
                
                # Check if bookings overlap (within 2 hours)
                time_diff = abs((booking_datetime - existing_datetime).total_seconds() / 3600)
                if time_diff < 2:
                    return False
            except (ValueError, TypeError):
                continue
        
        return True
    
    @staticmethod
    def find_best_driver(drivers: List, booking, driver_bookings_map: dict) -> Optional[Tuple]:
        """
        Find the best available driver for a booking
        Returns: (driver, distance) or None if no driver available
        
        Algorithm:
        1. Filter available drivers (not busy at booking time)
        2. Calculate distance from each driver to pickup location
        3. Sort by distance (nearest first)
        4. Return the nearest driver
        """
        try:
            booking_datetime = datetime.strptime(
                f"{booking.booking_date} {booking.booking_time}",
                "%Y-%m-%d %H:%M"
            )
        except (ValueError, TypeError):
            return None
        
        available_drivers = []
        
        for driver in drivers:
            # Get driver's bookings
            driver_bookings = driver_bookings_map.get(driver.user_id, [])
            
            # Check if driver is available
            if DriverAssignmentAlgorithm.is_driver_available(driver, booking_datetime, driver_bookings):
                # Calculate distance to pickup location
                distance = DriverAssignmentAlgorithm.calculate_distance(
                    driver.latitude, driver.longitude,
                    booking.pickup_lat, booking.pickup_lon
                )
                available_drivers.append((driver, distance))
        
        # Sort by distance (nearest first)
        if available_drivers:
            available_drivers.sort(key=lambda x: x[1])
            return available_drivers[0]  # Return nearest driver
        
        return None
    
    @staticmethod
    def assign_driver_to_booking(booking, drivers: List, driver_bookings_map: dict) -> Optional[str]:
        """
        Automatically assign best available driver to booking
        Returns: driver_id if assigned, None otherwise
        """
        result = DriverAssignmentAlgorithm.find_best_driver(drivers, booking, driver_bookings_map)
        
        if result:
            driver, distance = result
            return driver.user_id
        
        return None
    
    @staticmethod
    def get_driver_recommendations(booking, drivers: List, driver_bookings_map: dict, top_n: int = 5) -> List[Tuple]:
        """
        Get top N recommended drivers for a booking
        Returns: List of (driver, distance, is_available) tuples
        """
        try:
            booking_datetime = datetime.strptime(
                f"{booking.booking_date} {booking.booking_time}",
                "%Y-%m-%d %H:%M"
            )
        except (ValueError, TypeError):
            return []
        
        driver_recommendations = []
        
        for driver in drivers:
            # Get driver's bookings
            driver_bookings = driver_bookings_map.get(driver.user_id, [])
            
            # Check availability
            is_available = DriverAssignmentAlgorithm.is_driver_available(
                driver, booking_datetime, driver_bookings
            )
            
            # Calculate distance
            distance = DriverAssignmentAlgorithm.calculate_distance(
                driver.latitude, driver.longitude,
                booking.pickup_lat, booking.pickup_lon
            )
            
            driver_recommendations.append((driver, distance, is_available))
        
        # Sort by availability (available first) then by distance
        driver_recommendations.sort(key=lambda x: (not x[2], x[1]))
        
        return driver_recommendations[:top_n]

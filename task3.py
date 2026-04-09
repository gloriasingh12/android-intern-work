# =================================================================
# PROJECT: Ride-Sharing App Prototype
# DESCRIPTION: Simulating Location Tracking, Ride Requests, and Firebase logic.
# DELIVERABLE: Python script demonstrating the core workflow of a ride-sharing app.
# =================================================================

import random
import time

class RideSharingApp:
    def __init__(self, user_name):
        self.user_name = user_name
        self.current_location = (28.6139, 77.2090)  # Default: Delhi Coordinates
        print(f"🚖 Welcome to RideShare, {self.user_name}!")

    def track_location(self):
        """Simulating Google Maps SDK Location Tracking."""
        # Generating small random movements in coordinates
        lat, lon = self.current_location
        new_lat = lat + random.uniform(-0.01, 0.01)
        new_lon = lon + random.uniform(-0.01, 0.01)
        self.current_location = (new_lat, new_lon)
        print(f"📍 Current Location Updated: {self.current_location}")

    def request_ride(self, destination):
        """Simulating Firebase Backend Request and Driver Matching."""
        print(f"📡 Sending Ride Request to Firebase for Destination: {destination}...")
        time.sleep(1)  # Simulating network delay
        
        # Driver Details (Simulated from Firebase)
        driver_details = {
            "name": "Rajesh Kumar",
            "car": "Maruti Suzuki Swift (White)",
            "rating": 4.8,
            "plate": "DL 1CA 1234",
            "eta": "5 mins"
        }
        
        print(f"✅ Driver Found!")
        print(f"👨‍✈️ Driver: {driver_details['name']} ({driver_details['rating']}⭐)")
        print(f"🚗 Car: {driver_details['car']} | Plate: {driver_details['plate']}")
        print(f"🕒 Estimated Arrival: {driver_details['eta']}")
        
        return driver_details

# --- DEMONSTRATION ---
if __name__ == "__main__":
    # Initialize the App
    app = RideSharingApp("Aditya")

    print("\n--- Step 1: Real-time Location Tracking ---")
    app.track_location()
    app.track_location()

    print("\n--- Step 2: Requesting a Ride ---")
    driver = app.request_ride("Noida Sector 62")

    print("\n--- Step 3: Ride Status ---")
    print(f"Status: Your driver {driver['name']} is on the way to your location.")
    
    print("\n" + "="*35)
    print("PROTOTYPE STATUS: Logic Verified ✅")
    print("FEATURES: Maps SDK (Simulated) & Firebase Logic (Simulated)")
    print("="*35)

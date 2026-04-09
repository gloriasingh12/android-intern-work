# =================================================================
# PROJECT: Fitness Tracker App Logic
# DESCRIPTION: Tracking steps, distance, and calories using simulated sensors.
# DELIVERABLE: Python script with real-time data visualization logic.
# =================================================================

import time
import random

class FitnessTracker:
    def __init__(self, user_weight_kg=70):
        self.steps = 0
        self.user_weight = user_weight_kg
        self.stride_length = 0.78  # Average step length in meters
        print(f"🏃 Fitness Tracker Active! (User Weight: {self.user_weight}kg)")

    def simulate_step_sensor(self):
        """Simulates Android's Step Counter Sensor data."""
        # Randomly adding steps to simulate walking
        new_steps = random.randint(10, 50)
        self.steps += new_steps
        return new_steps

    def calculate_metrics(self):
        """Calculates distance and calories burned."""
        # Distance = Steps * Stride Length (in meters)
        distance_km = (self.steps * self.stride_length) / 1000
        
        # Calories calculation (Rough formula: 0.04 calories per step)
        calories_burned = self.steps * 0.04
        
        return round(distance_km, 2), round(calories_burned, 1)

    def display_dashboard(self):
        """Visualizes data for the user."""
        dist, cal = self.calculate_metrics()
        print("\n" + "="*30)
        print(f"📊 REAL-TIME DASHBOARD")
        print(f"👟 Steps:    {self.steps}")
        print(f"📍 Distance: {dist} km")
        print(f"🔥 Calories: {cal} kcal")
        
        # Simple text-based progress bar (Target: 10,000 steps)
        progress = min(int((self.steps / 10000) * 20), 20)
        bar = "█" * progress + "░" * (20 - progress)
        print(f"📈 Progress: [{bar}] {int((self.steps/10000)*100)}%")
        print("="*30)

# --- DEMONSTRATION ---
if __name__ == "__

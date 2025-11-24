import time
import math

# --- Data Store 
# The 'fleet' is a dictionary where the key is the vehicle ID.
# Each value is another dictionary containing vehicle details and status.
FLEET = {
    "C101": {"type": "Car", "rate": 3000.00, "status": "Available"},
    "B201": {"type": "Bike", "rate": 1500.00, "status": "Available"},
    "T301": {"type": "Truck", "rate": 10000.00, "status": "Available"}
}

# The 'rentals' dictionary tracks active transactions.
# Key: Vehicle ID. Value: The  timestamp when the rental started.
ACTIVE_RENTALS = {}

def display_vehicles():
    """Displays the current status of all vehicles in the fleet."""
    print("\n--- Available Vehicles ---")
    available_count = 0
    for v_id, data in FLEET.items():
        status = data["status"]
        rate = data["rate"]
        
        if status == "Available":
            print(f"[ID: {v_id}] | Type: {data['type']:<5} | Rate: ₹{rate:,.2f}/hr | Status: AVAILABLE")
            available_count += 1
    
    if available_count == 0:
        print("No vehicles are currently available for rent.")
    print("-" * 40)


def rent_vehicle(vehicle_id, customer_name):
    """Initiates a rental transaction."""
    v_id = vehicle_id.upper()

    if v_id not in FLEET:
        print(f"Error: Vehicle ID '{v_id}' not found.")
        return

    vehicle_data = FLEET[v_id]

    if vehicle_data["status"] == "Rented":
        print(f"Error: Vehicle {v_id} is currently Rented.")
        return

    # Start Transaction: Record the start time (timestamp) and update status
    start_time = time.time()
    
    vehicle_data["status"] = "Rented"
    ACTIVE_RENTALS[v_id] = start_time
    
    print(f"\nSUCCESS! {customer_name} rented {v_id} ({vehicle_data['type']}).")
    print(f"Rental started at timestamp: {int(start_time)}")
    print(f"Hourly rate: ₹{vehicle_data['rate']:,.2f}")


def return_vehicle(vehicle_id):
    """Handles the vehicle return and calculates the bill."""
    v_id = vehicle_id.upper()

    if v_id not in ACTIVE_RENTALS:
        print(f"Error: Vehicle {v_id} was not rented or is already returned.")
        return

    # Get rental details
    start_time = ACTIVE_RENTALS[v_id]
    vehicle_data = FLEET[v_id]
    hourly_rate = vehicle_data["rate"]
    
    end_time = time.time()
    
    # Calculate duration and bill
    duration_seconds = end_time - start_time
    duration_hours = duration_seconds / 3600.0  
    

    billed_hours = math.ceil(duration_hours) 
    
    total_charge = billed_hours * hourly_rate
    
    # Close Transaction
    del ACTIVE_RENTALS[v_id]
    vehicle_data["status"] = "Available"
    
    # Output Billing Statement
    print("\n--- BILLING STATEMENT ---")
    print(f"Vehicle ID: {v_id} ({vehicle_data['type']})")
    print(f"Actual Duration: {duration_seconds:.2f} seconds")
    print(f"Billed Hours (Rounded Up): {billed_hours} hours")
    print(f"TOTAL CHARGE: ₹{total_charge:,.2f}")
    print("-------------------------\n")


# --- Main Application Loop ---

def main():
    print("Welcome to the Vehicle Rental System!")

    while True:
        print("\n--- Menu ---")
        print("1. Show available vehicles")
        print("2. Rent a vehicle")
        print("3. Return a vehicle")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            display_vehicles()

        elif choice == '2':
            display_vehicles()
            v_id = input("Enter Vehicle ID to rent: ").upper()
            c_name = input("Enter Customer Name: ")
            if v_id and c_name:
                rent_vehicle(v_id, c_name)

        elif choice == '3':
            v_id = input("Enter Vehicle ID to return: ").upper()
            if v_id:
                return_vehicle(v_id)

        elif choice == '4':
            print("Thank you! Have a good day.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()


"""
Interactive Vehicle Rental Application
---------------------------------------
This is a real-life style, menu-driven version of the Vehicle Rental
Management System. A person registers themselves as a customer and then
uses a simple numbered menu to browse vehicles, rent one, return it, and
view invoices and rental history.

This file only adds an interactive layer on top of the existing classes
(Vehicle, Customer, Rental, PaymentProcessor, RentalService, Invoice).
No business logic was changed - it simply calls the same methods used
in main.py, driven by user input instead of hard-coded values.
"""

from datetime import date, datetime

from models.vehicle import Car, Bike, Van
from models.customer import Customer
from payment.payment import CardPayment, UPIPayment
from services.rental_service import RentalService
from invoice import Invoice


# --------------------------------------------------
# Setup: create a realistic vehicle fleet
# --------------------------------------------------

def setup_vehicles(rental_service):

    car1 = Car("V101", "KA01AB1234", "Maruti Suzuki", "Swift", 1500)
    car2 = Car("V102", "KA01CD5678", "Hyundai", "Creta", 2800)
    car3 = Car("V103", "KA01EF9012", "Toyota", "Innova Crysta", 3200)

    bike1 = Bike("V104", "KA02AB1111", "Honda", "Activa 6G", 400)
    bike2 = Bike("V105", "KA02CD2222", "Royal Enfield", "Classic 350", 900)
    bike3 = Bike("V106", "KA02EF3333", "Yamaha", "FZ-S", 600)

    van1 = Van("V107", "KA03AB4444", "Maruti Suzuki", "Eeco", 1800, 300)
    van2 = Van("V108", "KA03CD5555", "Tata", "Winger", 3500, 500)

    rental_service.add_vehicle(car1)
    rental_service.add_vehicle(car2)
    rental_service.add_vehicle(car3)
    rental_service.add_vehicle(bike1)
    rental_service.add_vehicle(bike2)
    rental_service.add_vehicle(bike3)
    rental_service.add_vehicle(van1)
    rental_service.add_vehicle(van2)


# --------------------------------------------------
# Registration
# --------------------------------------------------

def register_customer():

    print("\n" + "=" * 55)
    print("        WELCOME TO CITY WHEELS RENTALS")
    print("=" * 55)
    print("Please register with your details to continue.\n")

    while True:

        name = input("Enter your full name        : ").strip()
        email = input("Enter your email address    : ").strip()
        licence_number = input("Enter your licence number   : ").strip()

        customer_id = "CUS" + datetime.now().strftime("%H%M%S")

        try:
            customer = Customer(customer_id, name, email, licence_number)

            print(f"\nRegistration successful! Your Customer ID is {customer_id}.")

            return customer

        except ValueError as e:
            print(f"\nRegistration failed: {e}")
            print("Please enter your details again.\n")


# --------------------------------------------------
# Menu display
# --------------------------------------------------

def show_menu():

    print("\n" + "-" * 55)
    print("MAIN MENU")
    print("-" * 55)
    print("1. View My Registration Details")
    print("2. View / Search Available Vehicles")
    print("3. Rent a Vehicle")
    print("4. View My Active Rentals")
    print("5. Return a Vehicle")
    print("6. Get Invoice")
    print("7. View My Rental History")
    print("8. Exit")
    print("-" * 55)


# --------------------------------------------------
# Option 1: View registration
# --------------------------------------------------

def view_registration(customer):

    print("\nYour Registration Details")
    print("-" * 30)
    print(f"Customer ID     : {customer.customer_id}")
    print(f"Name            : {customer.name}")
    print(f"Email           : {customer.email}")
    print(f"Licence Number  : {customer.licence_number}")


# --------------------------------------------------
# Option 2: View / search vehicles
# --------------------------------------------------

def display_vehicle_list(vehicle_list):

    if len(vehicle_list) == 0:
        print("No vehicles found.")
        return

    for vehicle in vehicle_list:
        vehicle.display_details()


def view_or_search_vehicles(rental_service):

    print("\n1. View All Available Vehicles")
    print("2. Search by Vehicle Type (Car / Bike / Van)")
    print("3. Search by Price Range")

    choice = input("Enter your choice: ").strip()

    print("\nAvailable Vehicles")
    print("-" * 55)

    if choice == "1":
        results = rental_service.search_vehicle()
        display_vehicle_list(results)

    elif choice == "2":
        vehicle_type = input("Enter vehicle type: ").strip()
        results = rental_service.search_vehicle(vehicle_type=vehicle_type)
        display_vehicle_list(results)

    elif choice == "3":
        try:
            min_price = float(input("Enter minimum daily price: Rs. ").strip())
            max_price = float(input("Enter maximum daily price: Rs. ").strip())

        except ValueError:
            print("Please enter valid numbers for price.")
            return

        results = rental_service.search_vehicle(
            min_price=min_price,
            max_price=max_price
        )
        display_vehicle_list(results)

    else:
        print("Invalid choice.")


# --------------------------------------------------
# Payment method selection
# --------------------------------------------------

def choose_payment_method():

    print("\nSelect Payment Method")
    print("1. Card Payment")
    print("2. UPI Payment")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        card_number = input("Enter your 16-digit card number: ").strip()
        is_valid = card_number.isdigit() and len(card_number) == 16
        return CardPayment(is_valid)

    elif choice == "2":
        upi_id = input("Enter your UPI ID (example: name@bank): ").strip()
        is_valid = "@" in upi_id
        return UPIPayment(is_valid)

    else:
        print("Invalid choice. Card payment will be used by default.")
        return CardPayment(True)


# --------------------------------------------------
# Option 3: Rent a vehicle
# --------------------------------------------------

def rent_a_vehicle(rental_service, customer):

    print("\n===== AVAILABLE VEHICLES =====")
    rental_service.display_available_vehicles()

    vehicle_id = input(
        "\nEnter the Vehicle ID you want to rent (or 0 to cancel): "
    ).strip()

    if vehicle_id == "0":
        print("Rental cancelled.")
        return

    vehicle = rental_service.get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        print("Invalid Vehicle ID.")
        return

    if not vehicle.available:
        print("Sorry, this vehicle is currently unavailable.")
        return

    try:
        days = int(input("Enter number of rental days: ").strip())

    except ValueError:
        print("Please enter a valid whole number of days.")
        return

    if days <= 0:
        print("Rental days must be greater than zero.")
        return

    print(
        f"\nEstimated rental amount for {days} day(s): "
        f"Rs. {vehicle.calculate_rental_cost(days):.2f}"
    )

    confirm = input("Proceed with payment? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Rental cancelled.")
        return

    payment_processor = choose_payment_method()

    rental_id = "R" + datetime.now().strftime("%H%M%S")

    try:
        rental_service.rent_vehicle(
            rental_id,
            customer,
            vehicle,
            days,
            payment_processor,
            date.today()
        )

    except Exception as e:
        print(f"\nRental failed: {e}")


# --------------------------------------------------
# Helper: find active rentals for a customer
# --------------------------------------------------

def get_active_rentals(customer):

    active_rentals = []

    for rental in customer.rental_history:

        if rental.status == "Active":
            active_rentals.append(rental)

    return active_rentals


def get_completed_rentals(customer):

    completed_rentals = []

    for rental in customer.rental_history:

        if rental.status == "Completed":
            completed_rentals.append(rental)

    return completed_rentals


# --------------------------------------------------
# Option 4: View active rentals
# --------------------------------------------------

def view_active_rentals(customer):

    active_rentals = get_active_rentals(customer)

    if len(active_rentals) == 0:
        print("\nYou have no active rentals right now.")
        return

    print("\nYour Active Rentals")
    print("-" * 30)

    for rental in active_rentals:
        rental.display_rental_details()
        print("-" * 30)


# --------------------------------------------------
# Option 5: Return a vehicle
# --------------------------------------------------

def return_a_vehicle(rental_service, customer):

    active_rentals = get_active_rentals(customer)

    if len(active_rentals) == 0:
        print("\nYou have no active rentals to return.")
        return

    print("\nYour Active Rentals")
    print("-" * 30)

    for rental in active_rentals:
        print(
            f"Rental ID: {rental.rental_id}  |  "
            f"Vehicle: {rental.vehicle.vehicle_id} "
            f"({type(rental.vehicle).__name__})"
        )

    rental_id = input("\nEnter Rental ID to return: ").strip()

    selected_rental = None

    for rental in active_rentals:
        if rental.rental_id == rental_id:
            selected_rental = rental

    if selected_rental is None:
        print("Invalid Rental ID.")
        return

    date_text = input(
        "Enter actual return date (YYYY-MM-DD), or press Enter for today: "
    ).strip()

    if date_text == "":
        actual_return_date = date.today()

    else:
        try:
            actual_return_date = datetime.strptime(date_text, "%Y-%m-%d").date()

        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    if actual_return_date < selected_rental.start_date:
        print("Return date cannot be before the rental start date.")
        return

    try:
        rental_service.return_vehicle(selected_rental, actual_return_date)

        if actual_return_date > selected_rental.expected_return_date:
            days_exceeded = (
                actual_return_date - selected_rental.expected_return_date
            ).days

        else:
            days_exceeded = 0

        print("\nReturn Summary")
        print("-" * 30)
        print(f"Rental Days        : {selected_rental.days}")
        print(f"Due Date           : {selected_rental.expected_return_date}")
        print(f"Actual Return Date : {selected_rental.actual_return_date}")
        print(f"Days Exceeded      : {days_exceeded}")
        print(f"Base Amount        : Rs. {selected_rental.base_amount:.2f}")
        print(f"Late Fee           : Rs. {selected_rental.late_fee:.2f}")
        print(f"Final Amount       : Rs. {selected_rental.final_amount:.2f}")
        print("\nYou can view the full invoice from Option 6 in the main menu.")

    except Exception as e:
        print(f"\nReturn failed: {e}")


# --------------------------------------------------
# Option 6: Get invoice
# --------------------------------------------------

def get_invoice(customer):

    completed_rentals = get_completed_rentals(customer)

    if len(completed_rentals) == 0:
        print(
            "\nYou have no completed rentals yet. "
            "Return a vehicle first to generate an invoice."
        )
        return

    print("\nYour Completed Rentals")
    print("-" * 30)

    for rental in completed_rentals:
        print(f"Rental ID: {rental.rental_id}  |  Vehicle: {rental.vehicle.vehicle_id}")

    rental_id = input("\nEnter Rental ID to view invoice: ").strip()

    selected_rental = None

    for rental in completed_rentals:
        if rental.rental_id == rental_id:
            selected_rental = rental

    if selected_rental is None:
        print("Invalid Rental ID.")
        return

    invoice = Invoice(selected_rental)
    invoice.display()


# --------------------------------------------------
# Main program loop
# --------------------------------------------------

def main():

    rental_service = RentalService()
    setup_vehicles(rental_service)

    customer = register_customer()

    while True:

        show_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            view_registration(customer)

        elif choice == "2":
            view_or_search_vehicles(rental_service)

        elif choice == "3":
            rent_a_vehicle(rental_service, customer)

        elif choice == "4":
            view_active_rentals(customer)

        elif choice == "5":
            return_a_vehicle(rental_service, customer)

        elif choice == "6":
            get_invoice(customer)

        elif choice == "7":
            customer.display_rental_history()

        elif choice == "8":
            print(
                f"\nThank you for choosing City Wheels Rentals, "
                f"{customer.name}. Goodbye!\n"
            )
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()

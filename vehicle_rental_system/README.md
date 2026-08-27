# Vehicle Rental Management System

## Project Description

This project is a Vehicle Rental Management System developed using Python and Object-Oriented Programming (OOP).

The system allows customers to rent vehicles such as cars, bikes, and vans. It manages vehicle availability, customer information, rental records, payments, vehicle returns, late fees, invoices, and rental history.

## Project Structure

```text
vehicle_rental_system/
│
├── models/
│   ├── __init__.py
│   ├── customer.py
│   ├── rental.py
│   └── vehicle.py
│
├── payment/
│   ├── __init__.py
│   └── payment.py
│
├── services/
│   ├── __init__.py
│   └── rental_service.py
│
├── invoice.py
├── main.py
├── README.md
└── .gitignore

OOP Concepts Used
Encapsulation - Protecting important data using class attributes and methods.
Abstraction - Using abstract classes for Vehicle and PaymentProcessor.
Inheritance - Car, Bike, and Van inherit from Vehicle.
Polymorphism - Different vehicle types implement their own rental cost calculation.
Method Overriding - Child classes provide their own implementation of inherited methods.
Composition - Rental contains customer, vehicle, and payment objects.
Exception Handling - Used for unavailable vehicles, invalid rental duration, and payment failures.
Features
Add and manage vehicles
Support for Car, Bike, and Van
Register customers
Display available vehicles
Search vehicles
Check vehicle availability
Calculate rental cost
Card and UPI payment processing
Confirm rental after successful payment
Return vehicles
Calculate late fees
Generate invoices
Maintain customer rental history
How to Run

Open the project folder in Visual Studio Code.

Open the terminal and run one of the following, depending on which version you want:

**Scripted demonstration (fixed scenario, matches the assignment's mandatory demo):**

python main.py

**Interactive console application (register yourself and use a live menu):**

python interactive_app.py

If python does not work, try python3 instead of python.

### About interactive_app.py

This is a real-life style version of the same system. Instead of hard-coded
customers, you register yourself first (name, email, licence number), and
then use a numbered menu to:

1. View your registration details
2. View or search available vehicles (by type or price range)
3. Rent a vehicle (choose a vehicle, number of days, and pay by Card or UPI)
4. View your active rentals
5. Return a vehicle (enter the actual return date to see the late fee applied)
6. Get the final invoice for a completed rental
7. View your full rental history
8. Exit

It reuses the exact same classes (Vehicle, Customer, Rental, PaymentProcessor,
RentalService, Invoice) as main.py — only the input source changes, from
hard-coded values to input() prompts.
Demonstration

The program demonstrates:

Adding vehicles.
Registering customers.
Displaying available vehicles.
Customer A renting a car for 3 days.
Customer B attempting to rent the same car.
Rejecting the second rental because the vehicle is unavailable.
Processing Customer A's payment.
Returning the car one day late.
Calculating the late fee.
Generating the final invoice.
Making the car available again.
Displaying the customer's rental history.
Requirements
Python 3.x
No external libraries are required.
Author

Vehicle Rental Management System
## Class Diagram

![Vehicle Rental System Class Diagram](CLASS_DIAGRAM.png)

The class diagram shows the inheritance, composition, and associations used in the Vehicle Rental Management System.
### Polymorphism

Polymorphism is used through the `calculate_rental_cost()` method in the `Vehicle` class.

Car, Bike, and Van override this method and provide their own rental cost calculation.

The RentalService can call `vehicle.calculate_rental_cost(days)` without checking the type of vehicle.

This makes the program easier to maintain and allows new vehicle types to be added without changing the existing rental logic.
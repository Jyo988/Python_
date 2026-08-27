from datetime import date, timedelta

from models.vehicle import Car, Bike, Van
from models.customer import Customer
from payment.payment import CardPayment, UPIPayment
from services.rental_service import RentalService
from invoice import Invoice


# --------------------------------------------------
# 1. Create Vehicles
# --------------------------------------------------

car = Car(
    "V101",
    "DL01AB1234",
    "Toyota",
    "Innova",
    2000
)

bike = Bike(
    "V102",
    "DL02CD5678",
    "Yamaha",
    "FZ",
    700
)

van = Van(
    "V103",
    "DL03EF9012",
    "Tata",
    "Winger",
    3000,
    500
)


# --------------------------------------------------
# 2. Create Customers
# --------------------------------------------------

customer_a = Customer(
    "C101",
    "Customer A",
    "customerA@gmail.com",
    "DL1234567890"
)

customer_b = Customer(
    "C102",
    "Customer B",
    "customerB@gmail.com",
    "DL0987654321"
)


# --------------------------------------------------
# 3. Create Rental Service and Add Vehicles
# --------------------------------------------------

rental_service = RentalService()

rental_service.add_vehicle(car)
rental_service.add_vehicle(bike)
rental_service.add_vehicle(van)


# --------------------------------------------------
# 4. Display Available Vehicles
# --------------------------------------------------

print("\n===== AVAILABLE VEHICLES =====")

rental_service.display_available_vehicles()


# --------------------------------------------------
# 5. Search for a Vehicle
# --------------------------------------------------

print("\n===== SEARCH VEHICLE =====")

results = rental_service.search_vehicle(
    vehicle_type="Car"
)

for vehicle in results:
    vehicle.display_details()


# --------------------------------------------------
# 6. Customer A Rents the Car
# --------------------------------------------------

print("\n===== CUSTOMER A RENTAL =====")

start_date = date.today()

rental = rental_service.rent_vehicle(
    "R001",
    customer_a,
    car,
    3,
    CardPayment(),
    start_date
)


# --------------------------------------------------
# 7. Customer B Tries to Rent Same Car
# --------------------------------------------------

print("\n===== CUSTOMER B ATTEMPT =====")

try:

    rental_service.rent_vehicle(
        "R002",
        customer_b,
        car,
        2,
        UPIPayment(),
        start_date
    )

except Exception as e:

    print("Rental failed:", e)


# --------------------------------------------------
# 8. Display Available Vehicles After Rental
# --------------------------------------------------

print("\n===== AVAILABLE VEHICLES AFTER RENTAL =====")

rental_service.display_available_vehicles()


# --------------------------------------------------
# 9. Return Car One Day Late
# --------------------------------------------------

print("\n===== RETURN VEHICLE =====")

actual_return_date = start_date + timedelta(days=4)

rental_service.return_vehicle(
    rental,
    actual_return_date
)


# --------------------------------------------------
# 10. Display Invoice
# --------------------------------------------------

print("\n===== INVOICE =====")

invoice = Invoice(rental)

invoice.display()


# --------------------------------------------------
# 11. Check Vehicle Availability Again
# --------------------------------------------------

print("\n===== VEHICLE STATUS =====")

print(
    "Car available:",
    car.available
)


# --------------------------------------------------
# 12. Display Customer Rental History
# --------------------------------------------------

print("\n===== CUSTOMER A RENTAL HISTORY =====")

customer_a.display_rental_history()
print("\n===== INVALID RENTAL DAYS TEST =====")

try:
    rental_service.rent_vehicle(
        "R002",
        customer_b,
        bike,
        0,
        UPIPayment(),
        start_date
    )

except Exception as e:
    print("Rental failed:", e)

print("\n===== PAYMENT FAILURE TEST =====")

try:
    rental_service.rent_vehicle(
        "R003",
        customer_b,
        bike,
        2,
        CardPayment(False),
        start_date
    )

except Exception as e:
    print("Rental failed:", e)
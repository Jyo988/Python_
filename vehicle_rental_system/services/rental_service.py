from models.rental import Rental


class RentalService:

    def __init__(self):

        self.__vehicles = []
        self.__rentals = []

    def add_vehicle(self, vehicle):

        self.__vehicles.append(vehicle)

    def get_vehicle_by_id(self, vehicle_id):

        for vehicle in self.__vehicles:

            if vehicle.vehicle_id == vehicle_id:
                return vehicle

        return None

    def display_available_vehicles(self):

        print("\nAvailable Vehicles")
        print("-" * 60)

        found = False

        for vehicle in self.__vehicles:

            if vehicle.available:

                vehicle.display_details()
                found = True

        if not found:
            print("No vehicles are currently available.")

    def search_vehicle(self, vehicle_id=None,
                       vehicle_type=None,
                       min_price=None,
                       max_price=None):

        results = []

        for vehicle in self.__vehicles:

            if not vehicle.available:
                continue

            if vehicle_id is not None:
                if vehicle.vehicle_id != vehicle_id:
                    continue

            if vehicle_type is not None:
                if type(vehicle).__name__.lower() != vehicle_type.lower():
                    continue

            if min_price is not None:
                if vehicle.daily_rate < min_price:
                    continue

            if max_price is not None:
                if vehicle.daily_rate > max_price:
                    continue

            results.append(vehicle)

        return results

    def rent_vehicle(self, rental_id,
                     customer, vehicle, days,
                     payment_processor, start_date):

        # 1. Check vehicle availability
        if not vehicle.available:
            raise Exception("Vehicle is unavailable.")

        # 2. Check rental duration
        if days <= 0:
            raise ValueError(
                "Rental days must be greater than zero."
            )

        # 3. Calculate rental amount
        amount = vehicle.calculate_rental_cost(days)

        print(f"\nRental Amount: Rs. {amount:.2f}")

        # 4. Process payment
        payment = payment_processor.process_payment(amount)

        # 5. Payment must succeed before rental confirmation
        if not payment.successful:

            raise Exception(
                "Payment failed. Rental has not been confirmed."
            )

        # 6. Create rental
        rental = Rental(
            rental_id,
            customer,
            vehicle,
            start_date,
            days,
            payment
        )

        # 7. Mark vehicle as unavailable
        vehicle.mark_as_rented()

        # 8. Add rental to customer's history
        customer.add_rental(rental)

        # 9. Store rental in system
        self.__rentals.append(rental)

        print("Payment completed successfully.")
        print("Rental confirmed successfully.")

        return rental

    def return_vehicle(self, rental, actual_return_date):

        if rental.status == "Completed":
            raise Exception("This vehicle has already been returned.")

        rental.complete_rental(actual_return_date)

        print("\nVehicle returned successfully.")

        return rental
from datetime import timedelta


class Rental:

    def __init__(self, rental_id, customer, vehicle,
                 start_date, days, payment):

        if days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        self.__rental_id = rental_id
        self.__customer = customer
        self.__vehicle = vehicle
        self.__start_date = start_date
        self.__days = days

        self.__expected_return_date = (
            start_date + timedelta(days=days)
        )

        self.__actual_return_date = None

        self.__base_amount = vehicle.calculate_rental_cost(days)
        self.__late_fee = 0
        self.__final_amount = self.__base_amount

        self.__payment = payment
        self.__status = "Active"

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def customer(self):
        return self.__customer

    @property
    def vehicle(self):
        return self.__vehicle

    @property
    def start_date(self):
        return self.__start_date

    @property
    def days(self):
        return self.__days

    @property
    def expected_return_date(self):
        return self.__expected_return_date

    @property
    def actual_return_date(self):
        return self.__actual_return_date

    @property
    def base_amount(self):
        return self.__base_amount

    @property
    def late_fee(self):
        return self.__late_fee

    @property
    def final_amount(self):
        return self.__final_amount

    @property
    def payment(self):
        return self.__payment

    @property
    def status(self):
        return self.__status

    def complete_rental(self, actual_return_date):

        self.__actual_return_date = actual_return_date

        if actual_return_date > self.__expected_return_date:

            late_days = (
                actual_return_date - self.__expected_return_date
            ).days

            self.__late_fee = (
            late_days * self.__vehicle.daily_rate +
            late_days * 0.20 * self.__vehicle.daily_rate
            )

        else:
            self.__late_fee = 0

        self.__final_amount = (
            self.__base_amount + self.__late_fee
        )

        self.__status = "Completed"

        self.__vehicle.mark_as_available()

    def display_rental_details(self):

        print(f"Rental ID: {self.rental_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Vehicle: {self.vehicle.vehicle_id}")
        print(f"Start Date: {self.start_date}")
        print(f"Expected Return Date: {self.expected_return_date}")
        print(f"Actual Return Date: {self.actual_return_date}")
        print(f"Base Amount: Rs. {self.base_amount:.2f}")
        print(f"Late Fee: Rs. {self.late_fee:.2f}")
        print(f"Final Amount: Rs. {self.final_amount:.2f}")
        print(f"Status: {self.status}")
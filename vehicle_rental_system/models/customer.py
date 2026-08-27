class Customer:

    def __init__(self, customer_id, name, email, licence_number):

        if customer_id == "":
            raise ValueError("Customer ID cannot be empty.")

        if name == "":
            raise ValueError("Customer name cannot be empty.")

        if email == "":
            raise ValueError("Email cannot be empty.")

        if licence_number == "":
            raise ValueError("Licence number cannot be empty.")

        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__licence_number = licence_number

        self.__rental_history = []

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def licence_number(self):
        return self.__licence_number

    @property
    def rental_history(self):
        return list(self.__rental_history)

    def add_rental(self, rental):
        self.__rental_history.append(rental)

    def display_rental_history(self):

        print("\nRental History")
        print("-----------------------------")

        if len(self.__rental_history) == 0:
            print("No previous rentals.")
            return

        for rental in self.__rental_history:

            print(
                f"Rental ID: {rental.rental_id}"
            )

            print(
                f"Vehicle: {rental.vehicle.vehicle_id}"
            )

            print(
                f"Rental Period: "
                f"{rental.start_date} to {rental.expected_return_date}"
            )

            print(
                f"Status: {rental.status}"
            )

            print("-----------------------------")
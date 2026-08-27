from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_id, registration_number,
                 brand, model, daily_rate):

        if vehicle_id == "":
            raise ValueError("Vehicle ID cannot be empty.")

        if registration_number == "":
            raise ValueError("Registration number cannot be empty.")

        if brand == "":
            raise ValueError("Brand cannot be empty.")

        if model == "":
            raise ValueError("Model cannot be empty.")

        if daily_rate <= 0:
            raise ValueError("Daily rate must be greater than zero.")

        self.__vehicle_id = vehicle_id
        self.__registration_number = registration_number
        self.__brand = brand
        self.__model = model
        self.__daily_rate = daily_rate
        self.__available = True

    @property
    def vehicle_id(self):
        return self.__vehicle_id

    @property
    def registration_number(self):
        return self.__registration_number

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def daily_rate(self):
        return self.__daily_rate

    @property
    def available(self):
        return self.__available

    def mark_as_rented(self):
        self.__available = False

    def mark_as_available(self):
        self.__available = True

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Car(Vehicle):

    def calculate_rental_cost(self, days):
        return self.daily_rate * days

    def display_details(self):
        print(
            f"{self.vehicle_id} | Car | {self.brand} | "
            f"{self.model} | Rs. {self.daily_rate} per day"
        )


class Bike(Vehicle):

    def calculate_rental_cost(self, days):

        amount = self.daily_rate * days

        # 5% discount when rental is more than 5 days
        if days > 5:
            amount = amount * 0.95

        return amount

    def display_details(self):
        print(
            f"{self.vehicle_id} | Bike | {self.brand} | "
            f"{self.model} | Rs. {self.daily_rate} per day"
        )


class Van(Vehicle):

    def __init__(self, vehicle_id, registration_number,
                 brand, model, daily_rate, service_charge):

        super().__init__(
            vehicle_id,
            registration_number,
            brand,
            model,
            daily_rate
        )

        if service_charge < 0:
            raise ValueError("Service charge cannot be negative.")

        self.__service_charge = service_charge

    @property
    def service_charge(self):
        return self.__service_charge

    def calculate_rental_cost(self, days):

        normal_amount = self.daily_rate * days

        return normal_amount + self.service_charge

    def display_details(self):
        print(
            f"{self.vehicle_id} | Van | {self.brand} | "
            f"{self.model} | Rs. {self.daily_rate} per day"
        )
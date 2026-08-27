from abc import ABC, abstractmethod


class Payment:

    def __init__(self, amount, payment_method, successful):

        self.__amount = amount
        self.__payment_method = payment_method
        self.__successful = successful

    @property
    def amount(self):
        return self.__amount

    @property
    def payment_method(self):
        return self.__payment_method

    @property
    def successful(self):
        return self.__successful


class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(PaymentProcessor):

    def __init__(self, payment_successful=True):
        self.__payment_successful = payment_successful

    def process_payment(self, amount):

        if amount <= 0:
            return Payment(
                amount,
                "Card",
                False
            )

        return Payment(
            amount,
            "Card",
            self.__payment_successful
        )


class UPIPayment(PaymentProcessor):

    def __init__(self, payment_successful=True):
        self.__payment_successful = payment_successful

    def process_payment(self, amount):

        if amount <= 0:
            return Payment(
                amount,
                "UPI",
                False
            )

        return Payment(
            amount,
            "UPI",
            self.__payment_successful
        )
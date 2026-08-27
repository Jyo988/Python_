class Invoice:

    def __init__(self, rental):

        self.__rental = rental

    def display(self):

        rental = self.__rental

        print("\n")
        print("=" * 45)
        print("                 FINAL INVOICE")
        print("=" * 45)

        print(f"Customer          : {rental.customer.name}")
        print(f"Vehicle           : {rental.vehicle.vehicle_id}")
        print(f"Vehicle Type      : {type(rental.vehicle).__name__}")
        print(f"Rental Start Date : {rental.start_date}")
        print(f"Expected Return   : {rental.expected_return_date}")
        print(f"Actual Return     : {rental.actual_return_date}")
        print(f"Rental Days       : {rental.days}")

        print("-" * 45)

        print(f"Base Amount       : Rs. {rental.base_amount:.2f}")
        print(f"Late Fee          : Rs. {rental.late_fee:.2f}")

        print("-" * 45)

        print(f"Final Amount      : Rs. {rental.final_amount:.2f}")

        print(f"Payment Method    : {rental.payment.payment_method}")
        print(f"Payment Status    : "
              f"{'Successful' if rental.payment.successful else 'Failed'}")

        print("=" * 45)
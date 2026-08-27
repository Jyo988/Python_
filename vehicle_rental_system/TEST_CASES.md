# Test Cases

## Test Case 1: Display Available Vehicles

**Test ID:** TC01

**Scenario:** Display all available vehicles.

**Expected Result:**  
The system should display the available car, bike, and van.

**Actual Result:**  
The system displayed V101 Car, V102 Bike, and V103 Van.

**Status:** PASS


## Test Case 2: Search Vehicle by Type

**Test ID:** TC02

**Scenario:** Search for a vehicle using the vehicle type "Car".

**Expected Result:**  
The system should display the available car.

**Actual Result:**  
The system displayed V101, Toyota Innova.

**Status:** PASS


## Test Case 3: Successful Vehicle Rental

**Test ID:** TC03

**Scenario:** Customer A rents the car for 3 days.

**Expected Result:**  
The system should calculate the rental amount, process payment successfully, and confirm the rental.

**Actual Result:**  
Rental amount was Rs. 6000.00. Payment was completed successfully and the rental was confirmed.

**Status:** PASS


## Test Case 4: Rent an Unavailable Vehicle

**Test ID:** TC04

**Scenario:** Customer B attempts to rent the same car while it is already rented.

**Expected Result:**  
The system should reject the rental and display a vehicle unavailable message.

**Actual Result:**  
The system displayed "Vehicle is unavailable."

**Status:** PASS


## Test Case 5: Late Vehicle Return

**Test ID:** TC05

**Scenario:** Customer A returns the car one day after the expected return date.

**Expected Result:**  
The system should calculate the late fee and final amount.

**Actual Result:**  
Base amount was Rs. 6000.00, late fee was Rs. 400.00, and final amount was Rs. 6400.00.

**Status:** PASS


## Test Case 6: Returned Vehicle Becomes Available

**Test ID:** TC06

**Scenario:** Check the car availability after it is returned.

**Expected Result:**  
The returned car should become available again.

**Actual Result:**  
The system displayed "Car available: True".

**Status:** PASS


## Test Case 7: Customer Rental History

**Test ID:** TC07

**Scenario:** Display Customer A's rental history after completing the rental.

**Expected Result:**  
The system should display the completed rental record.

**Actual Result:**  
The system displayed rental R001 with vehicle V101 and status "Completed".

**Status:** PASS
## Test Case 8: Invalid Rental Duration

**Test ID:** TC08

**Scenario:** Attempt to rent a vehicle for 0 days.

**Expected Result:**  
The system should reject the rental.

**Actual Result:**  
The system displayed "Rental days must be greater than zero."

**Status:** PASS


## Test Case 9: Payment Failure

**Test ID:** TC09

**Scenario:** Attempt a rental using a payment processor that reports payment failure.

**Expected Result:**  
The rental should not be confirmed.

**Actual Result:**  
The system displayed "Payment failed. Rental has not been confirmed."

**Status:** PASS
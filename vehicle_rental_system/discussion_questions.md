# Discussion Questions

## 1. Why should Vehicle be abstract?

`Vehicle` describes attributes and behaviour every rentable vehicle shares (ID, registration number, brand, model, daily rate, availability), but "a vehicle" on its own is never actually rented — only a specific kind of vehicle is. Making it abstract prevents anyone from creating a bare `Vehicle` object with no real rental rule, and forces every subclass (`Car`, `Bike`, `Van`) to supply its own `calculate_rental_cost()` and `display_details()`. It also documents the contract new vehicle types must follow.

## 2. How does polymorphism remove vehicle-type conditionals?

Without polymorphism, `RentalService` would need something like `if vehicle_type == "Car": ... elif vehicle_type == "Bike": ...` every time it calculated a price. Instead, `RentalService` simply calls `vehicle.calculate_rental_cost(days)`. Python calls whichever version of that method belongs to the actual object at runtime — `Car`'s, `Bike`'s, or `Van`'s — so the calling code never needs to know or check the type.

## 3. Why should vehicle and customer fields remain private?

Private fields (`__daily_rate`, `__rental_history`, etc.) stop other parts of the program from changing critical data directly and skipping validation — for example, setting a negative daily rate or emptying a customer's rental history by mistake. Access is only allowed through controlled properties and methods (`mark_as_rented()`, `add_rental()`), so the class itself always stays responsible for keeping its own data valid.

## 4. What is the relationship between Rental, Customer, and Vehicle?

`Rental` is composed of a `Customer`, a `Vehicle`, and a `Payment` — it holds direct references to all three and cannot exist meaningfully without them. This is composition: a `Rental` object owns and coordinates these pieces to represent one rental transaction. Separately, `Customer` has an association with `Rental` through `rental_history`, since one customer can be linked to many rentals over time.

## 5. How can a new vehicle type be added without changing existing classes?

Create a new subclass of `Vehicle` (for example, `Truck`) and implement `calculate_rental_cost()` and `display_details()` for it. Because `RentalService`, `Rental`, and `Invoice` only ever interact with vehicles through the shared `Vehicle` interface, none of that existing code needs to change — the new class simply plugs into the existing polymorphic calls. This follows the open/closed principle: the system is open to extension but closed to modification.

## 6. What should happen when payment processing fails?

The rental must not be confirmed. In this system, `RentalService.rent_vehicle()` checks `payment.successful` right after calling `process_payment()`, and raises an exception ("Payment failed. Rental has not been confirmed.") before the vehicle is marked unavailable or the rental record is created. This guarantees the business rule "payment must complete successfully before the rental is confirmed" always holds, even if the failure happens partway through the workflow.

## 7. Which parts of the solution demonstrate composition?

`Rental` is the clearest example — it holds direct references to a `Customer`, a `Vehicle`, and a `Payment`, and none of those objects are optional; a `Rental` is only meaningful as a combination of all three. `Invoice` is a second example, since it is built directly from a `Rental` object and reads its data to produce the printed invoice.

## 8. How would the model change if one booking could contain multiple vehicles?

`Rental` currently holds a single `Vehicle` reference. To support multiple vehicles per booking, `Rental` would need to hold a list of vehicles (or a list of smaller `RentalLineItem` objects, each pairing one vehicle with its own cost) instead of one `vehicle` field. `calculate_rental_cost()`, the late-fee logic, and `Invoice.display()` would then need to loop over that list and sum the totals, rather than reading a single vehicle's values directly. `RentalService.rent_vehicle()` would also need to check availability and mark every vehicle in the booking, not just one.

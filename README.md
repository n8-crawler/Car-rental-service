# test
Your task is to implement a small part of business logic along with associated test cases that verify that the logic works according to the specification below

Specification
Rental cars are divided into three categories:
1. Compact
2. Premium
3. Minivan
It should be possible to add more categories later.

A reservation is identified by a unique reservation number. Each rental refers to a car at one time, meaning if the car is already hired it is not available for rent during that time. Rental price is calculated according to formulas depending on the category. The price for BaseDayRental and KilometerPrice (Price per kilometre) and this price is the same for all categories.

1. Compact Price = baseDayRental * numberOfDays
2. Premium Price = baseDayRental * numberOfDays * 1.2 + kilometerPrice * numberOfKilometers
3. Minivan Price = baseDayRental * numberOfDays * 1.7 + (kilometerPrice * numberOfKilometers * 1.5 )


Use Cases 

The two following use cases should be implemented.

U1. Rental registration When a customer rents a car it should get registered in the system with an appropriate response. The following data should be stored:
1. Booking number
2. Customer name
4. Car category
5. Time and date for the rental
6. Car mileage in kilometres (at pick up)

U2. Car Return The system should be able to handle car return using the following details:
1. Booking number
2. Time and date for the return
3. Current mileage of the car in kilometres (upon return)
Upon return of a car the system calculates and responses with the price for the rental period according to the formulas specified above.

from Customer import Customer
from Restaurant import Restaurant
from Review import Review

# Create customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
customer3 = Customer("stanley","kamau ")
print (customer1.__dict__, customer2.__dict__)
# changing names
customer1.name = ("stanley")
customer1.family_name=("muiruri")
customer2.name = ("Grace")
customer2.family_name = ("wanjiru")
print (customer1.__dict__, customer2.__dict__)
#print full customer name
print (customer1.full_name())


print("\nCustomer class instances")
for customer in Customer.all():
    print(customer.full_name())

# Create restaurants
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")
print(restaurant1._name, restaurant2._name)
#trying to change the restaurant name
# restaurant1.name = "small villa"
# print( restaurant1._name)

# Customers add reviews for restaurants
review1 = customer1.add_review(restaurant1, "Good experience", 4)
review2 = customer1.add_review(restaurant2, "Excellent service", 5)
review3 = customer2.add_review(restaurant1, "Average", 3)

# Print customer information
print("All Customers:")
for customer in Customer.all():
    print(f"{customer.full_name()} - Number of Reviews: {customer.num_reviews()}")

# Print restaurant information
print("\nAll Restaurants:")
for restaurant in Restaurant.all():
    print(f"{restaurant.name} - Average Rating: {restaurant.average_star_rating()}")

# Print reviews for a specific restaurant
print(f"\nReviews for {restaurant1.name}:")
for review in restaurant1.reviews():
    print(f"{review.customer().full_name()}: {review.review_name()} - Rating: {review.rating()}")

print("\n find by name:")
found_customer = Customer.find_by_name("stanley muiruri")

# Check the result
if found_customer:
    print(f"Customer found: {found_customer.full_name()}")
else:
    print("Customer not found.")


found_customers = Customer.find_all_by_given_name("stanley")


print("\n find all by given name:")
# Check the result
if found_customers:
    print("Customers found:")
    for customer in found_customers:
        print(f"  {customer.name} {customer.family_name}")
else:
    print("No customers found.")


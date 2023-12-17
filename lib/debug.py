from Customer import Customer
from Restaurant import Restaurant
from Review import Review

# Create customers
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Create restaurants
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Customers add reviews for restaurants
review1 = customer1.add_review(restaurant1, "Good experience", 4)
review2 = customer1.add_review(restaurant2, "Excellent service", 5)
review3 = customer2.add_review(restaurant1, "Average", 3)

# Print customer information
print("All Customers:")
for customer in Customer.all():
    print(f"{customer.full_name} - Number of Reviews: {customer.num_reviews()}")

# Print restaurant information
print("\nAll Restaurants:")
for restaurant in Restaurant.all():
    print(f"{restaurant.name} - Average Rating: {restaurant.average_star_rating()}")

# Print reviews for a specific restaurant
print(f"\nReviews for {restaurant1.name}:")
for review in restaurant1.reviews():
    print(f"{review.customer().full_name()}: {review.review_name()} - Rating: {review.rating()}")

print(Customer.all_customers)
print(Restaurant.customers)

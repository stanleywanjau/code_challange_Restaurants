from Customer import Customer
from Restaurant import Restaurant

class Review:
    all_reviews = []

    def __init__(self, rating, customer, restaurant):
        self.customer = customer
        self.restaurant = restaurant
        self.rate = rating

    def rating(self):
        return self.rate
    def customer(self):
        return self.customer
    def restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews

    @classmethod
    def create_review(cls, customer, restaurant, rate):
        new_review = cls(rate, customer, restaurant)
        cls.all_reviews.append(new_review)
        return new_review

# Example usage:

# Assuming you have instances of Customer and Restaurant classes
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Example Restaurant")

# Create some reviews
review1 = Review.create_review(customer1, restaurant1, 4)
review2 = Review.create_review(customer1, restaurant1, 5)

# Print information for all reviews
for review in Review.all():
    print(f"Review Rating: {review.rating()}, Customer Data: {review.customer.__dict__}, Restaurant Data: {review.restaurant.__dict__}")

# Alternatively, you can also print the list of reviews directly
print(Review.all())

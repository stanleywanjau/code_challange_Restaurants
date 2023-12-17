class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, name, rating):
        self.customer_obj = customer
        self.restaurant_obj = restaurant
        self.name = name
        
        self.rating_value = rating
        Review.all_reviews.append(self)
        restaurant.reviews_list.append(self)

    def rating(self):
        return self.rating_value
    
    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self.customer_obj

    def restaurant(self):
        return self.restaurant_obj

    def review_name(self):
        return self.name

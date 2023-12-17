class Review:
    all_reviews = []

    def __init__(self, rating, customer, restaurant):
        self._customer_obj = customer
        self._restaurant_obj = restaurant
        self.rate = rating
        self.all_reviews.append(self)

    def rating(self):
        return self.rate

    @classmethod
    def all(cls):
        return cls.all_reviews
    
    def customer(self):
        return self._customer_obj
     
    def restaurant(self):
        return self._restaurant_obj

    


from Review import Review

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        self.reviews_list = []
        Restaurant.all_restaurants.append(self)
        
    @property
    def name(self):
        return self._name
    

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        return self.reviews_list

    def customers(self):
        return list(set([review.customer() for review in self.reviews_list if review.customer()==self]))

    def average_star_rating(self):
        if not self.reviews_list:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews_list])
        return total_ratings / len(self.reviews_list)

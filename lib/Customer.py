from Review import Review  

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def num_reviews(self):
        return len([review for review in Review.all() if review.customer() == self])
        
                               

    @classmethod
    def find_by_name(cls, name):
       for customer in cls.all_customers:
        if customer.full_name() == name:
            return customer
        return None
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]

    def restaurants(self):
        return list(set([review.restaurant() for review in Review.all() if review.customer() == self]))

    def add_review(self, restaurant, name, rating): 
      new_review = Review(self, restaurant, name, rating)  
      return new_review
# print(restaurants())
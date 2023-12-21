from Review import Review  

class Customer:
    all_customers = []

    def __init__(self, name, family_name):
        self._name = name
        self._family_name = family_name
        Customer.all_customers.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def family_name(self):
        return self._family_name
    @family_name.setter
    def family_name(self, family_name):
        self._family_name = family_name

    def full_name(self):
        return f"{self._name} {self._family_name}"

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
        return [customer for customer in cls.all_customers if customer.name == name]

    def restaurants(self):
        return list(set([review.restaurant() for review in Review.all() if review.customer() == self]))

    def add_review(self, restaurant, name, rating): 
      new_review = Review(self, restaurant, name, rating)  
      return new_review
# print(restaurants())
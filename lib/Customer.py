from Review import Review 
class Customer:
  all_customers=[]
  def __init__(self,name,f_name):
    self.name = name
    self.f_name = f_name
    Customer.all_customers.append(self)
  

  def given_name(self):
    return self.name
  def family_name(self):
    return self.f_name
  def full_name(self):
    return(f"({self.name} {self.f_name})")
  @classmethod
  def all(cls):
    return cls.all_customers
  def restaurant(self):
     return list(set([review.restaurant() for review in Review.all() if review.customer() == self]))
  def add_review(self, restaurant,rating):
    new_review = Review(self, restaurant, rating)
    return new_review
    
  

  pass

stanley = Customer("stanley","muiruri")
muiruri=Customer("mark","muiruri")
# print (full_name())
# stanley.full_name()
# # print(all())
# Customer.show_customer()
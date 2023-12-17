class Restaurant:
  all_restraurant=[]
  def __init__(self,name):
    self._name = name
    self.review_list = []
    self.all_restraurants.append(self)
  def name(self):
     return self._name
  
  
  def review(self):
    return self.review_list
  def customers(self):
    return list(set(review.customers()for review in self.review_list))
    pass
  

  pass
# mac=Restaurant("Restaur")
# print(mac.get_name())
# mac=Restaurant("Res")
# print(mac.get_name())
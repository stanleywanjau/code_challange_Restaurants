class Restaurant:
  def __init__(self,name):
    self.name = name
  def name(self):
    if type(self.name)==str:
      return self.name
  
  def get_name(self):
    return self.name
  

  pass
# mac=Restaurant("Restaur")
# print(mac.get_name())
# mac=Restaurant("Res")
# print(mac.get_name())
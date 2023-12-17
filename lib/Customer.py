class Customer:
  all=[]
  def __init__(self,name,f_name):
    self.name = name
    self.f_name = f_name
    full_name = f"{name} {f_name}"
    self.add_customer_to_all(full_name)
  # def test_drive(self):
  #    print(f"({self.name} {self.f_name})")

  def given_name(self):
    return self.name
  def family_name(self):
    return self.f_name
  def full_name(self):
    return(f"({self.name} {self.f_name})")
  @classmethod
  def add_customer_to_all(cls,full_name):
    cls.all.append(full_name)
  @classmethod
  def show_customer(cls):
    print(cls.all)

  pass

stanley = Customer("stanley","muiruri")
muiruri=Customer("mark","muiruri")
# print (full_name())
# stanley.full_name()
# # print(all())
# Customer.show_customer()
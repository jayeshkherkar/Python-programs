class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)
class address:
    def __init__(self,city,pin,state):
        self.__city = city         # Private member of address class.
        self.pin = pin
        self.state = state
    def get_city(self):           # get function to access the private member of address class.
        return self.__city
    def edit_address(self,new_city,new_pin,new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state

add1 = address('Indore',42006,'Madhyapradesh')
C1 = Customer('Jayesh','Male',add1)
C1.print_address()
C1.edit_profile('Om','Dadar',4200100,'Mumbai')
C1.print_address()

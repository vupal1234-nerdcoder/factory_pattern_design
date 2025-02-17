# class car:
#   def drive(self):
#     return "Car is running"
  
# class bus:
#   def drive(self):
#     return "Bus is running"
  
# vechile = bus()
# print(vechile.drive()) 
# This code is normal form

# apply facoty pattern

# class Bus:
#   def drive(self):
#     return 'Bus is running'
  
# class Bike:
#   def drive(self):
#     return 'Bike is running'
  
# class VehicleFactory:
#   @staticmethod
#   def get_vechile(vechile_name):
#     vechile ={"bus" :Bus,"bike" :Bike}
#     return vechile.get(vechile_name,lambda :"This is wrong type vechile")()
  
# vechile =VehicleFactory.get_vechile("bus")
# print(vechile.drive())

# abstract factory pattern


# from abc import ABC,abstractmethod
# class Vechile(ABC):
#   @abstractmethod
#   def drive(self):
#     pass

# class Bus(Vechile):
#   def drive(self):
#     return "Bus is running"
  
# class Bike(Vechile):
#   def drive(self):
#     return "Bike is running"
  
# # apply abstact factory method
# class VechicleFactory(ABC):
#   @abstractmethod
#   def create_vechile(self):
#     pass

# class BusFactory(VechicleFactory):
#   def create_vechile(self):
#     return Bus()
# class BikeFactory(VechicleFactory):
#   def create_vechile(self):
#     return Bike()
  


# factory =BusFactory()
# bus =factory.create_vechile()
# print(bus.drive())

  
import math
# another example of factory example

class Circle:
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return f'Circle area : {math.pi * self.radius *self.radius}'
    
class Square:
  def __init__(self,a):
    self.a=a
  def area(self):
    return f' Square area: {self.a*self.a}' 
    
  
class Rectangle:
  def __init__(self,length,width):
    self.length =length
    self.width= width

  def area(self):
    return f' Rectangular area: {self.length *self.width}' 
  
class Shapefactory:
  @staticmethod
  def get_shape(shape_type,*args):
    shapes ={
        "circle": Circle,
        "rectangle" :Rectangle,
        "square" :Square
    }
    return shapes.get(shape_type,lambda *args :"shape is wrong")(*args)
  

shape = Shapefactory.get_shape('circle',5)
print(shape.area())


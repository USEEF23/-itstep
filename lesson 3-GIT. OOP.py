class BMW:
  price=11000
  horsePower=25000
  engine=2.0
  petrol="gasoline"
  breakTime=7
  breakDistance=9
  maxTemp=100
class Toyota:
  price=160000
  horsePower=40000
  engine=2.5
  petrol="disel"
  breakTime=20
  breakDistance=27
  maxTemp=200
class Mercedes:
  price=1500000
  horsePower=60000
  engine=3.7
  petrol="premium gasoline"
  breakTime=40
  breakDistance=50
  maxTemp=150
class Chevrolet:
  price=78000
  horsePower=50000
  engine=2.1
  petrol="gasoline"
  breakTime=10
  breakDistance=13
  maxTemp=100
mat=input("Enter material: ")
type=input("Enter car BMW/Mercedes/Toyota/Chevrolet: ")
if type=="BMW":
  print(mat,type)
  print("price",BMW.price)
  print("horse power",BMW.horsePower)
  print("engine",BMW.engine)
  print("petrol",BMW.petrol)
  print("break time",BMW.breakTime)
  print("break distance",BMW.breakDistance)
  print("max temp",BMW.maxTemp)
elif type=="Mercedes":
  print(mat,type)
  print("price",Mercedes.price)
  print("horse power",Mercedes.horsePower)
  print("engine",Mercedes.engine)
  print("petrol",Mercedes.petrol)
  print("break time",Mercedes.breakTime)
  print("break distance",Mercedes.breakDistance)
  print("max temp",Mercedes.maxTemp)
elif type=="Toyota":
  print(mat,type)
  print("price",Toyota.price)
  print("horse power",Toyota.horsePower)
  print("engine",Toyota.engine)
  print("petrol",Toyota.petrol)
  print("break time",Toyota.breakTime)
  print("break distance",Toyota.breakDistance)
  print("max temp",Toyota.maxTemp)
elif type=="Chevrolet":
  print(mat,type)
  print("price",Chevrolet.price)
  print("horse power",Chevrolet.horsePower)
  print("engine",Chevrolet.engine)
  print("petrol",Chevrolet.petrol)
  print("break time",Chevrolet.breakTime)
  print("break distance",Chevrolet.breakDistance)
  print("max temp",Chevrolet.maxTemp)
else:
  print("Please select from catalog")
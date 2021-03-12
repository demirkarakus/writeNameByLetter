#Write a name letters
def letters():
  name = input("Please, Write Your Name : ")

  count=0
  while count < len(name):
    print(name[count])
    count+=1
  else:
    print("Everything Ok")


#Finding of prime numbers like 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
def primeNumbers():
  numbers = input("Please, Write a Numner")

  count = 0
  for num in range(2,int(numbers)):
    if (int(numbers)%num==0):
      count+=1
      break
  if (count!=0):
    print("The number is not prime.")
  else:
    print("The number is prime")

#Find leap of Year
def leapYear(year):
  leap=False
  if year%400==0 or (year%4==0 and year%100!=0):
    leap=True
    return leap

def daysOfYear(month,day,year):
  days=[31,28,31,30,31,30,31,31,30,31,30,31]
  if leapYear(year):
    days[1]=29
  
  order=0
  for i in range(month-1):
    order+=days[i]
  order+=day
  print(order)

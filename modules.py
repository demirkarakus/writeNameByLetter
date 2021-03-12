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


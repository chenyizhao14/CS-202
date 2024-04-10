def weight_on_planets():
   weight = float(input("What do you weigh on earth? \n"))

   mWeight = weight * 0.38
   jWeight = weight * 2.34

   print (f"On Mars you would weigh {mWeight} pounds.\n" +
         f"On Jupiter you would weigh {jWeight} pounds.")

   
if __name__ == '__main__':
   weight_on_planets()
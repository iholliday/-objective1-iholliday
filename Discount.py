#Discount investigation (variables and constants)

#subroutine to calculate price
def Discount (Total, Rate):
  return Total - (Total * Rate/100)

#main program
print(Discount(55, 20))
#Fish Tank Volume Problem

#subroutine for volume
def volume(l,d,h):
  return l * d * h / 1000

#main program
l = 100
d = 6
h = 20
print ('The fish tank is',volume(l,d,h), 'litres')
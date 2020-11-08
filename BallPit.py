#ball pit problem

#function for volume of ball pit
def Vpit(r,h):
  return pi * r * r * h 

#function for volume of a ball
def Vball(r):
  return 4/3 * pi * r ** 3

#function for number of balls to fill a pit
def numBalls(Vpit,Vball):
  return Vpit / Vball * 0.75

#main program
#(a constant:)
pi = 3.14
#inputs:
Rpit = 1
Hpit = 0.2
Rball = 0.05
#processes:
Vpit = Vpit(Rpit,Hpit)
Vball = Vball(Rball)
numBalls = numBalls(Vpit,Vball)
#outputs:
print(' Volume of pit:',Vpit)
print(' Volume of a ball:',Vball)
print('>Number of balls to fill the pit:',numBalls)
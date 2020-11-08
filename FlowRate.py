#Flow rate investigation (variables and constants)

#Original
#subroutine for flow rate of heart
def FlowRate(Volume, Time):
  return Volume / Time

#main program
Volume = 330
Time = 4
Heart = FlowRate(Volume, Time)
print('The flow rate of the human heart is', Heart, 'ml/s')


#Modified
#subroutine for flow rate of heart
def FlowRate(Volume, Time):
  return Volume / Time * 60

#main program
Volume = 100
Time = 30
Heart = FlowRate(Volume, Time)
print('The flow rate of the human heart is', Heart, 'mL/hr')
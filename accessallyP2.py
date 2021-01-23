# Get input


# Function to see how much is left depending on units and patients left
def unitsLeft(j,i):
  m = min(available[i],patients[j])
  available[i]-=m
  patients[j] -=m
  return m

def positivePatients():
  unitsOfBlood = 0
  #O Pos. Case
  unitsOfBlood += unitsLeft(1,1)
  unitsOfBlood += unitsLeft (1,0)

  #A Pos. Case
  for x in range(3,-1,-1):
    unitsOfBlood += unitsLeft(3,x)

  #B Pos. Case
  unitsOfBlood += unitsLeft(5,5)
  unitsOfBlood += unitsLeft(5,4)
  unitsOfBlood += unitsLeft(5,1)
  unitsOfBlood += unitsLeft(5,0)
  #AB Pos. Case
  for x in range(7,-1,-1):
    unitsOfBlood += unitsLeft(7,x)
  return unitsOfBlood

def negativePatients():
  unitsOfBlood = 0
  #A Negative
  unitsOfBlood += unitsLeft(2,2)
  unitsOfBlood += unitsLeft(2,0)

  #B Negative
  unitsOfBlood += unitsLeft(4,4)
  unitsOfBlood += unitsLeft(4,0)

  #O Negative patients
  unitsOfBlood += unitsLeft(0,0)

  #AB Negative
  for x in range(6,-1,-2):
    unitsOfBlood += unitsLeft(6,x)

  return unitsOfBlood

inputAvailable = map(int,input().split())
patientsInput = map(int,input().split())
available = [inputAvailable[i] for i in range(len(list(inputAvailable)))]
patients = [patientsInput[i] for i in range(len(list(patientsInput)))]

s = positivePatients() + negativePatients()
available = inputAvailable
patients = patientsInput
s1 = negativePatients() + positivePatients()
print(max(s,s1))

#Q1: Favourite Times
duration = int(input("Input:"))
hour = 12
minutes = 0
curr = 0

for i in range (duration):
  minutes = int(minutes)
  hour = int(hour)
  minutes += 1
  if minutes >= 60:
    minutes -= 60
    if hour + 1 < 13:
      hour += 1
    else:
      hour = (hour + 1) % 12
  if minutes < 10:
    minutes = "0" + str(minutes)
  else:
    minutes = minutes
  minutes = str(minutes)
  hour = str(hour)
  time = hour + minutes
  first = int(time[2]) - int(time[1])
  secondVal = int(time[1]) - int(time[0])
  if len(time) == 3:
    if (first == secondVal):
      curr += 1
  else:
    if ((int(time[3]) - int(time[2])) == first) and (first == secondVal):
      curr += 1

print(curr)

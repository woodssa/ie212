#inputting library np with a reference of np
import numpy as np

#putting our HW2data.csv into an array called data, skipping the first row of labesl
data = np.loadtxt("HW2data.csv", delimiter=",", dtype=float, skiprows=1)

#sum of total seats in our data array, where total seats are in column 2
totalSeats = sum(data[ :, 1])
#converting total seats into an integer, you can't have part of a seat
totalSeats = int(totalSeats)

#average flight time where flight time is in column 3
avgFlight = np.mean(data[ :, 2])
#rounding into a more visually reasonable number
avgFlight = round(avgFlight, 2)

#minimum of total flight attendants
minAttend = np.min(data[ :, 3])
#converting minimum attendants into an integer, you can't have part of an attendant
minAttend = int(minAttend)

#maximum of total flight attendants
maxAttend = np.max(data[ :, 3])
#converting maximum attendants into an integer, you can't have part of an attendant
maxAttend = int(maxAttend)

print("There are", totalSeats, "total seats and the average flight time is", avgFlight, "hours.")
print("The minimum number of flight attendants is", minAttend, "and the maximum is", maxAttend,".")
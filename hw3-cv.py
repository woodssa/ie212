#inputting library np with a reference of np
import numpy as np
import math
import sys

#instructions
print('This program will return sample Coefficient of Variation, sample average, sample standard deviation, and relative variability of inputted observed assembly times.')
print("\n1. Include all observed assembly times in a file titled 'Input.csv'")
print('\n2. Save the CSV file in the same folder as this program, then run this program.')

input("\nWhen completed, press Enter to run the program!")
#checking input for valid entries and putting into an array called data
while True:
    try:
        data = np.loadtxt("Input.csv", delimiter=",", dtype=float, encoding='utf-8-sig')
        break
    except ValueError:
        print('\nInvalid input. Please try again.')
        #ends program if invalid input provided 
        sys.exit()

#determine sample average from data array of input assembly times and return that value
def sample_average(data):
    return np.mean(data)

#determine sample standard deviation from data array of input assembly times and return that value
def sample_standard(data):
    #ddof is degrees of freedom since std is population std dev by default    
    return np.std(data, ddof=1)

#determine coefficient of variation from calculated sample std dev and average and return that value
def sample_coefficient(sampleStandard, sampleAverage):
    return sampleStandard/sampleAverage

#determine relative variability from calculated sample coefficient and return that string
def relative_variability(sampleCoefficient):
    if sampleCoefficient < 0.75:
        relativeVariability = "Low"
    elif 0.75 <= sampleCoefficient <= 1.33:
        relativeVariability = "Medium"
    else:
        relativeVariability = "High"
    return relativeVariability

#defining the variables
sampleAverage = sample_average(data)
sampleStandard = sample_standard(data)
sampleCoefficient = sample_coefficient(sampleStandard, sampleAverage)
relativeVariability = relative_variability(sampleCoefficient)

#printing the results
print('\nCoefficient of Variation:', round(sampleCoefficient,2), '\nSample Average:', round(sampleAverage,2), '\nSample Standard Deviation:', round(sampleStandard,2))
print('\n\nRelative Variability:', relativeVariability)
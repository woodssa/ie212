import numpy as np
import pandas as pd
import sys

#instructions to inform user what the program does and the deliverable options
print("This program will report the summary statistics for a maximum of six deliverables of the course.")
print("\n There are 6 deliverable options, labelled: HW1, HW2, HW3, Midterm, Final, and Project")
print("\n The calculated summary statistics are: Average, Median, Highest, Lowest, and Sample Standard Deviation \n")

#function to read data from csv file
def read_csv():
    data = pd.read_csv("HW5data.csv")
    return data
    
#function that calculates summary statistics for given set of data
def calculate_statistics(deliverable_data):
    statistics = {}
    statistics["Average"] = np.mean(deliverable_data)
    statistics["Median"] = np.median(deliverable_data)
    statistics["Highest"] = np.max(deliverable_data)
    statistics["Lowest"] = np.min(deliverable_data)
    statistics["St Dev"] = np.std(deliverable_data, ddof=1)
    
    #rounding statistic to one decimal place
    for key, value in statistics.items():
        statistics[key] = round(value, 1)
        
    return statistics

#main function
def main():
    data = read_csv()
    
    #while loop to get number of deliverables to calculate for
    while True:
        try:
            num_deliverables = int(input("Enter the number of deliverables (1 to 6): "))
            if 1<= num_deliverables <= 6:
                break
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    deliverable_labels = []
    
    #prompting for labels for each deliverable
    for i in range(num_deliverables):
        while True:
            label = input("Enter label for deliverable: ")
            if label in data.columns:
                deliverable_labels.append(label)
                break
            else:
                print("Invalid label. Please enter a valid label.")
    
    summary_statistics = pd.DataFrame(index=["", "Average", "Median", "Highest", "Lowest", "St Dev"])
    
    for label in deliverable_labels:
        deliverable_data = data[label]
        statistics = calculate_statistics(deliverable_data)
        summary_statistics[label] = pd.Series(statistics)
    
    #skip values that are NaN (not a number)
    summary_statistics.dropna(inplace=True)
    
    #print summary statistics
    print(summary_statistics)
main()
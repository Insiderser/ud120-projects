#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    new_data_size = int(float(len(ages)) * 0.9)

    new_data: list[tuple] = []
    for i in range(len(ages)):
        age = ages[i]
        net_worth = net_worths[i]
        new_data.append(tuple([age, net_worth, calculate_error(predictions[i], net_worth)]))

    new_data.sort(key=lambda data: data[2])
    return new_data[:new_data_size]

def calculate_error(prediction, expected_net_worth) -> float:
    return abs(prediction - expected_net_worth)

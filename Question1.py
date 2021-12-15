#creating the nth sum function
def nth_sum(n):
    # Creating the variable for tracking the sum
    total = 0

  # this is used to run a for loop that loops through the range of values 
    for numbers in range(1, n + 1):
        #  adding each value in that range to the variable initially created until the range ends.
        total += numbers

    # Returning the total sum gotten
    return total


# time function to calculate the time taken to run the different inputs
import time

start = time.process_time()
#printing my results
print("The input :: 10, and result :: " + str(nth_sum(10)) + ' and the time taken:: ' + str(time.process_time() - start) + "secs")
print("The input :: 10000, and result :: " + str(nth_sum(10000)) + ' and the time  taken:: ' + str(time.process_time() - start) + "secs")
print("The input :: 1000000, and result :: " + str(nth_sum(1000000)) + ' and the  time taken :: ' + str(time.process_time() - start) + "secs")
print("The input :: 100000000, and result :: " + str(nth_sum(1000000000)) + ' and  the time taken :: ' + str(time.process_time() - start) + "secs")

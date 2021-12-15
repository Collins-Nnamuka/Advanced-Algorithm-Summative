#Importing math library that will be used for rounding up the numbers into integers if there are decimals.
import math

initial_grade = [73, 38, 67, 33]

#Creating a function that takes the list of grades and then returns the results gotten.
def gradingStudents(grade):
    # Initializing the student result.
    final_grade = []

    #Creating a for loop used to loop through the array created for the students' grades.
    for grade in initial_grade:
        # The grade of the student needs to be greater or equal to 38. 
        #Any grade less than 38 can't be rounded up because 40 is the pass mark.  
        #So if the grade is less than 38
        if grade < 38:
            #this is used for appending the grades to the result
            final_grade.append(grade)
        else:
            #If the grade is higher than 38, it should be rounded up.
            #the ceil is used to round up to the nearest integer
            rounded_grade = math.ceil(grade / 5) * 5

  #If the difference between the grade and 
  #the next of 5 should be less than 3( less than or equals 2), 
  #it should be rounded up and added to the rounded_grade array.
            if rounded_grade - grade < 3:
                final_grade.append(rounded_grade)
            else:
                final_grade.append(grade)

    # returning the rounded grades
    return final_grade

# printing the result outputs
print("Original grades are: " + str(initial_grade))
print("Rounded  grades are: " + str(gradingStudents(initial_grade)))

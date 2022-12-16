import numpy as np 

grades_students = np.array([95,88,70,91,57,78,82,85,75,86]) #grades for ten students 
grades_sum = 0 #calculate the sum of the grades 
count = 0  #represent number of student in for loop for each grade

for marks in grades_students:
    grades_sum = (grades_sum + marks) #summing up all the grades 

    count += 1 

#output in calculating average 
grades_average = grades_sum / count 

print ("Average of ten students on the online test is: ", grades_average)


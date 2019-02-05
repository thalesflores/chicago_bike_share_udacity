
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt
import pdb
import collections

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.DictReader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))
print(data_list[0])

input("Press Enter to continue...")
# TASK 1
# DONE: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

"""
function firts_elements(total_elements)
Args:
    total_elements: all elements that user whants to show
    element_list: list that will be printed
Returns:
    list of the first x values
"""

def firts_elements(total_elements):
    for i in range(total_elements):
        print("{} register -> {}\n".format(i + 1, data_list[i]))

firts_elements(20)

input("Press Enter to continue...")
# TASK 2
# DONE: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

"""
function first_elements_by_column(column, total_elements):
Args:
    column: column that will be printed elements
    total_elements: amount of elements that will be printed
Returns:
    output with a specific amount of elements with given column
"""

def first_elements_by_column(column, total_elements):
    for i in range(total_elements):
        print(data_list[i][column.title()])

first_elements_by_column('Gender', 20)


input("Press Enter to continue...")
# TASK 3
# DONE: Create a function to add the columns(features) of a list in another list in the same order

"""
function column_to_list(data, column):
Args:
    data: dictionary that will be transformed
    column: column that will be transformed in list
Returns:
    a list with elements from given column
"""

def column_to_list(data, column):
    column_list = []
    for sample in data:
        column_list.append(sample[column])
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, 'Gender')[:20])

# # ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, 'Gender')) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, 'Gender')) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, 'Gender')[0] == "" and column_to_list(data_list, 'Gender')[1] == "Male", "TASK 3: The list doesn't match."
# # -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# DONE: Count each gender. You should not use a function to do that.
male = sum(sample.get('Gender') == 'Male' for sample in data_list)
female = sum(sample.get('Gender') == 'Female' for sample in data_list)


# # Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 5
# DONE: Create a function to count the genders. Return a list

"""
function count_gender(data):
Args:
    data: dictionary which will be consulted
Returns:
    a list with total amount of gender -> [male, female]
"""

def count_gender(data):
    male = sum(sample.get('Gender') == 'Male' for sample in data)
    female = sum(sample.get('Gender') == 'Female' for sample in data)
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# DONE: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.

"""
function most_popular_gender(data):
Args:
    data: dictionary which will be consulted
Returns:
    which gender has more register in database
"""

def most_popular_gender(data):
    male, female = count_gender(data)
    answer = "Male" if male > female else "Female"
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 7
# DONE: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

"""
function plot_graph_by_field(field):
Args:
    field: specific column that will be analized
Returns:
    a graph from that field
"""

def plot_graph_by_field(field):
    user_type_list = column_to_list(data_list, field)
    types = list(set(user_type_list))
    quantity = count_total_by_fields(field, types)
    create_graph(types, quantity, field)

"""
function count_total_by_fields(field_name, types):
Args:
    field_name: specific column that will be analized
    types: values alocated in passed field
Returns:
    a list with an amount based on type/fields -> [1000, 2000]
"""

def count_total_by_fields(field_name, types):
    total = []
    for type in types:
        total.append(sum(sample.get(field_name) == type for sample in data_list))

    return total

"""
function create_graph(types, quantity, field):
Args:
    types: values alocated in passed field
    quantity: amount of values based on types
    field: specific column that will be analized
Returns:
    a graph
"""

def create_graph(types, quantity, field):
    y_pos = list(range(len(types)))
    plt.bar(y_pos, quantity)
    plt.ylabel('Quantity')
    plt.xlabel(field)
    plt.xticks(y_pos, types)
    plt.title('Quantity by {}'.format(field))
    plt.show(block=True)

plot_graph_by_field('User Type')

input("Press Enter to continue...")
# TASK 8
# DONE: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "It's beacause there are some gender values that has no content and the code only sum fields that is filled with male or female"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 9
# DONE: Find the Minimum, Maximum, Mean and Median trip duration.

"""
function calculate_median(trip_duration_list, list_length):
Args:
    trip_duration_list: list with all total durations
    list_length: length of list
Returns:
    median of list
"""

def calculate_median(trip_duration_list, list_length):
    if length % 2 == 0:
        return (trip_duration_list[list_length//2] + trip_duration_list[list_length//2-1]) / 2
    else:
        return trip_duration_list[(list_length-1)//2]


trip_duration_list = column_to_list(data_list, 'Trip Duration')
trip_duration_list = [ int(x) for x in trip_duration_list ]
trip_duration_list.sort()
length = len(trip_duration_list)

min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = round(float(sum(trip_duration_list))/length)
median_trip = calculate_median(trip_duration_list, length)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# DONE: Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, 'Start Station'))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
Example function with annotations.
Args:
    param1: The first parameter.
    param2: The second parameter.
Returns:
    List of X values

"""

# TASK 12 - Challenge! (Optional)
# DONE: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")

def count_items(column_list):
    item_types = list(set(column_list))
    count_items = list(collections.Counter(column_list).values())

    return item_types, count_items

# ------------ DO NOT CHANGE ANY CODE HERE ------------
column_list = column_to_list(data_list, 'Gender')
types, counts = count_items(column_list)
print("\nTASK 11: Printing results for count_items()")
print("Types:", types, "Counts:", counts)
assert len(types) == 3, "TASK 11: There are 3 types of gender!"
assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
# -----------------------------------------------------

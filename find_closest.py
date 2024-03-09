import time
from generate import generate_objects
def read_data(filename):
    '''

    :param filename:
    :return: list named 'objects'; objects is a list of tuples, each tuple has 2 elements:
    first element is a name of object(type:string), second element is a tuple of coordinates(each tuple element has type:float)

    function opens input file with filename parameter given and using list comprehension:
        1. creates list of strings, each line is string
        2. strips and splits each line with ':' into list of lists of line's contents
        3. strips, and splits the second element from list of lists from previous step
        4. converts all elements of list from previous step to float numbers and then converts the list into a tuple
        5. returns a list of tuples, where in each tuple first element is first element from list of lists(2nd step),
            second element is a tuple which was created in step 4
    '''
    with open(filename) as input_file:
        objects = [(el[0], tuple([float(num) for num in el[1].strip().split(" ")]))
                   for el in [[part for part in line.strip().split(":")]
                              for line in input_file.readlines()]]
        return objects

def distance(point_1, point_2):
    '''

    :param point_1: tuple of 3 float numbers
    :param point_2: tuple of 3 float numbers
    :return: returns distance between two points in 3 coordinate system
    '''
    return ((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2 + (point_1[2]-point_2[2])**2) ** 0.5

# distance = lambda point_1, point_2: ((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2 + (point_1[2]-point_2[2])**2) ** 0.5

def find_pairs(list_of_objects, threshold):
    '''

    :param list_of_objects: list of objects, where object is ('object_name', (tuple of coordinates))
    :param threshold: any number either float of integer
    :return: list of tuples, where each tuple is a pair of two object names ('name', 'name')

    function iterates through a list_of_objects, it gets each element and looks forward,
    starting from the following element until the end of list, searches an element which located within given threshold,
    if pair element found, tuple with this pair being appended to list of pairs 'pairs',
    when iterating is over function returns list of pairs(tuples)
    '''
    pairs = []
    for index in range(len(list_of_objects)):
        for el in list_of_objects[index + 1:]:
            if distance(list_of_objects[index][1], el[1]) <= threshold:
                pairs.append((list_of_objects[index][0], el[0]))
    return pairs

def print_table(data):
    '''

    :param data: list of tuples, which contains pairs of point names, which located within some threshold
    :return: doesn't return anything
    '''
    print(f"{'':_^27}\n|{('Point(1)'):^12}|{('Point(2)'):^12}|\n{'':-^27}")
    for pair in data:
        print(f"|{pair[0]:^12}|{pair[1]:^12}|\n{'':-^27}")


file = input("Enter filename(format: 'filename.txt') for generating objects: ")
num_of_objects = int(input("Enter integer(number of objects) you want to generate: "))
generate_objects(file, num_of_objects)
radius = float(input("Enter number(threshold) for finding pairs: "))

start = time.time()
list_of_tuples = read_data(file)
# print(list_of_tuples)
pairs = find_pairs(list_of_tuples, radius)
end = time.time()

print_table(pairs) #prints paris of points in table
print(f"\nIt takes {round(end-start, 4)} seconds to calculate pairs\n")

#Part 3
#For 100 objects program computes everything approximately for 0.003 sec
#For 1000 objects program computes everything approximately for 0.3 sec
#For 10'000 objects program computes everything approximately for 30 sec
#I saw the trend that every time number of objects increases in 10 times,computation time increases in 100(10^2) times
#So I assume that with 1'000'000 objects computation time will be approximately 300'000 sec(5000 minutes),
# grows like a polynomial(quadratic) function
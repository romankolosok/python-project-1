
import random
def generate_objects(filename, num_of_lines):
    '''
    :param filename: name of output file in string(path to file)
    :param num_of_lines: number of lines that will be generated
    :return: doesn't return anything

    function get those 2 parameters and file is being opened(or created if file with that name doesn't exist within path)
    and creates 'num_of_lines' lines of objects and writes them into file
    '''
    with open(filename, "w") as output_file:
        for i in range(num_of_lines):
            object_name = "P" + str(i) + ": "
            output_file.write(object_name + str(round(random.uniform(-500, 500), 2)) + " " +
                              str(round(random.uniform(-500, 500), 2)) + " " +
                              str(round(random.uniform(-500, 500), 2)) + "\n")


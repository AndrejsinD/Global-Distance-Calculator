######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: David Andrejsin
# Username: lovelle & heggens              TODO: Andrejsind
#
# Assignment: T10: Oh, The Places You'll Go!
#
# Purpose:  To create a map of locations
#           where the user is originally from or has visited,
#           and to use tuples and lists correctly.
######################################################################
# Acknowledgements:
#
# Original Authors: Dr. Scott Heggen and Dr. Jan Pearce

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import math


class Place:
    def __init__(self, person, name, coordinates, color):
        self.name = name
        self.coordinates = coordinates
        self.person = person
        self.color = color
        self.gps_pos = "(0, 0)"

    def __str__(self):
        return "({0}, {1}, {2}, {3})".format(self.person, self.name, self.gps_pos, self.color)

    def place_pin(self):
        """
        This function places a pin on the world map.

        :param window: the window object where the pin will be placed
        :param place: a tuple object describing a place to be put on the map
        :return: None
        """

        pin = turtle.Turtle()
        pin.penup()
        pin.color(self.color)  # Set the pin to user's chosen color
        pin.shape("circle")  # Sets the pin to a circle shape

        # Logically, the denominator for longitude should be 360; lat should be 180.
        # These values (195 and 120) were determined through testing to account for
        # the extra white space on the edges of the map. You shouldn't change them!
        pin.goto(self.coordinates[0], self.coordinates[1])
        pin.stamp()  # Stamps on the location
        text = "{0}'s place:\n    {1}".format(self.person, self.name)  # Setting up pin label
        pin.write(text, font=("Arial", 10, "bold"))

    def gps_location(self):
        latitude = self.coordinates[0] * 2 / wn.window_width() * 195
        longitude = self.coordinates[1] * 2 / wn.window_height() * 120
        latitude = round(latitude, 6)
        longitude = round(longitude, 6)
        self.gps_pos = (latitude, longitude)
        return latitude, longitude


def parse_file(filename):
    """
    Iterates through the file, and creates the list of places

    :param filename: the name of the file to be opened
    :return: a list representing multiple places
    """

    #####################################################
    # You do not need to modify this function!
    #####################################################

    file_content = open(filename, 'r')           # Opens file for reading

    str_num = file_content.readline()           # The first line of the file, which is the number of entries in the file
    str_num = int(str_num[:-1])                 # The '/n' character needs to be removed

    places_list = []
    for i in range(str_num):
        places_list.append(extract_place(file_content))         # Assembles the list of places

    file_content.close()

    return places_list


def handle_mouse_event(x, y):
    pin = turtle.Turtle()
    pin.penup()
    pin.goto(x, y)
    pin.stamp()
    name = input("Enter your name ")
    place_name = input("Enter the name of your place ")
    color = input("What is the color of your pin? ")
    pos = pin.position()
    pin1 = Place(name, place_name, pos, color)
    pin1.place_pin()
    gps_pos = pin1.gps_location()
    print(pin1)
    gps.append(gps_pos)
    print("Your total trip distance is", calculate_distance(), "km")


def calculate_distance():
    total_distance = 0
    if len(gps) > 1:
        for i in range(len(gps)-1):
            distance = 69 * math.sqrt((gps[i][0] - gps[i+1][0])**2 + (gps[i][1] - gps[i+1][1])**2)
            total_distance = distance + total_distance
    return total_distance


def closer():
    quit()


def place_pin(window, place):
    """
    This function places a pin on the world map.

    :param window: the window object where the pin will be placed
    :param place: a tuple object describing a place to be put on the map
    :return: None
    """

    #####################################################
    # You do not need to modify this function!
    #####################################################

    pin = turtle.Turtle()
    pin.penup()
    if len(place) == 5:
        pin.color(place[4])                     # Set the pin to user's chosen color
    pin.shape("circle")                     # Sets the pin to a circle shape

    # Logically, the denominator for longitude should be 360; lat should be 180.
    # These values (195 and 120) were determined through testing to account for
    # the extra white space on the edges of the map. You shouldn't change them!
    if len(place) == 5:
        pin.goto((place[3] / 195) * window.window_width() / 2, (place[2] / 120) * window.window_height() / 2)
    pin.stamp()                             # Stamps on the location

    text = "Unknown place"
    if len(place) == 5:
        text = "{0}'s place:\n    {1}".format(place[0], place[1])   # Setting up pin label
    pin.write(text, font=("Arial", 10, "bold"))                     # Stamps the text describing the location


def extract_place(file_content):
    """
    This function extracts five lines out of file_content,
    which is a variable holding all of the file content from the calling function. Each extracted line represents,
    in order, the place's name, location, latitude, longitude, and user color. The function returns the five elements
    to the function call as a tuple.

    :param file_content: contents of the file which represents all places
    :return: a tuple representing a single place.
    """

    name = file_content.readline().strip("\n")

    cities = file_content.readline().strip("\n")
    latitudes = file_content.readline().strip("\n")
    longitudes = file_content.readline().strip("\n")
    user_color = file_content.readline().strip("\n")

    master_tuple = (name, cities, float(latitudes), float(longitudes), user_color)

    print(master_tuple)
    return master_tuple


def main():
    """
    This program is designed to place pins on a world map.
    Each place is represented as a tuple.
    Each tuple is then added to a list.
    The list of tuples is used to populate the map.

    :return: None
    """

    # The next three lines set up the world map

    # A sample file was created for you to use here: places.txt
    in_file = input("Enter the name of your input file: ")

    global wn
    global gps
    gps = []
    wn = turtle.Screen()
    wn.setup(width=1100, height=650, startx=0, starty=0)
    wn.bgpic("world-map.gif")
    wn.title("Oh, The Places You'll Go!")

    place_list = parse_file(in_file)        # Generates place_list from the file

    # Iterates through each item in the place_list list, calling the place_pin() function
    for place in place_list:
        place_pin(wn, place)  # Adds ONE place to the map for each loop iteration

    gps = []
    wn.onclick(handle_mouse_event)
    wn.onkey(closer, "q")

    wn.listen()
    wn.mainloop()

    print("Map created!")


if __name__ == "__main__":
    main()

# This script will read in 
# 1. a list of songs 
#
# Then output 
# 1. A csv file containing the the list of songs in a random order

import csv
import sys
import random

class Randomize_list(object):

    def __init__(self):
        self.version = 0

    def print_and_log(self, log_file, print_string):
        print(print_string)
        log_file.write(print_string)

    def read_song_list(self, filename, log_file):
        song_names = []
        header_name_dict = []
        number_of_songs = 0
        self.print_and_log(log_file, "\n\rReading song list from file " + filename)

        with open(filename, 'r') as csvfile:
            csv_file = csv.reader(csvfile, delimiter=',')

            #read first row
            header = next(csv_file)

            # Event names start in column index 3 and continue to end
            for header_name in range(len(header)):
                header_name_dict.append(header[header_name])

            #read remaining rows
            for row in csv_file:
                song_names.append(row)
                number_of_songs+=1

        self.print_and_log(log_file, f"Read {number_of_songs} songs")
        return(number_of_songs, song_names)
    
    def randomize(self, number_of_songs, song_names):
        rand_list = []
       # num_songs_remaining = number_of_songs
        for num_songs_remaining in range(number_of_songs, 0, -1):
            random_value = random.randint(0, num_songs_remaining - 1)
            rand_list.append(song_names[random_value])
            print("\n\rNew Random List")
            print(rand_list)
            del song_names[random_value]
            print("\n\rremaining songs")
            print(song_names)

    def randomize_list(self, input_filename, log_file_name):
        with open(log_file_name, 'w') as outlogfile:
            outlogfile.write("Starting Randomizer\n\r")
            number_of_songs, song_names = self.read_song_list(input_filename, outlogfile)
            ramdomized_song_list = self.randomize(number_of_songs, song_names)

if __name__ == '__main__':
    print("\n\r**************************************")
    print("**** Starting randomize song list *****")
    print("**************************************\n\r")

    randomizer = Randomize_list()
    log_file = "log_file.txt"
    randomizer.randomize_list(sys.argv[1], log_file)


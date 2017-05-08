import os

if __name__ == '__main__':
    records_directory = "/Users/rob/Dev/MathGame/records"
    highscore_filename = "highscore.txt"
    filepath_of_record = os.path.join(records_directory, highscore_filename)
    if not os.path.exists(records_directory):
        os.makedirs(records_directory)
    records_file = open(filepath_of_record, 'a')

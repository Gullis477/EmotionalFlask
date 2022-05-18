from csv import writer
import csv
import pandas as pd


def write_static_data(file, data):
    '''Takes data that is a list of lists and writes them in the csv file file'''
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        if len(data) == 1:
            writer.writerow(data)  # Write one row to csv
        elif len(data) > 1:
            writer.writerows(data)  # Write multiple rows to csv

    return file


def add_row_csv(file, data):
    with open(file, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def load_csv_file(file_name):
    data_frame = None
    try:
        data_frame = pd.DataFrame()
        data = pd.DataFrame(pd.read_csv(file_name, dtype='category', sep=','))

        data_frame = data_frame.append(data)

    except FileNotFoundError as Not_Found_Error:
        data_frame = pd.DataFrame()
        print(f'Error Message: {Not_Found_Error}')
    #print(data_frame)
    return data_frame

csv_file = 'csvfiles/test.csv'
data = [['Title1', 'Title2', 'Title3'], ['Row1Column1', 'Row1Column2', 'Row1Column3'], ['Row2Column1', 'Row2Column2', 'Row2Column3'], ['Row3Column1', 'Row3Column2', 'Row3Column3']]
add_data = ["AddRow1", "AddRow1", "AddRow1"]

write_static_data(csv_file, data)
add_row_csv(csv_file, add_data)
load_csv_file(csv_file)

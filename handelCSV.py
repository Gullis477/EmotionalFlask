from csv import writer
import pandas as pd


def write_in_csv(file, data):
    '''Takes data that is a list of lists and writes them in the csv file file'''
    if len(data) == 1:
        writer.writerow(data)  # Write one row to csv
    elif len(data) > 1:
        writer.writerows(data)  # Write multiple rows to csv
        writer.writerows(data)  # Write multiple rows to csv

    file.close()
    return file


def load_csv_file(file_name):
    data_frame = None
    try:
        data_frame = pd.DataFrame()
        data = pd.DataFrame(pd.read_csv(file_name, dtype='category', sep=","))

        data_frame = data_frame.append(data)

    except FileNotFoundError as Not_Found_Error:
        data_frame = pd.DataFrame()
        print(f"Error Message: {Not_Found_Error}")
    return data_frame

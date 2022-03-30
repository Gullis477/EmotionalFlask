from csv import writer


def writeincsv( file, data ):
    '''Takes data that is a list of lists and writes them in the csv file file'''
    if len( data ) == 1:
        writer.writerow( data ) # Write one row to csv
    elif len( data ) > 1: 
        writer.writerows( data) # Write multiple rows to csv
        writer.writerows( data ) # Write multiple rows to csv

    file.close()
    return file


def load_csv_as_array(fpath, datatype=np.int0, skip_header=True):
    """
    load a csv file and return as a numpy array
    faster than loading using pandas but all cols must be same datatype
    skips first row by default
    """
    with open(fpath,'r') as dest_f:
        data_reader = csv.reader(dest_f,
                                delimiter = ',',
                                quotechar = '"')
        if skip_header:
            next(data_reader) #skips the header/first line
    
        data = [data for data in data_reader]
    
    return np.asarray(data, datatype)

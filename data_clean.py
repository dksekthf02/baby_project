def readcsv(filename):
    """ This function reads data from csv formatted file.

    1. Save the first line into a tuple.
    >>> baby_label
    ('Name', 'Year', 'Gender', 'Count')

    2. Save the baby data to a list of tuples.
    >>> baby_list[0]
    ('Mary', 1880, 'F', 7065)
    >>> baby_list[1]
    ('Anna', 1880, 'F', 2604)
    """
    ### Your code here



    return baby_label, baby_list

def list_to_dict(L, year):
    """ Make a dictionary that groups babies with
    same name and gender with given amount of years
    starting from 1880.

    if year == 5, then
        ('Mary', 1880, 'F', 7065)
        ('Mary', 1881, 'F', 6919)
        ('Mary', 1882, 'F', 8148)
        ('Mary', 1883, 'F', 8012)
        ('Mary', 1884, 'F', 9217)
    would be grouped into
        key: [('Mary', 1880, 'F')]
        value: 39361
    """
    ### Your code here


    return baby_dict

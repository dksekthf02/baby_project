def number_of_babies(baby_dict, name, year, gender):
    """ Find number of babies when name, year, gender is given.

    name: string,
    year: int(ex 1880)
    gender: char(M or F)

    When grouped by 5 years,
    >>> baby_dict[('Mary', 1880, 'F')]
    39361
    """
    ### Your code here

def top_babies_helper(baby_dict, year, gender):
    """ Given year and gender, find a baby tuple
    which it's name is mostly used.

    When grouped by 5 years,
    >>> top_babies_helper(baby_dict, 2000, 'M')
    ('Jacob', 2000, 'M')
    >>> top_babies_helper(baby_dict, 2000, 'F')
    ('Emily', 2000, 'F')
    """
    ### Your code here


def top_named_babies(baby_dict, year, gender):
    """ Given year and gender, find a baby's name and number
    which it's name is mostly used.

    When grouped by 5 years,
    >>> top_named_babies(baby_dict, 1880, 'F')
    ('Mary', 39361)
    >>> top_named_babies(baby_dict, 2000, 'F')
    ('Emily', 126171)
    """
    ### Your code here

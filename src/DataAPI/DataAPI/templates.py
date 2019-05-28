"""Contains underlying functions serving the routes, including an alternate implementation using pandas"""
import pandas as pd


def num_sum(num_list):
    """
    Takes in an iterable and returns sum of all the numbers in it.

    Parameters
    ----------
    num_list : iterable
        Object containing numeric objects.
        All non-numeric objects in the iterable will be ignored.

    Returns
    -------
    int
        Sum of all the numbers in it.
        If a non-iterable is passed, will return 0

    """
    try:
        iterator = iter(num_list)
        x = 0
        for num in num_list:
            try:
                x += num
            except TypeError:
                x += 0
    except TypeError:
        x = 0
    return x


def num_sum_pandas(num_list):
    """
    Takes in an iterable and returns sum of all the numbers in it. This uses pandas.

    Parameters
    ----------
    num_list : iterable
        Object containing numeric objects.
        All non-numeric objects in the iterable will be ignored.

    Returns
    -------
    int
        Sum of all the numbers in it.
        If a non-iterable is passed, will return 0

    """
    try:
        iterator = iter(num_list)
        df = pd.DataFrame(list(num_list))
        x = pd.to_numeric(df[0], errors='coerce').sum()
    except TypeError:
        x = 0
    return x

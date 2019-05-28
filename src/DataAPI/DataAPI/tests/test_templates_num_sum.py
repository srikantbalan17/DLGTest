from DataAPI.templates import num_sum


def test_num_sum_list():
    """Test if list is summed correctly"""
    assert 6 == num_sum([1,2,3])


def test_num_sum_tuple():
    """Test if tuple is summed correctly"""
    assert 6 == num_sum((1,2,3))


def test_num_sum_range():
    """Test if range is summed correctly"""
    assert 6 == num_sum(range(4))


def test_num_sum_non_iterable():
    """Test if non-iterable argument returns 0"""
    assert 0 == num_sum('a')


def test_num_sum_non_numeric():
    """Test if non-numeric in argument is ignored"""
    assert 3 == num_sum([1,2,'a'])


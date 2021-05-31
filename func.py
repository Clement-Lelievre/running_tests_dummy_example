# I will be using pytest. See video on kitt (week 7 day 1 by Gaetan in French, around 1h09m) and the documentation: https://docs.pytest.org/en/6.2.x/getting-started.html#create-your-first-test

def s(*args : int) -> int :
    '''Sums the args passed and returns the result'''
    a = 0
    for item in args:
        a += item
    return a

def test_result():
    assert s(-1,2,3) == 4
    
    
# in the shell, type : pytest func.py


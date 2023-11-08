from app.my_mod import enlarge



def test_example():
    assert 2+2 == 4



def test_enlarge():
    assert enlarge(10) == 1000


# here is a documented version of the function

def enlarge(n):
    """ This is a docstring.
    This function enlarges a number.
    Pass in n as a parameter.
    Returns a larger version of the number.
    """
    return float(n) * 100



if __name__ == "__main__":


    x = input("Please input a number: ")
    result = enlarge(x)
    print(result)
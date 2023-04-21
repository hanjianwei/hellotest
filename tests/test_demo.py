from hellotest.demo import toupper, tolower

def test_upper_case():
    assert toupper('hello') == 'HELLO'

def test_lower_case():
    assert tolower('HELLO') == 'hello'

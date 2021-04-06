import pytest
@pytest.mark.branch
def conditionValue():
    a=100
    b=20
    if(a>b):
        return a
    elif (a<b):
        return  b
    else:
        return  a==b
import sys

import sum
import pytest
@pytest.mark.parametrize('num1, num2, result',
                    [
                        (7, 3, 10),

                        (3.5, 4.5, 8),
                        ('HELLO', ' World', 'HELLO World'),
                    ]
                    )
def test_add(num1, num2, result):
    assert sum.sum(num1, num2) == result
@pytest.mark.skip(reason="I want to skip this test")
def test_subtract(num1, num2, result):
    assert sum.subratct(num1, num2) == result
@pytest.mark.skipif(sys.version_info>3, reason="I want to skip this test")
def test_multiple(num1, num2, result):
    assert sum.multiply(num1, num2) == result

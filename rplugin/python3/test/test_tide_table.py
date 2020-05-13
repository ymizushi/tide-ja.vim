from tide_ja.tide_table import tide_dict
from tide_ja.tide_table import InvalidKeyException
import pytest

SUCCESS_DICT = dict(
    levels=[65,47,39,44,61,86,113,137,153,159,154,142,127,112,103,101,108,121,135,146,149,142,127,106],
    highs=[
        ((9,3), 159),
        ((19,49), 149),
    ],
    lows=[
        ((2,7), 39),
        ((14,42), 101),
    ]
)

def test_success_tide_dict():
    tide = tide_dict('KW', (20, 1, 1))
    assert tide == SUCCESS_DICT

def test_failed_tide_dict():
    with pytest.raises(InvalidKeyException):
        tide = tide_dict('KW', (20, 13, 1))


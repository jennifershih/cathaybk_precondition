import pytest

from program_logic_1 import STUDENTS, round_grade
from program_logic_2 import bounce


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (33, 33),  # next multiple is 35, still below 40
        (37, 40),  # difference of 3 and the new score reaches 40
        (38, 40),
        (39, 40),
        (73, 75),
        (72, 75),  # difference of exactly 3 counts ("3 以下")
        (71, 71),
        (75, 75),  # already a multiple of 5
    ],
)
def test_round_grade(score, expected):
    assert round_grade(score) == expected


def test_example_students():
    assert {name: round_grade(s) for name, s in STUDENTS.items()} == {
        "德瑞克": 33,
        "尚恩": 75,
        "傑夫": 65,
        "馬基": 40,
    }


def test_bounce_tenth_landing():
    distance, rebound = bounce(100, 10)
    assert distance == pytest.approx(299.609375)
    assert rebound == pytest.approx(0.09765625)


def test_bounce_first_landing():
    assert bounce(100, 1) == (100, 50)

from ..main import (
    saskaitisana,
    atnemsana,
    reizinasana,
    dalisana,
    kapinasana
)
import pytest

def test_saskaitisana():
    assert saskaitisana(4, 5) == 9
    assert saskaitisana(6.0, 4) == 10.0
    assert saskaitisana(2, -3) == -1
    assert saskaitisana(1, 7) == 8
    assert saskaitisana(0.0, 0.0) == 0.0

def test_atnemsana():
    assert atnemsana(9, 7) == 2
    assert atnemsana(3, 5) == -2
    assert atnemsana(6.0, 4.5) == 1.5
    assert atnemsana(0, 5) == -5
    assert atnemsana(5, -10) == 15

def test_dalisana():
    assert dalisana(5, 0) == "Dalīt ar nulli nedrīkst!"
    assert dalisana(10, 2) == 5
    assert dalisana(5, 2) == 2.5
    assert dalisana(-20, 5) == -4
    assert dalisana(2, 2) == 1
    assert dalisana(100, 3) == 33.3

def test_reizinasana():
    assert reizinasana(5, 6) == 30
    assert reizinasana(1, 2) == 2
    assert reizinasana(10, 10) == 100
    assert reizinasana(-2, -5) == 10
    assert reizinasana(4, 3.5) == 14
    
def test_kapinasana():
    assert kapinasana(4, 2) == 16
    assert kapinasana(2, 5) == 32
    assert kapinasana(3, 3) == 27
    assert kapinasana(10, 2) == 100
    assert kapinasana(3, 0) == 1
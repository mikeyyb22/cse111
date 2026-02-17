from barycenters import *
import pytest
from pytest import approx

"""Test calculate_r1"""
def test_calculate_r1():
    assert calculate_r1({"name": "mercury", "mass": "0.055", "distance": "0.39", "radius": "2439.7"}, {"name": "sun", "mass": "332946.049", "distance": "0", "radius": "695700"}) == pytest.approx(9.637956, rel=None, abs=1e-6
    )
    assert calculate_r1({"name": "earth", "mass": "1", "distance": "1", "radius": "6371"}, {"name": "sun", "mass": "332946.049", "distance": "0", "radius": "695700"}) == pytest.approx(449.320697, rel=None, abs=1e-6)
    assert calculate_r1({"name": "jupiter", "mass": "317.8", "distance": "5.20", "radius": "71492"}, {"name": "sun", "mass": "332946.049", "distance": "0", "radius": "695700"}) == pytest.approx(741823.563347, rel=None, abs=1e-6)
    assert calculate_r1({"name": "A", "mass": "1", "distance": "0", "radius": "0"}, {"name": "sun", "mass": "332946.049", "distance": "0", "radius": "695700"}) == pytest.approx(0, rel=None, abs=1e-6)
    assert calculate_r1({"name": "moon", "mass": "0.0123", "distance": "0.00257"}, {"name": "earth", "mass": "1", "distance": "0", "radius": "6371"}) == pytest.approx(4671.545589, rel=None, abs=1e-6)





pytest.main(["-v", "--tb=line", "-rN", __file__])
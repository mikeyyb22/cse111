from pytest import approx
import pytest
from water_flow import *

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == 0.0
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == pytest.approx(0.000, rel=None, abs=1e-3)
    assert pressure_gain_from_water_height(30.2) == pytest.approx(295.628, rel=None, abs=1e-3)
    assert pressure_gain_from_water_height(50.0) == pytest.approx(489.450, rel=None, abs=1e-3)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == pytest.approx(0.000, rel=None, abs=1e-3)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == pytest.approx(0.000, rel=None, abs=1e-3)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == pytest.approx(0.000, rel=None, abs=1e-3)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == pytest.approx(-113.008, rel=None, abs=1e-3)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == pytest.approx(-100.462, rel=None, abs=1e-3)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == pytest.approx(-61.576, rel=None, abs=1e-3)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == pytest.approx(-110.884, rel=None, abs=1e-3)

def test_pressure_lost_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == pytest.approx(0.000, rel=None, abs=1e-3)
    assert pressure_loss_from_fittings(1.65, 0) == pytest.approx(0.000, rel=None, abs=1e-3)
    assert pressure_loss_from_fittings(1.65, 2) == pytest.approx(-0.109, rel=None, abs=1e-3)
    assert pressure_loss_from_fittings(1.75, 2) == pytest.approx(-0.122, rel=None, abs=1e-3)
    assert pressure_loss_from_fittings(1.75, 5) == pytest.approx(-0.306, rel=None, abs=1e-3)

def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == pytest.approx(0, rel=None, abs=1)
    assert reynolds_number(0.048692, 1.65) == pytest.approx(80069, rel=None, abs=1)
    assert reynolds_number(0.048692, 1.75) == pytest.approx(84922, rel=None, abs=1)
    assert reynolds_number(0.286870, 1.65) == pytest.approx(471729, rel=None, abs=1)
    assert reynolds_number(0.286870, 1.75) == pytest.approx(500318, rel=None, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == pytest.approx(0.000, rel=None, abs=1e-3)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == pytest.approx(-163.744, rel=None, abs=1e-3)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == pytest.approx(-184.182, rel=None, abs=1e-3)

def test_convert_kPa_to_psi():
    assert convert_kPa_to_psi(1) == pytest.approx(0.145038, rel=None, abs=1e-3)
    assert convert_kPa_to_psi(500) == pytest.approx(72.5189, rel=None, abs=1e-3)
    assert convert_kPa_to_psi(28.4) == pytest.approx(4.119072, rel=None, abs=1e-3)
    assert convert_kPa_to_psi(1245.3) == pytest.approx(180.615495, rel=None, abs=1e-3)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
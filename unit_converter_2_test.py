import unit_converter_2;
import pytest

def test_unit_converter_2(monkeypatch):
    inputs = iter(['100', 'mi'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert unit_converter_2.unit_converter() == "100 mi is 160934.0 m"

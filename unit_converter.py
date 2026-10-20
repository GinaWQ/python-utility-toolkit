"""Simple unit conversion helpers."""
_LENGTH_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
}
_MASS_TO_KG = {
    "g": 0.001,
    "kg": 1.0,
    "lb": 0.45359237,
}
def convert(value, from_unit, to_unit):
    """Convert length, mass, or temperature between supported units."""
    source = from_unit.strip().lower()
    target = to_unit.strip().lower()
    if source in _LENGTH_TO_METERS and target in _LENGTH_TO_METERS:
        return value * _LENGTH_TO_METERS[source] / _LENGTH_TO_METERS[target]
    if source in _MASS_TO_KG and target in _MASS_TO_KG:
        return value * _MASS_TO_KG[source] / _MASS_TO_KG[target]
    if source in {"c", "f"} and target in {"c", "f"}:
        celsius = value if source == "c" else (value - 32) * 5 / 9
        return celsius if target == "c" else celsius * 9 / 5 + 32
    raise ValueError(f"Cannot convert from '{from_unit}' to '{to_unit}'")


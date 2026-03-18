def transform_data(x: int, y: float, z: str) -> float:
    result = (x * y) / (len(z) + 1) + sum(ord(c) for c in z) % 10
    return round(result, 2)
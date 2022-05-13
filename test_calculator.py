from calculator import calculate_rectangle_area, calculate_triangle_area


def test_calculate_rectangle_area():
    """tests that a rectangle area is equal to height * width"""
    assert calculate_rectangle_area(2, 3) == 6


def test_calculate_triangle_area():
    """tests that a triangle's area is equal to base * height / 2"""
    assert calculate_triangle_area(2, 3) == 3

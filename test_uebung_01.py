import pytest
from uebung_01 import *

# python -m pytest uebung_01.py

# Test cases for gradepoints_to_grade
def test_gradepoints_to_grade__check_for_grades():
    # Arrange
    test_value_percentage = 92.0
    expected_result = "Sehr gut"

    # Act
    result = gradepoints_to_grade(test_value_percentage)
    
    # Assert
    assert result == expected_result


# Test cases for grade_result_percentage
def test_grade_result_percentage__lock_for_percentage_value():
    # Arrange
    test_value_points = 55.0
    test_value_max_points = 75.0
    expected_result =  test_value_points / test_value_max_points * 100.0

    # Act
    result = grade_result_percentage(test_value_points, test_value_max_points)
    
    # Assert
    assert round(result) == round(expected_result)

def test_grade_result_percentage__check_for_percentage_value():
    # Arrange
    test_value_points = "points"
    test_value_max_points = 75.0

    # Act
    with pytest.raises(TypeError):
        grade_result_percentage(test_value_points, test_value_max_points)


def test_grade_result_percentage__check_for_negativ_points_values():
    # Arrange
    test_value_points = -0.01
    test_value_max_points = -15.0

    # Act
    with pytest.raises(ValueError):
        grade_result_percentage(test_value_points, test_value_max_points)

def test_grade_result_percentage__check_for_negativ_max_points_values():
    # Arrange
    test_value_points = 0.01
    test_value_max_points = -0.01

    # Act
    with pytest.raises(ValueError):
        grade_result_percentage(test_value_points, test_value_max_points)
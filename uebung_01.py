import pytest

def grade_result_percentage (points, maxPoints):
    percentage = (points / maxPoints) * 100
    return percentage




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


def test_grade_result_percentage__check_for_negativ_values():
    # Arrange
    test_value_points = -75.0
    test_value_max_points = 75.0

    # Act
    with pytest.raises(ValueError):
        grade_result_percentage(test_value_points, test_value_max_points)
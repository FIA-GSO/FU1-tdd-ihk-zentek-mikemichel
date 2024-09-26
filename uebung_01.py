import pytest

def grade_result_percentage (points, maxPoints):
    if points < 0 or maxPoints < 0:
        raise ValueError("Negative values are not allowed")
    
    percentage = (points / maxPoints) * 100
    return percentage


def gradepoints_to_grade(percentage):
    if percentage >= 92:
        return "Sehr gut"
    elif percentage >= 81:
        return "Gut"
    elif percentage >= 67:
        return "Befriedigend"
    elif percentage >= 50:
        return "Genügend"
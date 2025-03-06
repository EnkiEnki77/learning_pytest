import pytest
from Source.school import School, Teacher, Student, TooManyStudentsError  # Assuming the code is in 'school.py'


@pytest.fixture
def hogwarts():
    """Fixture to create a default Hogwarts school setup."""
    return School(
        students=[Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")],
        teacher=Teacher("Professor McGonagall"),
        course_name="Transfiguration"
    )


def test_add_student_success(hogwarts):
    """Test that a new student can be added successfully."""
    new_student = Student("Neville Longbottom")
    hogwarts.add_student(new_student)
    assert new_student in hogwarts.students


def test_add_student_limit(hogwarts):
    """Test that adding more than 10 students raises an error."""
    for i in range(8):  # Adding 8 more students to reach above the limit of 10
        hogwarts.add_student(Student(f"Student {i}"))

    with pytest.raises(TooManyStudentsError):
        hogwarts.add_student(Student("Draco Malfoy"))


def test_remove_student(hogwarts):
    """Test that a student can be removed."""
    student_to_remove = hogwarts.students[0]
    hogwarts.remove_student(student_to_remove)
    assert student_to_remove not in hogwarts.students


@pytest.mark.parametrize("new_teacher", ["Professor Snape", "Professor Dumbledore"])
def test_change_teacher(hogwarts, new_teacher):
    """Test that a teacher can be changed."""
    hogwarts.change_teacher(Teacher(new_teacher))
    assert hogwarts.teacher.name == new_teacher

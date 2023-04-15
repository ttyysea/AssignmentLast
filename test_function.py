from function import validate_number


def test_people_1_van_0_car_0_input_1():
    input = 1
    expected_result = (1, 0, 0)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_people_0_van_1_car_0_input_11():
    input = 11
    expected_result = (0, 1, 0)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_people_0_van_0_car_1_input_4():
    input = 4
    expected_result = (0, 0, 1)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_people_1_van_1_car_1_input_16():
    input = 16
    expected_result = (1, 1, 1)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_people_0_van_0_car_0_input_0():
    input = 0
    expected_result = (0, 0, 0)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_number_not_integer_input_abc():
    input = "abc"
    expected_result = "ข้อมูลไม่ได้เป็น Integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_number_not_integer_input_1dot1():
    input = 1.1
    expected_result = "ข้อมูลไม่ได้เป็น Integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_number_less_than_0_input_minus_1():
    input = -1
    expected_result = "จำนวนเลขต้องมากกว่าหรือเท่ากับ 0 "
    actual_result = validate_number(input)
    assert expected_result == actual_result

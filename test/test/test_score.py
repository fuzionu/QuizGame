from test.fixture import run
from main import main


def test_percentage_zero():
    # given
    user_input = 'Yes\nDupa\nDupa\nDupa\nDupa'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Incorrect!\nWhat does GPU stand for? Incorrect!\nWhat does RAM stand for? Incorrect!\nWhat does PSU stand for? Incorrect!\nYou got 0 questions correct\nYou got 0.0% correct\n"


def test_percentage_quarter():
    # given
    user_input = 'Yes\nCentral Processing Unit\nDupa\nDupa\nDupa'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Incorrect!\nWhat does RAM stand for? Incorrect!\nWhat does PSU stand for? Incorrect!\nYou got 1 questions correct\nYou got 25.0% correct\n"


def test_percentage_half():
    # given
    user_input = 'Yes\nCentral Processing Unit\nGraphics Processing Unit\nDupa\nDupa'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Correct!\nWhat does RAM stand for? Incorrect!\nWhat does PSU stand for? Incorrect!\nYou got 2 questions correct\nYou got 50.0% correct\n"


def test_percentage_three_quarters():
    # given
    user_input = 'Yes\nCentral Processing Unit\nGraphics Processing Unit\nRandom Access Memory\nDupa'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Correct!\nWhat does RAM stand for? Correct!\nWhat does PSU stand for? Incorrect!\nYou got 3 questions correct\nYou got 75.0% correct\n"


def test_percentage_hundred():
    # given
    user_input = 'Yes\nCentral Processing Unit\nGraphics Processing Unit\nRandom Access Memory\nPower Supply'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Correct!\nWhat does RAM stand for? Correct!\nWhat does PSU stand for? Correct!\nYou got 4 questions correct\nYou got 100.0% correct\n"

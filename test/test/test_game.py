from test.fixture import run


def test_accepted():
    # given
    user_input = 'Yes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Correct!\nWhat does RAM stand for? Correct!\nWhat does PSU stand for? Correct!\nYou got 4 questions correct\nYou got 100.0% correct\n"


def test_declined():
    # given
    user_input = 'No'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Bye...\n"


def test_incorrect_answer_first():
    # given
    user_input = 'Yes\nDupa\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Incorrect!\nWhat does GPU stand for? Correct!\nWhat does RAM stand for? Correct!\nWhat does PSU stand for? Correct!\nYou got 3 questions correct\nYou got 75.0% correct\n"


def test_incorrect_answer_second():
    # given
    user_input = 'Yes\nCentral processing unit\nDupa\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Incorrect!\nWhat does RAM stand for? Correct!\nWhat does PSU stand for? Correct!\nYou got 3 questions correct\nYou got 75.0% correct\n"


def test_incorrect_answer_third():
    # given
    user_input = 'Yes\nCentral processing unit\nGraphics Processing unit\nDupa\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Correct!\nWhat does RAM stand for? Incorrect!\nWhat does PSU stand for? Correct!\nYou got 3 questions correct\nYou got 75.0% correct\n"


def test_incorrect_answer_fourth():
    # given
    user_input = 'Yes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nDupa\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Correct!\nWhat does RAM stand for? Correct!\nWhat does PSU stand for? Incorrect!\nYou got 3 questions correct\nYou got 75.0% correct\n"

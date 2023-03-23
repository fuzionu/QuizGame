from test.fixture import run, answers


def test_accepted_empty_string():
    # given
    user_input = '\nYes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")


def test_accepted_empty_string_many():
    # given
    user_input = '\n\n\nYes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")


def test_accepted_space():
    # given
    user_input = ' \nYes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")


def test_accepted_space_many():
    # given
    user_input = '   \nYes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")

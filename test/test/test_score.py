from test.fixture import run, answers


def test_percentage_zero():
    # given
    user_input = 'Yes\nDupa\nDupa\nDupa\nDupa'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Incorrect", "Incorrect", "Incorrect", "Incorrect")


def test_percentage_quarter():
    # given
    user_input = 'Yes\nCentral Processing Unit\nDupa\nDupa\nDupa'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Incorrect", "Incorrect", "Incorrect")


def test_percentage_half():
    # given
    user_input = 'Yes\nCentral Processing Unit\nGraphics Processing Unit\nDupa\nDupa'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Incorrect", "Incorrect")


def test_percentage_three_quarters():
    # given
    user_input = 'Yes\nCentral Processing Unit\nGraphics Processing Unit\nRandom Access Memory\nDupa'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Incorrect")


def test_percentage_hundred():
    # given
    user_input = 'Yes\nCentral Processing Unit\nGraphics Processing Unit\nRandom Access Memory\nPower Supply'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")

from test.fixture import run, answers


def test_accepted():
    # given
    user_input = 'Yes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")


def test_accepted_lowercase():
    # given
    user_input = 'yes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")


def test_accepted_uppercase():
    # given
    user_input = 'YES\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")


def test_accepted_mixed_case():
    # given
    user_input = 'yEs\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Correct")

from test.fixture import run


def test_accepted():
    # given
    user_input = 'Yes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nPower supply\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Okay! Let's play :)\nWhat does CPU stand for? Correct!\nWhat does GPU stand for? Correct!\nWhat does RAM stand for? Correct!\nWhat does PSU stand for? Correct!\nYou got 4 questions correct\nYou got 100.0% correct\n"

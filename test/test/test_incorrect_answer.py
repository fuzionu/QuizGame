from test.fixture import run


def test_incorrect_answer_first():
    # given
    user_input = ['Yes', 'Dupa', 'Graphics Processing unit', 'Random access memory', 'Power supply']
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Incorrect", "Correct", "Correct", "Correct")


def test_incorrect_answer_second():
    # given
    user_input = ['Yes', 'Central processing unit', 'Dupa', 'Random access memory', 'Power supply']
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Incorrect", "Correct", "Correct")


def test_incorrect_answer_third():
    # given
    user_input = ['Yes', 'Central processing unit', 'Graphics Processing unit', 'Dupa', 'Power supply']
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Incorrect", "Correct")


def test_incorrect_answer_fourth():
    # given
    user_input = 'Yes\nCentral processing unit\nGraphics Processing unit\nRandom access memory\nDupa\n'
    # when
    program_output = run(user_input)
    # then
    assert program_output == answers("Correct", "Correct", "Correct", "Incorrect")


def answers(first: str, second: str, third: str, fourth: str) -> str:
    return f"""Welcome to my computer quiz!
Do you want to play? Okay! Let's play :)
What does CPU stand for? {first}!
What does GPU stand for? {second}!
What does RAM stand for? {third}!
What does PSU stand for? {fourth}!
You got 3 questions correct
You got 75.0% correct
"""

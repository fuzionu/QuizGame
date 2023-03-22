from test.fixture import run


def test_declined():
    # given
    user_input = 'No'
    # when
    program_output = run(user_input)
    # then
    assert program_output == "Welcome to my computer quiz!\nDo you want to play? Bye...\n"

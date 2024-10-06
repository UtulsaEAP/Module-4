'''
Test cases for the reverse_string module.
'''
import reverse_string as reverse_string
ERROR_MSG = "Validate the schema in the README"

def test_four_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["Hello there","Hey","done"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    reverse_string.reverse_string()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ['ereht olleH','yeH']) ,ERROR_MSG

def test_four_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["a","ab","abc","d"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    reverse_string.reverse_string()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ['a','ba','cba']) ,ERROR_MSG

def test_four_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["Oh my!!!","Done"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    reverse_string.reverse_string()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ['!!!ym hO']) ,ERROR_MSG

def test_four_four(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["See Saw","1234","d"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    reverse_string.reverse_string()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ['waS eeS','4321']) ,ERROR_MSG

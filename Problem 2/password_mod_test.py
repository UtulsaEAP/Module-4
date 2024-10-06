'''
Test cases for the password_mod module.
'''
import password_mod as password_mod
ERROR_MSG = "Validate the schema in the README"

def test_two_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["password"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    password_mod.password_mod()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "p@$$word!" in all_outputs , ERROR_MSG

def test_two_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["myBirthday"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    password_mod.password_mod()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "My81rthd@y!" in all_outputs , ERROR_MSG

def test_two_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["secretPzwrd"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    password_mod.password_mod()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "$ecretPzwrd!" in all_outputs , ERROR_MSG
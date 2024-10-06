'''
Test cases for the brute_eq module.
'''
import brute_eq as brute_eq
ERROR_MSG = "Validate the schema in the README"

def test_five_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["8","7","38","3","-5","-1"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    brute_eq.brute_eq()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "x = 3 , y = 2" in all_outputs ,ERROR_MSG
def test_five_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["1","-1","6","1","1","8"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    brute_eq.brute_eq()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "x = 7 , y = 1" in all_outputs ,ERROR_MSG

def test_five_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["5","2","3","4","2","9"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    brute_eq.brute_eq()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "There is no solution" in all_outputs ,ERROR_MSG
    
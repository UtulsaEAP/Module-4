'''
Test cases for the reverse_binary module.
'''
import reverse_binary as reverse_binary
EVEN_ERROR = "The leading digit of the reverse binary representation of an even number should be 0."
ODD_ERROR = "The leading digit of the reverse binary representation of an odd number should be 1."

def test_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["6"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    reverse_binary.reverse_binary()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "011" in all_outputs , EVEN_ERROR    

def test_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["19"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    reverse_binary.reverse_binary()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "11001" in all_outputs , ODD_ERROR

def test_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["255"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    reverse_binary.reverse_binary()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "11111111" in all_outputs , ODD_ERROR

'''
Test cases for the norm module.
'''
import norm as norm
ERROR_MSG = "Validate the schema in the README"

def test_six_one(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["5","30.0","50.0","10.0","100.0","65.0"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    norm.norm()
    captured = capsys.readouterr()
    all_outputs = captured.out.split("\n")
    assert all(x in all_outputs for x in ['0.30','0.50','0.10','1.00','0.65']) ,ERROR_MSG
def test_six_two(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["7","5.0","10.0","15.0","20.0",'25.0','30.0','35.0'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    norm.norm()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ['0.14','0.29','0.43','0.57','0.71','0.86','1.00']) ,ERROR_MSG
def test_six_three(monkeypatch,capsys):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    inputs = iter(["4","99.9","52.5","12.6","200.0"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

    # go about using input() like you normally would:
    norm.norm()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert all(x in all_outputs for x in ['0.50','0.26','0.06','1.00']) ,ERROR_MSG
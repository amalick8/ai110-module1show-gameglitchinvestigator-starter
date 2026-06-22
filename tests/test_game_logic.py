import pytest
from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty

# --- check_guess tests ---

def test_guess_too_low():
    # Guess below secret should return Too Low
    outcome, message = check_guess(30, 77)
    assert outcome == "Too Low"

def test_guess_too_high():
    # Guess above secret should return Too High
    outcome, message = check_guess(90, 77)
    assert outcome == "Too High"

def test_guess_correct():
    # Exact guess should return Win
    outcome, message = check_guess(77, 77)
    assert outcome == "Win"

# --- parse_guess tests ---

def test_parse_valid_number():
    # Normal number string should parse fine
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42

def test_parse_word_input():
    # Words should fail gracefully with helpful message
    ok, value, err = parse_guess("five")
    assert ok == False
    assert err is not None

def test_parse_empty_input():
    # Empty input should fail gracefully
    ok, value, err = parse_guess("")
    assert ok == False

def test_parse_decimal():
    # Decimal should be converted to int
    ok, value, err = parse_guess("45.5")
    assert ok == True
    assert value == 45

# --- update_score tests ---

def test_score_increases_on_win():
    # Winning should add points
    new_score = update_score(0, "Win", 1)
    assert new_score > 0

def test_score_decreases_on_wrong_guess():
    # Wrong guess should subtract points
    new_score = update_score(50, "Too High", 1)
    assert new_score < 50

# --- get_range_for_difficulty tests ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50
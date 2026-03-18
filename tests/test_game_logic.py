from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_too_high_hint_says_go_lower():
    # Bug: status said "Too High" but hint said "Go HIGHER!" (contradiction)
    status, hint = check_guess(60, 50)
    assert status == "Too High"
    assert "LOWER" in hint


def test_too_low_hint_says_go_higher():
    # Symmetric case: status "Too Low" must pair with "Go HIGHER!" hint
    status, hint = check_guess(40, 50)
    assert status == "Too Low"
    assert "HIGHER" in hint


def test_too_high_always_penalizes_score():
    # Bug: "Too High" on an odd attempt_number skipped the -5 penalty
    # (the old guard `if attempt_number % 2 == 0` made odd attempts free)
    score_after = update_score(100, "Too High", attempt_number=1)
    assert score_after == 95


def test_too_high_and_too_low_penalize_equally():
    # Asymmetry glitch: "Too High" was sometimes free while "Too Low" always cost 5
    too_high_score = update_score(100, "Too High", attempt_number=1)
    too_low_score = update_score(100, "Too Low", attempt_number=1)
    assert too_high_score == too_low_score

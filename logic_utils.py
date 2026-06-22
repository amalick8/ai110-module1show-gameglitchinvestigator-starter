def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        # FIX: Clearer error message explaining what format we expect
        return False, None, "Please enter a number using digits (e.g. 5, not 'five')."
    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).
    FIX: Always compare as integers, never convert secret to string.
    """
    # FIX: Force both to int so string vs int bug can never happen
    guess = int(guess)
    secret = int(secret)
    
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.
    FIX: Wrong guesses never add points.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points
    # FIX: Both wrong outcomes just subtract 5, no rewarding bad guesses
    if outcome in ("Too High", "Too Low"):
        return current_score - 5
    return current_score
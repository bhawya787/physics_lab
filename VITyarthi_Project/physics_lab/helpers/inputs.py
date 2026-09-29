import math


def ask_number(text, low=0.0, high=None, allow_low=False):
    while True:
        raw = input(text).strip()
        try:
            value = float(raw)
        except ValueError:
            print("that is not a number, try again")
            continue
        if math.isnan(value) or math.isinf(value):
            print("that number is not usable, try again")
            continue
        if value < low or (value == low and not allow_low):
            word = "at least" if allow_low else "more than"
            print(f"value must be {word} {low}")
            continue
        if high is not None and value > high:
            print(f"value must be {high} or less")
            continue
        return value

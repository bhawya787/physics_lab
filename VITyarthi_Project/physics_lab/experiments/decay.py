import math
from helpers.inputs import ask_number
from helpers.output import show_results, save_log


def calculate(start_amount, half_life, time):
    if start_amount <= 0:
        raise ValueError("starting amount must be positive")
    if half_life <= 0:
        raise ValueError("half life must be positive")
    if time < 0:
        raise ValueError("time cannot be negative")
    decay_constant = math.log(2) / half_life
    tau = 1 / decay_constant
    remaining = start_amount * math.exp(-decay_constant * time)
    return {
        "lambda": decay_constant,
        "tau": tau,
        "remaining": remaining,
        "decayed": start_amount - remaining,
    }


def run():
    print("Radioactive Decay")
    start_amount = ask_number("starting amount of nuclei (or mass): ")
    half_life = ask_number("half life (any time unit): ")
    time = ask_number("time passed (same unit): ", allow_low=True)
    result = calculate(start_amount, half_life, time)
    rows = [
        ("Decay constant", result["lambda"], "per time unit"),
        ("Mean life (tau)", result["tau"], "time units"),
        ("Amount remaining", result["remaining"], ""),
        ("Amount decayed", result["decayed"], ""),
    ]
    show_results("Radioactive Decay Results", rows)
    save_log(
        "decay",
        {"start": start_amount, "half_life": half_life, "time": time},
        result,
    )

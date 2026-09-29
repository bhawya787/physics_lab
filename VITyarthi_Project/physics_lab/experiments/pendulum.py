import math
from helpers.inputs import ask_number
from helpers.output import show_results, save_log

G = 9.8


def calculate(length):
    if length <= 0:
        raise ValueError("length must be positive")
    period = 2 * math.pi * math.sqrt(length / G)
    frequency = 1 / period
    return {"period": period, "frequency": frequency}


def run():
    print("Simple Pendulum")
    print("this works best for small swing angles")
    length = ask_number("length of the string in m: ")
    result = calculate(length)
    rows = [
        ("Time period", result["period"], "s"),
        ("Frequency", result["frequency"], "Hz"),
    ]
    show_results("Pendulum Results", rows)
    save_log("pendulum", {"length": length}, result)

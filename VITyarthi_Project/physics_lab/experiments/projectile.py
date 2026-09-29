import math
from helpers.inputs import ask_number
from helpers.output import show_results, save_log

G = 9.8


def calculate(speed, angle):
    if speed <= 0:
        raise ValueError("speed must be positive")
    if angle <= 0 or angle > 90:
        raise ValueError("angle must be above 0 and at most 90")
    rad = math.radians(angle)
    vx = speed * math.cos(rad)
    vy = speed * math.sin(rad)
    flight_time = 2 * vy / G
    max_height = vy ** 2 / (2 * G)
    horizontal_range = vx * flight_time
    return {
        "vx": vx,
        "vy": vy,
        "time": flight_time,
        "height": max_height,
        "range": horizontal_range,
    }


def run():
    print("Projectile Motion")
    speed = ask_number("initial speed in m/s: ")
    angle = ask_number("launch angle in degrees (0 to 90): ", high=90)
    result = calculate(speed, angle)
    rows = [
        ("Velocity in x direction", result["vx"], "m/s"),
        ("Initial velocity in y direction", result["vy"], "m/s"),
        ("Time of flight", result["time"], "s"),
        ("Maximum height", result["height"], "m"),
        ("Horizontal range", result["range"], "m"),
    ]
    show_results("Projectile Motion Results", rows)
    save_log("projectile", {"speed": speed, "angle": angle}, result)

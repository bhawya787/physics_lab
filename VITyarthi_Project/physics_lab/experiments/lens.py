from helpers.inputs import ask_number
from helpers.output import show_results, save_log


def calculate(focal_length, object_distance, object_height):
    if focal_length <= 0 or object_distance <= 0 or object_height <= 0:
        raise ValueError("all values must be positive")
    f = -focal_length
    u = -object_distance
    v = 1 / (1 / f + 1 / u)
    magnification = v / u
    image_height = magnification * object_height
    return {
        "v": v,
        "m": magnification,
        "image_height": image_height,
    }


def run():
    print("Image by a Concave Lens")
    print("enter every distance as a positive number, the program handles signs")
    focal_length = ask_number("focal length in cm: ")
    object_distance = ask_number("object distance in cm: ")
    object_height = ask_number("object height in cm: ")
    result = calculate(focal_length, object_distance, object_height)
    rows = [
        ("Image distance (v)", result["v"], "cm"),
        ("Magnification", result["m"], ""),
        ("Image height", result["image_height"], "cm"),
    ]
    show_results("Concave Lens Results", rows)
    print("the image is virtual, erect and smaller than the object")
    print("it forms on the same side of the lens as the object")
    save_log(
        "lens",
        {"f": focal_length, "u": object_distance, "h": object_height},
        result,
    )

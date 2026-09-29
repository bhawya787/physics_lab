import math
from helpers.inputs import ask_number
from helpers.output import show_results, save_log


def calculate(inductance, capacitance, resistance, voltage, frequency):
    values = [inductance, capacitance, resistance, voltage, frequency]
    if any(v <= 0 for v in values):
        raise ValueError("all values must be positive")
    xl = 2 * math.pi * frequency * inductance
    xc = 1 / (2 * math.pi * frequency * capacitance)
    impedance = math.sqrt(resistance ** 2 + (xl - xc) ** 2)
    current = voltage / impedance
    phase = math.degrees(math.atan2(xl - xc, resistance))
    resonant = 1 / (2 * math.pi * math.sqrt(inductance * capacitance))
    q_factor = math.sqrt(inductance / capacitance) / resistance
    return {
        "xl": xl,
        "xc": xc,
        "impedance": impedance,
        "current": current,
        "phase": phase,
        "resonant": resonant,
        "q": q_factor,
    }


def run():
    print("Series LCR Circuit")
    inductance = ask_number("inductance L in henry: ")
    capacitance = ask_number("capacitance C in farad (like 0.00001): ")
    resistance = ask_number("resistance R in ohm: ")
    voltage = ask_number("source voltage in volt: ")
    frequency = ask_number("source frequency in Hz: ")
    result = calculate(inductance, capacitance, resistance, voltage, frequency)
    rows = [
        ("Inductive reactance", result["xl"], "ohm"),
        ("Capacitive reactance", result["xc"], "ohm"),
        ("Impedance", result["impedance"], "ohm"),
        ("Current", result["current"], "A"),
        ("Phase angle", result["phase"], "degrees"),
        ("Resonant frequency", result["resonant"], "Hz"),
        ("Quality factor", result["q"], ""),
    ]
    show_results("LCR Circuit Results", rows)
    if abs(result["phase"]) < 0.01:
        print("the circuit is at resonance")
    elif result["phase"] > 0:
        print("the circuit is more inductive at this frequency")
    else:
        print("the circuit is more capacitive at this frequency")
    save_log(
        "lcr",
        {"L": inductance, "C": capacitance, "R": resistance,
         "V": voltage, "f": frequency},
        result,
    )

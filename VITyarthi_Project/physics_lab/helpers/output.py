import logging

logger = logging.getLogger("physics_lab")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("lab_log.txt", delay=True)
handler.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))
logger.addHandler(handler)


def show_results(title, rows):
    print()
    print("--- " + title + " ---")
    for label, value, unit in rows:
        print(f"{label:<34}{value:>14.4f} {unit}")
    print()


def save_log(name, inputs, results):
    logger.info("%s | inputs=%s | results=%s", name, inputs, results)

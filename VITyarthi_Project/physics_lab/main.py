from experiments import projectile, pendulum, decay, lcr, lens

MENU = {
    "1": ("Projectile motion", projectile.run),
    "2": ("Simple pendulum", pendulum.run),
    "3": ("Radioactive decay", decay.run),
    "4": ("LCR circuit", lcr.run),
    "5": ("Concave lens image", lens.run),
}


def main():
    print("=== Physics Experiment Calculator ===")
    while True:
        print()
        for key, (name, _) in MENU.items():
            print(f"{key}. {name}")
        print("6. Exit")
        try:
            choice = input("pick an option: ").strip()
            if choice == "6":
                print("bye")
                break
            if choice in MENU:
                MENU[choice][1]()
            else:
                print("please pick a number from 1 to 6")
        except (EOFError, KeyboardInterrupt):
            print("\nbye")
            break


if __name__ == "__main__":
    main()

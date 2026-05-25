from typing import Callable

def show_menu() -> None:
    print("\n╔══════════════════════════════╗")
    print("║     SYS ADMIN TOOLKIT        ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Ping a una IP             ║")
    print("║ 2. Comprobar espacio en disco║")
    print("║ 3. Parsear logs SSH          ║")
    print("║ 4. Auditar dispositivo       ║")
    print("║ 5. Geolocalizar IP atacante  ║")
    print("║ 6. Generar inventario CSV    ║")
    print("║ 7. Analizar inventario       ║")
    print("║ 8. Generar reporte Excel     ║")
    print("║ 0. Salir                     ║")
    print("╚══════════════════════════════╝")

def main() -> None:
    options: dict[str, Callable] = {}

    while True:
        show_menu()
        choice: str = input("\nElige una opción: ").strip()

        if choice == "0":
            print("Saliendo...")
            break
        elif choice in options:
            options[choice]()
        else:
            print("Opción no disponible aún.")

if __name__ == "__main__":
    main()
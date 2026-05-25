from typing import Callable
from os_utils import check_ping, check_disk_space

def run_ping() -> None:
    ip: str = input("IP a comprobar: ").strip()
    result: bool = check_ping(ip)
    print(f"{'Responde' if result else 'Sin respuesta'}: {ip}")

def run_disk() -> None:
    path: str = input("Ruta a comprobar (Enter para C:\\): ").strip() or "C:\\"
    check_disk_space(path)

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
    options: dict[str, Callable] = {
        "1": run_ping,
        "2": run_disk,
    }

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
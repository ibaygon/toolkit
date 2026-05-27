from typing import Callable
from os_utils import check_ping, check_disk_space
from log_parser import parse_failed_ips, print_failed_summary
from network_models import Router, Server
from threat_intel import print_threat_table
from generate_inventory import generate_inventory
from inventory_manager import load_inventory, filter_vulnerable, group_by_department, generate_excel_report

def run_ping() -> None:
    ip: str = input("IP a comprobar: ").strip()
    result: bool = check_ping(ip)
    print(f"{'Responde' if result else 'Sin respuesta'}: {ip}")

def run_disk() -> None:
    path: str = input("Ruta a comprobar (Enter para C:\\): ").strip() or "C:\\"
    check_disk_space(path)

def run_log_parser() -> None:
    log_path: str = input("Ruta al archivo de log (Enter para data/auth.log): ").strip() or "data/auth.log"
    failed_ips: dict[str, int] = parse_failed_ips(log_path)
    print_failed_summary(failed_ips)

def run_audit() -> None:
    print("\nDispositivos de ejemplo:")
    devices = [
        Router("router-01", "192.168.1.1", "AA:BB:CC:DD:EE:01", "Cisco ISR 4321"),
        Server("server-01", "192.168.1.10", "AA:BB:CC:DD:EE:02", "Ubuntu 22.04"),
    ]
    for device in devices:
        device.audit_device()

def run_geolocate() -> None:
    log_path: str = input("Ruta al archivo de log (Enter para data/auth.log): ").strip() or "data/auth.log"
    failed_ips: dict[str, int] = parse_failed_ips(log_path)
    print_threat_table(failed_ips)

def run_generate_inventory() -> None:
    generate_inventory()

def run_analyze_inventory() -> None:
    df = load_inventory()
    vulnerable = filter_vulnerable(df)
    print(f"\nServidores vulnerables: {len(vulnerable)} de {len(df)}")
    print("\nPor departamento:")
    print(group_by_department(vulnerable).to_string(index=False))

def run_excel_report() -> None:
    df = load_inventory()
    vulnerable = filter_vulnerable(df)
    generate_excel_report(vulnerable)

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
        "3": run_log_parser,
        "4": run_audit,
        "5": run_geolocate,
        "6": run_generate_inventory,
        "7": run_analyze_inventory,
        "8": run_excel_report,
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
            print("Opción no válida.")

if __name__ == "__main__":
    main()
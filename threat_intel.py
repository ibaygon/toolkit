import requests
from typing import Optional

def geolocate_ip(ip: str) -> Optional[dict]:
    """Consulta ipinfo.io y devuelve país y organización."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error consultando {ip}: {e}")
        return None

def print_threat_table(failed_ips: dict[str, int]) -> None:
    print(f"\n{'IP':<20} {'Intentos':<10} {'País':<15} {'Organización'}")
    print("─" * 70)

    for ip, count in sorted(failed_ips.items(), key=lambda x: x[1], reverse=True):
        data = geolocate_ip(ip)
        if data:
            country: str = data.get("country", "Desconocido")
            org: str     = data.get("org", "Desconocida")[:30]
        else:
            country, org = "Error", "Error"

        print(f"{ip:<20} {count:<10} {country:<15} {org}")
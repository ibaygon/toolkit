import subprocess
import os
import shutil
from typing import Optional

def check_ping(ip: str) -> bool:
    """Hace ping a una IP y devuelve True si responde."""
    try:
        result = subprocess.run(
            ["ping", "-n", "1", ip],   # -n en Windows, -c en Linux/Mac
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def check_disk_space(path: str = "C:\\") -> Optional[float]:
    """
    Comprueba el espacio libre en disco.
    Lanza alerta si es menor al 20%.
    Devuelve el porcentaje libre.
    """
    try:
        total, used, free = shutil.disk_usage(path)
        percent_free: float = (free / total) * 100

        print(f"\nDisco: {path}")
        print(f"  Total : {total // (2**30)} GB")
        print(f"  Usado : {used  // (2**30)} GB")
        print(f"  Libre : {free  // (2**30)} GB ({percent_free:.1f}%)")

        if percent_free < 20:
            print(f"  ⚠️  ALERTA: espacio libre por debajo del 20%")
        else:
            print(f"  ✅ Espacio libre suficiente")

        return percent_free
    except FileNotFoundError:
        print(f"Ruta no encontrada: {path}")
        return None
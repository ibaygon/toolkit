class NetworkDevice:
    def __init__(self, hostname: str, ip: str, mac: str) -> None:
        self.hostname: str = hostname
        self.ip: str = ip
        self.mac: str = mac

    def audit_device(self) -> None:
        print(f"\nDispositivo: {self.hostname} ({self.ip})")
        print("  - Verificar actualizaciones de firmware")
        print("  - Revisar logs de acceso")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(hostname={self.hostname}, ip={self.ip})"


class Router(NetworkDevice):
    def __init__(self, hostname: str, ip: str, mac: str, model: str) -> None:
        super().__init__(hostname, ip, mac)
        self.model: str = model

    def audit_device(self) -> None:
        print(f"\nRouter: {self.hostname} ({self.ip}) — Modelo: {self.model}")
        print("  - Verificar reglas de firewall y ACLs")
        print("  - Comprobar que SSH está deshabilitado y se usa solo consola local")
        print("  - Revisar tabla de enrutamiento por rutas sospechosas")


class Server(NetworkDevice):
    def __init__(self, hostname: str, ip: str, mac: str, os_name: str) -> None:
        super().__init__(hostname, ip, mac)
        self.os_name: str = os_name

    def audit_device(self) -> None:
        print(f"\nServidor: {self.hostname} ({self.ip}) — OS: {self.os_name}")
        print("  - Verificar que no hay puertos abiertos innecesarios")
        print("  - Comprobar usuarios con privilegios root/admin")
        print("  - Revisar integridad de archivos del sistema")
import time
import random

class Servidor:
    def __init__(self, nombre, capacidad_maxima=6):
        self.nombre = nombre
        self.capacidad_maxima = capacidad_maxima
        self.ip_bloqueadas = set()
        self.carga_actual = 0

    def esta_bloqueada(self, ip):
        return ip in self.ip_bloqueadas

    def bloquear_ip(self, ip, origen="Desconocido"):
        if ip not in self.ip_bloqueadas:
            self.ip_bloqueadas.add(ip)
            print(f"🔒 [{origen}] IP {ip} bloqueada y expulsada de la red.")

    def procesar_peticion(self, ip, accion):
        if self.esta_bloqueada(ip):
            print(f"🚫 [RED] Paquete descartado de IP bloqueada: {ip}")
            return False

        self.carga_actual += 1
        print(f"⚙️  [SERVIDOR] Procesando acción '{accion}' de {ip} | Carga actual: {self.carga_actual}/{self.capacidad_maxima}")
        time.sleep(0.03)
        self.carga_actual = max(0, self.carga_actual - 1)
        return True


class DefensorFrontal:
    """Agente 1: Puerta de enlace."""
    def __init__(self, servidor):
        self.servidor = servidor

    def evaluar(self, ip, accion):
        if self.servidor.esta_bloqueada(ip):
            return False
        return True


class DefensorRemoto:
    """Agente 2: Guardián Anti-DDoS."""
    def __init__(self, servidor, umbral_flood=6):
        self.servidor = servidor
        self.peticiones_recientes = []
        self.umbral_flood = umbral_flood

    def vigilar_y_mitigar(self, ip):
        tiempo_actual = time.time()
        self.peticiones_recientes.append((ip, tiempo_actual))

        self.peticiones_recientes = [
            (i, t) for i, t in self.peticiones_recientes 
            if tiempo_actual - t <= 2.0
        ]

        peticiones_de_esta_ip = sum(1 for i, t in self.peticiones_recientes if i == ip)

        if self.servidor.carga_actual >= self.servidor.capacidad_maxima or peticiones_de_esta_ip >= self.umbral_flood:
            print(f"🚨 [Agente 2 - Guardián DDoS] ¡Saturación o Flood detectado en IP {ip}!")
            self.servidor.bloquear_ip(ip, origen="Defensa Remota de Emergencia")
            return True
        return False


class AuditorInterno:
    """Agente 3: Auditor de contenido interno."""
    def __init__(self, servidor):
        self.servidor = servidor

    def inspeccionar_contenido(self, ip, accion):
        if self.servidor.esta_bloqueada(ip):
            return False

        if accion in ["ACCESO_ROOT", "ROBAR_CODIGO_FUENTE", "BYPASS_ADMIN"]:
            print(f"🕵️‍♂️ [Agente 3 - Auditor Interno] ¡ALERTA! Intento de escalación de privilegios detectado desde {ip}.")
            print(f"⚠️ [Auditor] La acción '{accion}' está estrictamente prohibida.")
            self.servidor.bloquear_ip(ip, origen="Auditoría Interna de Seguridad")
            return False
        
        return True


# --- ACTORES DE LA SIMULACIÓN ---
class AtacanteDDoS:
    def __init__(self, ip):
        self.ip = ip
    def generar_peticion(self):
        return "INUNDACION_PETICIONES"

class ClienteLegitimo:
    def __init__(self, ip):
        self.ip = ip
    def generar_peticion(self):
        return random.choice(["LOGIN_OK", "ACCESO_DATO", "CONSULTAR_PERFIL"])

class InfiltradoRandom:
    def __init__(self, ip):
        self.ip = ip
    def generar_peticion(self):
        intento_malicioso = random.choices([True, False], weights=[0.3, 0.7], k=1)[0]
        if intento_malicioso:
            return random.choice(["ACCESO_ROOT", "ROBAR_CODIGO_FUENTE", "BYPASS_ADMIN"])
        else:
            return random.choice(["LOGIN_OK", "ACCESO_DATO"])


# --- BUCLE DE SIMULACIÓN MULTICAPA ---
if __name__ == "__main__":
    core = Servidor("Matrix Core Server", capacidad_maxima=8)
    agente_frontal = DefensorFrontal(core)
    agente_remoto = DefensorRemoto(core, umbral_flood=7)
    auditor_interno = AuditorInterno(core)

    atacante_ddos = AtacanteDDoS("185.220.101.5")
    cliente_bueno = ClienteLegitimo("192.168.1.50")
    infiltrado = InfiltradoRandom("10.0.0.99")

    print(f"🛡️  Arquitectura de 3 Capas Defensivas Iniciada en {core.nombre}\n" + "="*65)

    for turno in range(1, 9):
        print(f"\n--- Turno {turno} ---")
        
        # 1. Tráfico Legítimo puro
        print(f"👤 [Usuario Legítimo - 192.168.1.50]:")
        if not core.esta_bloqueada(cliente_bueno.ip):
            if not agente_remoto.vigilar_y_mitigar(cliente_bueno.ip):
                acc = cliente_bueno.generar_peticion()
                if auditor_interno.inspeccionar_contenido(cliente_bueno.ip, acc):
                    core.procesar_peticion(cliente_bueno.ip, acc)

        print()

        # 2. Infiltrado Random (Con aviso si ya fue bloqueado)
        print(f"🕵️ [Infiltrado Sigiloso - 10.0.0.99]:")
        if not core.esta_bloqueada(infiltrado.ip):
            if not agente_remoto.vigilar_y_mitigar(infiltrado.ip):
                acc_infiltrado = infiltrado.generar_peticion()
                print(f"👀 [Monitoreo] Infiltrado intenta acción: {acc_infiltrado}")
                if auditor_interno.inspeccionar_contenido(infiltrado.ip, acc_infiltrado):
                    core.procesar_peticion(infiltrado.ip, acc_infiltrado)
        else:
            print(f"🛑 [SISTEMA] IP del Infiltrado ya se encuentra bloqueada.")

        print()

        # 3. Atacante DDoS
        print(f"🤖 [Atacante DDoS - 185.220.101.5]:")
        for _ in range(3):
            if not core.esta_bloqueada(atacante_ddos.ip):
                if not agente_remoto.vigilar_y_mitigar(atacante_ddos.ip):
                    acc_ddos = atacante_ddos.generar_peticion()
                    if auditor_interno.inspeccionar_contenido(atacante_ddos.ip, acc_ddos):
                        core.procesar_peticion(atacante_ddos.ip, acc_ddos)
            else:
                print(f"🛑 [SISTEMA] IP del DDoS ya se encuentra bloqueada.")
                break

        time.sleep(0.6)
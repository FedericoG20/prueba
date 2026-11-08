class OperacionFiscal:
    def __init__(self, concepto: str, importe_neto: float, alicuota: float = 21.0):
        self.concepto = concepto
        self.importe_neto = importe_neto
        self.alicuota = alicuota

    def calcular_iva(self) -> float:
        """Calcula el monto del IVA en base al neto y la alícuota."""
        return self.importe_neto * (self.alicuota / 100)

    def calcular_total(self) -> float:
        """Calcula el importe total sumando el neto más el IVA."""
        return self.importe_neto + self.calcular_iva()

    def mostrar_detalle(self):
        iva = self.calcular_iva()
        total = self.calcular_total()
        print(f"--- Detalle: {self.concepto} ---")
        print(f"Neto: ${self.importe_neto:.2f}")
        print(f"IVA ({self.alicuota}%): ${iva:.2f}")
        print(f"Total con IVA: ${total:.2f}\n")


# --- Prueba de la clase ---
if __name__ == "__main__":
    # Creamos un objeto de tipo OperacionFiscal
    item1 = OperacionFiscal("Honorarios profesionales", 50000.0, 21.0)
    item1.mostrar_detalle()
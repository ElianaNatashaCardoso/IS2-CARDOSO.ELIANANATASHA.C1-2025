from datetime import datetime, timedelta

class Prestamo:
    """
    Modelo de la entidad Prestamo. Registra la transacción.
    (Basado en el diagrama UML)
    """
    def __init__(self, socio, libro):
        # Atributos: -id, -socio, -libro, -fecha_prestamo, -fecha_devolucion_pactada
        self.id = 1 
        self.socio = socio
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        # Fecha pactada: 7 días después del préstamo
        self.fecha_devolucion_pactada = self.fecha_prestamo + timedelta(days=7)

    # Método para registrar el evento (+registrar_prestamo())
    def registrar_prestamo(self):
        return (f"PRÉSTAMO ID:{self.id} | Libro: {self.libro.titulo} "
                f"| Pactada: {self.fecha_devolucion_pactada.strftime('%Y-%m-%d')}")
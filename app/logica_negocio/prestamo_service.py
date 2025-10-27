from domain.socio import Socio
from domain.libro import Libro
from domain.prestamo import Prestamo

class PrestamoDeLibros:
    """
    Servicio principal que coordina la operación de préstamo.
    (Clase PrestamoDeLibros con el método +procesar_prestamo())
    """
    def procesar_prestamo(self, socio: Socio, libro: Libro):
        print(f"\n--- Ejecutando Servicio de Préstamos: {libro.titulo} ---")
        
        
        if not libro.disponible:
            return f"❌ ERROR: El libro '{libro.titulo}' NO está disponible para préstamo."
            
        if not socio.verificar_aptitud():
             return f"❌ ERROR: El socio {socio.nombre} no es apto (tiene multas pendientes)."

       
        
       
        libro.cambiar_estado_disponibilidad(False)
        print(f"Log: Libro actualizado a PRESTADO.")
        
        nuevo_prestamo = Prestamo(socio, libro)
        registro = nuevo_prestamo.registrar_prestamo()
        
        return f"✅ ÉXITO: Préstamo completado. {registro}"